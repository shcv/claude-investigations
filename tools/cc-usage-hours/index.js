const fs = require('fs');
const path = require('path');
const readline = require('readline');
const asciichart = require('asciichart');
const chalk = require('chalk');

// Helper functions
function getWeekNumber(date) {
  const d = new Date(date);
  const yearStart = new Date(d.getFullYear(), 0, 1);
  const weekNumber = Math.ceil((((d - yearStart) / 86400000) + yearStart.getDay() + 1) / 7);
  return `${d.getFullYear()}-W${weekNumber.toString().padStart(2, '0')}`;
}

function formatDuration(minutes) {
  const hours = Math.floor(minutes / 60);
  const mins = Math.round(minutes % 60);
  return `${hours}h ${mins}m`;
}

function getDateKey(date) {
  const d = new Date(date);
  const year = d.getFullYear();
  const month = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

async function parseSessionFile(filePath) {
  const fileStream = fs.createReadStream(filePath);
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  const messages = [];
  let lastModel = null;
  
  for await (const line of rl) {
    if (line.trim()) {
      try {
        const entry = JSON.parse(line);
        if (entry.timestamp && (entry.type === 'user' || entry.type === 'assistant')) {
          // Track the model from assistant messages
          if (entry.type === 'assistant' && entry.message?.model) {
            lastModel = entry.message.model;
          }
          
          // Check if this message contains Task tool usage (indicating subagent)
          let hasTaskTool = false;
          if (entry.type === 'assistant' && entry.message?.content) {
            hasTaskTool = entry.message.content.some(c => c.type === 'tool_use' && c.name === 'Task');
          }
          
          messages.push({
            timestamp: new Date(entry.timestamp),
            type: entry.type,
            sessionId: entry.sessionId,
            model: entry.type === 'assistant' ? entry.message?.model : lastModel,
            hasTaskTool,
            uuid: entry.uuid
          });
        }
      } catch (e) {
        // Skip malformed lines
      }
    }
  }
  
  return messages;
}

async function analyzeUsage(options = {}) {
  const gapThresholdMinutes = options.gapThresholdMinutes || 5;
  const subscription = options.subscription || null;
  const usageMetric = options.usageMetric || 'parallel';
  const showWeekly = options.showWeekly || false;
  const showModels = options.showModels || false;
  const showCharts = options.showCharts || false;
  const showSubagents = options.showSubagents || false;
  const modelFilter = options.modelFilter || null;
  const projectsDir = path.join(process.env.HOME, '.claude', 'projects');
  
  if (!fs.existsSync(projectsDir)) {
    throw new Error('Claude projects directory not found at ~/.claude/projects');
  }

  // Find all session files
  const sessionFiles = [];
  const projectDirs = fs.readdirSync(projectsDir);
  
  for (const projectDir of projectDirs) {
    const fullPath = path.join(projectsDir, projectDir);
    if (fs.statSync(fullPath).isDirectory()) {
      const files = fs.readdirSync(fullPath);
      for (const file of files) {
        if (file.endsWith('.jsonl')) {
          sessionFiles.push(path.join(fullPath, file));
        }
      }
    }
  }

  console.log(chalk.gray(`Found ${chalk.cyan(sessionFiles.length)} session files to analyze...\n`));

  // Parse all sessions
  const allMessages = [];
  for (const file of sessionFiles) {
    const messages = await parseSessionFile(file);
    allMessages.push(...messages);
  }

  // Sort by timestamp
  allMessages.sort((a, b) => a.timestamp - b.timestamp);

  // Calculate usage hours per session
  const sessions = {};
  const gapThresholdMs = gapThresholdMinutes * 60 * 1000;

  for (const msg of allMessages) {
    const sessionId = msg.sessionId;
    
    if (!sessions[sessionId]) {
      sessions[sessionId] = {
        messages: [],
        segments: [],
        taskInvocations: []
      };
    }
    
    sessions[sessionId].messages.push(msg);
    
    // Track Task tool invocations (subagents)
    if (msg.hasTaskTool) {
      sessions[sessionId].taskInvocations.push({
        timestamp: msg.timestamp,
        uuid: msg.uuid
      });
    }
  }

  // Analyze each session for segments
  const weeklyLinear = {};  // Total time per session (parallel sessions add up)
  const weeklyWallClock = {};  // Actual elapsed time (parallel sessions merged)
  const weeklyWorkingHours = {}; // Working hours (1hr gap threshold)
  const modelUsage = {};  // Track usage by model
  const dailyUsage = {};  // Track daily usage for sparkline charts
  const subagentStats = {  // Track subagent usage
    totalInvocations: 0,
    sessionsWithSubagents: 0,
    maxParallelSubagents: 0,
    weeklyInvocations: {},
    estimatedSubagentMinutes: 0,
    weeklySubagentMinutes: {}
  };

  for (const [sessionId, session] of Object.entries(sessions)) {
    const messages = session.messages;
    if (messages.length === 0) continue;
    
    // Track subagent statistics
    if (session.taskInvocations.length > 0) {
      subagentStats.sessionsWithSubagents++;
      subagentStats.totalInvocations += session.taskInvocations.length;
      
      // Estimate subagent execution time
      // We'll assume each subagent runs for 2 minutes on average (conservative estimate)
      const estimatedMinutesPerTask = 2;
      
      // Count parallel subagents within small time windows (30 seconds)
      const subagentWindow = 30000; // 30 seconds
      let maxParallel = 0;
      const parallelGroups = [];
      
      // Group tasks that are invoked close together
      for (let i = 0; i < session.taskInvocations.length; i++) {
        let foundGroup = false;
        const currentTime = session.taskInvocations[i].timestamp;
        
        for (const group of parallelGroups) {
          // Check if this task belongs to an existing group
          const timeDiff = Math.abs(currentTime - group.startTime);
          if (timeDiff <= subagentWindow) {
            group.tasks.push(session.taskInvocations[i]);
            group.endTime = Math.max(group.endTime, currentTime);
            foundGroup = true;
            break;
          }
        }
        
        if (!foundGroup) {
          parallelGroups.push({
            startTime: currentTime,
            endTime: currentTime,
            tasks: [session.taskInvocations[i]]
          });
        }
      }
      
      // Calculate max parallel tasks and estimated time
      for (const group of parallelGroups) {
        maxParallel = Math.max(maxParallel, group.tasks.length);
        
        // For parallel tasks, add the time for all tasks
        const groupMinutes = group.tasks.length * estimatedMinutesPerTask;
        subagentStats.estimatedSubagentMinutes += groupMinutes;
        
        // Track weekly subagent time
        const week = getWeekNumber(group.startTime);
        if (!subagentStats.weeklySubagentMinutes[week]) {
          subagentStats.weeklySubagentMinutes[week] = 0;
        }
        subagentStats.weeklySubagentMinutes[week] += groupMinutes;
      }
      
      subagentStats.maxParallelSubagents = Math.max(subagentStats.maxParallelSubagents, maxParallel);
      
      // Track weekly invocations
      for (const invocation of session.taskInvocations) {
        const week = getWeekNumber(invocation.timestamp);
        if (!subagentStats.weeklyInvocations[week]) {
          subagentStats.weeklyInvocations[week] = 0;
        }
        subagentStats.weeklyInvocations[week]++;
      }
    }

    let segmentStart = messages[0].timestamp;
    let lastTimestamp = messages[0].timestamp;
    let segmentModel = messages[0].model;

    for (let i = 1; i < messages.length; i++) {
      const timeDiff = messages[i].timestamp - lastTimestamp;
      
      if (timeDiff > gapThresholdMs) {
        // End current segment
        const duration = (lastTimestamp - segmentStart) / 1000 / 60; // minutes
        if (duration > 0) {
          session.segments.push({
            start: segmentStart,
            end: lastTimestamp,
            duration,
            week: getWeekNumber(segmentStart),
            model: segmentModel
          });
        }
        segmentStart = messages[i].timestamp;
        segmentModel = messages[i].model;
      }
      
      // Update model if it changes
      if (messages[i].model) {
        segmentModel = messages[i].model;
      }
      
      lastTimestamp = messages[i].timestamp;
    }

    // Add final segment
    const duration = (lastTimestamp - segmentStart) / 1000 / 60;
    if (duration > 0) {
      session.segments.push({
        start: segmentStart,
        end: lastTimestamp,
        duration,
        week: getWeekNumber(segmentStart),
        model: segmentModel
      });
    }
  }

  // Calculate linear hours by week and model
  for (const session of Object.values(sessions)) {
    for (const segment of session.segments) {
      if (!weeklyLinear[segment.week]) {
        weeklyLinear[segment.week] = 0;
      }
      weeklyLinear[segment.week] += segment.duration;
      
      // Track daily usage
      const dateKey = getDateKey(segment.start);
      if (!dailyUsage[dateKey]) {
        dailyUsage[dateKey] = {
          totalMinutes: 0,
          models: {}
        };
      }
      dailyUsage[dateKey].totalMinutes += segment.duration;
      
      // Track model usage
      const modelName = segment.model || 'unknown';
      if (!modelUsage[modelName]) {
        modelUsage[modelName] = {
          totalMinutes: 0,
          weekly: {}
        };
      }
      modelUsage[modelName].totalMinutes += segment.duration;
      
      if (!modelUsage[modelName].weekly[segment.week]) {
        modelUsage[modelName].weekly[segment.week] = 0;
      }
      modelUsage[modelName].weekly[segment.week] += segment.duration;
      
      // Track daily model usage
      if (!dailyUsage[dateKey].models[modelName]) {
        dailyUsage[dateKey].models[modelName] = 0;
      }
      dailyUsage[dateKey].models[modelName] += segment.duration;
    }
  }
  
  // Add subagent time to the parallel totals
  for (const [week, minutes] of Object.entries(subagentStats.weeklySubagentMinutes)) {
    if (!weeklyLinear[week]) {
      weeklyLinear[week] = 0;
    }
    weeklyLinear[week] += minutes;
  }

  // Calculate wall-clock hours (merge overlapping sessions)
  const allSegments = [];
  for (const session of Object.values(sessions)) {
    allSegments.push(...session.segments);
  }
  allSegments.sort((a, b) => a.start - b.start);

  // Merge overlapping segments to get actual wall-clock time
  const mergedSegments = [];
  for (const segment of allSegments) {
    if (mergedSegments.length === 0) {
      mergedSegments.push({...segment});
      continue;
    }

    const last = mergedSegments[mergedSegments.length - 1];
    if (segment.start <= last.end) {
      // Overlapping segments
      last.end = new Date(Math.max(last.end.getTime(), segment.end.getTime()));
      last.duration = (last.end - last.start) / 1000 / 60;
    } else {
      mergedSegments.push({...segment});
    }
  }

  // Calculate wall-clock hours by week
  for (const segment of mergedSegments) {
    const week = getWeekNumber(segment.start);
    if (!weeklyWallClock[week]) {
      weeklyWallClock[week] = 0;
    }
    weeklyWallClock[week] += segment.duration;
  }

  // Calculate working hours (count unique hours with activity)
  const hourlyActivity = new Map(); // key: "YYYY-MM-DD-HH", value: true
  
  for (const msg of allMessages) {
    const date = msg.timestamp;
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const hour = String(date.getHours()).padStart(2, '0');
    const hourKey = `${year}-${month}-${day}-${hour}`;
    const week = getWeekNumber(date);
    
    if (!hourlyActivity.has(hourKey)) {
      hourlyActivity.set(hourKey, { week, date });
    }
  }
  
  // Count working hours by week
  for (const [hourKey, info] of hourlyActivity) {
    if (!weeklyWorkingHours[info.week]) {
      weeklyWorkingHours[info.week] = 0;
    }
    weeklyWorkingHours[info.week] += 1; // Each unique hour counts as 1
  }
  
  // Convert to minutes for consistency with other metrics
  for (const week in weeklyWorkingHours) {
    weeklyWorkingHours[week] *= 60; // Convert hours to minutes
  }

  // Display results
  const weeks = [...new Set([...Object.keys(weeklyWallClock), ...Object.keys(weeklyLinear)])].sort();

  let totalWallClock = 0;
  let totalLinear = 0;
  let totalWorkingHours = 0;
  let totalLinearWithoutSubagents = 0;

  // Calculate totals
  for (const week of weeks) {
    const wallClock = weeklyWallClock[week] || 0;
    const linear = weeklyLinear[week] || 0;
    const workingHours = weeklyWorkingHours[week] || 0;
    const subagentMinutes = subagentStats.weeklySubagentMinutes[week] || 0;
    totalWallClock += wallClock;
    totalLinear += linear;
    totalWorkingHours += workingHours;
    totalLinearWithoutSubagents += (linear - subagentMinutes);
  }

  // Show weekly breakdown if requested
  if (showWeekly) {
    console.log(chalk.bold.cyan('=== WEEKLY USAGE ANALYSIS ===\n'));
    console.log(chalk.gray(`Gap threshold: ${chalk.yellow(gapThresholdMinutes)} minutes\n`));

    for (const week of weeks) {
      const wallClock = weeklyWallClock[week] || 0;
      const linear = weeklyLinear[week] || 0;
      const workingHours = weeklyWorkingHours[week] || 0;

      console.log(chalk.bold.white(`Week ${week}:`));
      console.log(`  ${chalk.magenta('Hours with Activity:')}      ${chalk.magenta(formatDuration(workingHours))} ${chalk.gray(`(${(workingHours / 60).toFixed(1)}h)`)}`);
      console.log(`  ${chalk.blue('Active Conversation Time:')} ${chalk.blue(formatDuration(wallClock))} ${chalk.gray(`(${(wallClock / 60).toFixed(1)}h)`)}`);
      console.log(`  ${chalk.green('Parallel Session Total:')}   ${chalk.green(formatDuration(linear))} ${chalk.gray(`(${(linear / 60).toFixed(1)}h)`)}`);
      const parallelFactor = linear > 0 ? (linear / wallClock).toFixed(2) : 'N/A';
      const factorColor = parallelFactor === 'N/A' ? chalk.gray : 
                         parseFloat(parallelFactor) > 2 ? chalk.yellow :
                         parseFloat(parallelFactor) > 1.5 ? chalk.yellowBright : chalk.white;
      console.log(`  ${chalk.gray('Parallel factor:')}          ${factorColor(parallelFactor + 'x')}\n`);
    }
  }

  console.log(chalk.bold.cyan('=== OVERALL SUMMARY ===\n'));
  console.log(`${chalk.gray('Total weeks analyzed:')} ${chalk.cyan.bold(weeks.length)}`);
  console.log(`${chalk.magenta('Total Hours with Activity:')} ${chalk.magenta.bold(formatDuration(totalWorkingHours))} ${chalk.gray(`(${(totalWorkingHours / 60).toFixed(1)}h)`)}`);
  console.log(`${chalk.blue('Total Active Conversation Time:')} ${chalk.blue.bold(formatDuration(totalWallClock))} ${chalk.gray(`(${(totalWallClock / 60).toFixed(1)}h)`)}`);
  console.log(`${chalk.green('Total Parallel Session Total:')} ${chalk.green.bold(formatDuration(totalLinear))} ${chalk.gray(`(${(totalLinear / 60).toFixed(1)}h)`)}`);
  console.log(`  ${chalk.gray('- Session time:')} ${chalk.white(formatDuration(totalLinearWithoutSubagents))} ${chalk.gray(`(${(totalLinearWithoutSubagents / 60).toFixed(1)}h)`)}`);
  console.log(`  ${chalk.gray('- Estimated subagent time:')} ${chalk.white(formatDuration(subagentStats.estimatedSubagentMinutes))} ${chalk.gray(`(${(subagentStats.estimatedSubagentMinutes / 60).toFixed(1)}h)`)}`);
  
  console.log();
  console.log(`${chalk.magenta('Average Hours with Activity per week:')} ${chalk.magenta(formatDuration(totalWorkingHours / weeks.length))} ${chalk.gray(`(${(totalWorkingHours / 60 / weeks.length).toFixed(1)}h)`)}`);
  console.log(`${chalk.blue('Average Active Conversation Time per week:')} ${chalk.blue(formatDuration(totalWallClock / weeks.length))} ${chalk.gray(`(${(totalWallClock / 60 / weeks.length).toFixed(1)}h)`)}`);
  console.log(`${chalk.green('Average Parallel Session Total per week:')} ${chalk.green(formatDuration(totalLinear / weeks.length))} ${chalk.gray(`(${(totalLinear / 60 / weeks.length).toFixed(1)}h)`)}`);
  const overallParallelFactor = totalLinear > 0 ? (totalLinear / totalWallClock).toFixed(2) : 'N/A';
  const factorColor = overallParallelFactor === 'N/A' ? chalk.gray : 
                     parseFloat(overallParallelFactor) > 2 ? chalk.yellow :
                     parseFloat(overallParallelFactor) > 1.5 ? chalk.yellowBright : chalk.white;
  console.log(`${chalk.gray('Overall parallel factor:')} ${factorColor(overallParallelFactor + 'x')}`);
  console.log(`\n${chalk.bold('Usage intensity:')}`);
  const utilizationRate = (totalWallClock / totalWorkingHours * 100).toFixed(1);
  const utilizationColor = parseFloat(utilizationRate) > 80 ? chalk.green : 
                          parseFloat(utilizationRate) > 60 ? chalk.yellow : chalk.red;
  console.log(`  ${chalk.gray('Hours with Activity → Active Conversation:')} ${utilizationColor(utilizationRate + '%')} ${chalk.gray('of active hours had conversations')}`);
  console.log(`  ${chalk.gray('Active Conversation → Parallel Total:')} ${factorColor((totalLinear / totalWallClock).toFixed(2) + 'x')} ${chalk.gray('parallel sessions')}`);
  
  // Show subagent statistics
  console.log(`\n${chalk.bold('Subagent usage:')}`);
  console.log(`  ${chalk.gray('Total Task invocations:')} ${chalk.cyan(subagentStats.totalInvocations)}`);
  console.log(`  ${chalk.gray('Sessions with subagents:')} ${chalk.cyan(subagentStats.sessionsWithSubagents)}`);
  console.log(`  ${chalk.gray('Max parallel subagents in a session:')} ${chalk.cyan(subagentStats.maxParallelSubagents)}`);
  console.log(`  ${chalk.gray('Average Task invocations per week:')} ${chalk.cyan((subagentStats.totalInvocations / weeks.length).toFixed(1))}`);
  
  console.log();
  
  // Show detailed subagent breakdown if requested
  if (showSubagents && subagentStats.totalInvocations > 0) {
    console.log(chalk.bold.cyan('\n=== SUBAGENT USAGE BREAKDOWN ===\n'));
    
    // Show weekly breakdown
    const subagentWeeks = Object.keys(subagentStats.weeklyInvocations).sort();
    console.log(chalk.bold('Weekly Task invocations and estimated time:'));
    for (const week of subagentWeeks) {
      const count = subagentStats.weeklyInvocations[week];
      const minutes = subagentStats.weeklySubagentMinutes[week] || 0;
      console.log(`  ${chalk.gray(week + ':')} ${chalk.cyan(count)} invocations, ~${chalk.white(formatDuration(minutes))} estimated`);
    }
    
    // Calculate subagent impact on parallel factor
    console.log(chalk.bold('\nSubagent impact analysis:'));
    console.log(`  ${chalk.gray('Sessions using subagents:')} ${chalk.cyan(((subagentStats.sessionsWithSubagents / Object.keys(sessions).length) * 100).toFixed(1) + '%')}`);
    console.log(`  ${chalk.gray('Average Tasks per session with subagents:')} ${chalk.cyan((subagentStats.totalInvocations / subagentStats.sessionsWithSubagents).toFixed(1))}`);
    console.log(chalk.gray('\nNote: The parallel session metric now accounts for both parallel sessions and'));
    console.log(chalk.gray('parallel subagents within sessions, providing a more accurate measure of total'));
    console.log(chalk.gray('computational resources used.'));
  }

  // Model breakdown if requested
  if (showModels) {
    console.log(chalk.bold.cyan('\n=== MODEL USAGE BREAKDOWN ===\n'));
    
    let sortedModels = Object.entries(modelUsage)
      .sort((a, b) => b[1].totalMinutes - a[1].totalMinutes);
    
    // Apply model filter if specified
    if (modelFilter) {
      sortedModels = sortedModels.filter(([model]) => 
        model.toLowerCase().includes(modelFilter)
      );
      
      if (sortedModels.length === 0) {
        console.log(chalk.yellow(`No usage found for ${modelFilter} models.\n`));
        // Don't return early, continue with limit comparison
      } else {
      
      console.log(chalk.gray(`Showing only ${modelFilter.charAt(0).toUpperCase() + modelFilter.slice(1)} models:\n`));
    }
    
    for (const [model, usage] of sortedModels) {
      const hours = usage.totalMinutes / 60;
      // Color model names based on type
      const modelColor = model.includes('opus') ? chalk.hex('#9333EA') : // Purple for Opus
                        model.includes('sonnet') ? chalk.hex('#0EA5E9') : // Sky blue for Sonnet
                        model.includes('haiku') ? chalk.hex('#10B981') : // Green for Haiku
                        chalk.white;
      console.log(modelColor.bold(`${model}:`));
      console.log(`  ${chalk.gray('Total:')} ${modelColor(formatDuration(usage.totalMinutes))} ${chalk.gray(`(${hours.toFixed(1)}h)`)}`);
      console.log(`  ${chalk.gray('Average per week:')} ${modelColor(formatDuration(usage.totalMinutes / weeks.length))} ${chalk.gray(`(${(hours / weeks.length).toFixed(1)}h)`)}`);
      
      // Show weekly breakdown for this model
      const modelWeeks = Object.keys(usage.weekly).sort();
      if (modelWeeks.length > 1) {
        console.log(`  ${chalk.gray('Weekly breakdown:')}`);
        for (const week of modelWeeks) {
          const weekMinutes = usage.weekly[week];
          console.log(`    ${chalk.white(week)}: ${modelColor(formatDuration(weekMinutes))} ${chalk.gray(`(${(weekMinutes / 60).toFixed(1)}h)`)}`);
        }
      }
      console.log();
    }
  }
    
    // Show time metric comparisons
    console.log(chalk.bold.cyan('=== TIME METRIC COMPARISON ===\n'));
    console.log(chalk.bold('Different ways to measure usage time:'));
    console.log(`${chalk.magenta('1. Hours with Activity:')} ${chalk.gray('Count of unique hours where Claude was used')}`);
    console.log(`${chalk.blue('2. Active Conversation Time:')} ${chalk.gray('Actual time spent in conversation (gap-based)')}`);
    console.log(`${chalk.green('3. Parallel Session Total:')} ${chalk.gray('Sum of all session times (parallel sessions add up)')}`);
    console.log(`\n${chalk.bold('Formulas:')}`);
    console.log(chalk.gray('- Utilization Rate = Active Conversation Time / Hours with Activity'));
    console.log(chalk.gray('- Parallel Factor = Parallel Session Total / Active Conversation Time'));
    console.log(chalk.gray('- Effective Usage = Hours with Activity × Utilization Rate × Parallel Factor'));
  }

  // Show sparkline charts if requested
  if (showCharts) {
    console.log(chalk.bold.cyan('\n=== DAILY USAGE SPARKLINE (PAST MONTH) ===\n'));
    
    // Get date range for past month
    const today = new Date();
    const thirtyDaysAgo = new Date(today);
    thirtyDaysAgo.setDate(today.getDate() - 30);
    
    // Create array of dates for past 30 days
    const dates = [];
    const dateLabels = [];
    for (let d = new Date(thirtyDaysAgo); d <= today; d.setDate(d.getDate() + 1)) {
      dates.push(getDateKey(new Date(d)));
      dateLabels.push(`${d.getMonth() + 1}/${d.getDate()}`);
    }
    
    // Prepare data for sparkline
    const dailyHours = dates.map(date => {
      const usage = dailyUsage[date];
      if (!usage) return 0;
      
      // Apply model filter if specified
      if (modelFilter) {
        let filteredMinutes = 0;
        for (const [model, minutes] of Object.entries(usage.models)) {
          if (model.toLowerCase().includes(modelFilter)) {
            filteredMinutes += minutes;
          }
        }
        return filteredMinutes / 60; // Convert to hours
      }
      
      return usage.totalMinutes / 60; // Convert to hours
    });
    
    // Calculate statistics
    const maxHours = Math.max(...dailyHours);
    const totalHours = dailyHours.reduce((a, b) => a + b, 0);
    const avgHours = totalHours / dailyHours.length;
    const daysWithUsage = dailyHours.filter(h => h > 0).length;
    
    // Create asciichart
    if (maxHours > 0) {
      const modelText = modelFilter ? 
        (modelFilter === 'opus' ? chalk.hex('#9333EA')(modelFilter + ' models') : 
         modelFilter === 'sonnet' ? chalk.hex('#0EA5E9')(modelFilter + ' models') : 
         chalk.white(modelFilter + ' models')) : 
        chalk.white('all models');
      console.log(chalk.bold(`Daily usage in hours (${modelText}):`));
      console.log();
      
      // Interpolate data to make the chart wider (double the width)
      const interpolatedHours = [];
      for (let i = 0; i < dailyHours.length - 1; i++) {
        interpolatedHours.push(dailyHours[i]);
        // Add interpolated point between each pair of days
        interpolatedHours.push((dailyHours[i] + dailyHours[i + 1]) / 2);
      }
      interpolatedHours.push(dailyHours[dailyHours.length - 1]);
      
      // Configure chart options
      const chartConfig = {
        offset: 2,
        padding: '       ',
        height: 14,
        colors: [asciichart.cyan],
        format: function (x, i) { return (' ' + x.toFixed(1) + 'h').slice(-6); }
      };
      
      // Create the chart
      const chart = asciichart.plot(interpolatedHours, chartConfig);
      console.log(chalk.cyan(chart));
      console.log();
      
      // Show date range
      console.log(`${chalk.gray('Period:')} ${chalk.white(dateLabels[0])} ${chalk.gray('to')} ${chalk.white(dateLabels[dateLabels.length - 1])}`);
      const usageColor = daysWithUsage > dailyHours.length * 0.8 ? chalk.green :
                        daysWithUsage > dailyHours.length * 0.5 ? chalk.yellow : chalk.red;
      console.log(`${chalk.gray('Days with usage:')} ${usageColor(daysWithUsage)}${chalk.gray('/')}${chalk.white(dailyHours.length)} ${chalk.gray('days')}`);
      console.log(`${chalk.gray('Average daily usage:')} ${chalk.cyan(avgHours.toFixed(1) + 'h')}`);
      console.log(`${chalk.gray('Peak daily usage:')} ${chalk.bold.yellow(maxHours.toFixed(1) + 'h')}`);
      
      // Show which days had peak usage
      const peakDays = [];
      dailyHours.forEach((hours, index) => {
        if (hours === maxHours) {
          peakDays.push(dateLabels[index]);
        }
      });
      if (peakDays.length > 0) {
        console.log(`${chalk.gray('Peak usage on:')} ${chalk.yellow(peakDays.join(', '))}`);
      }
    } else {
      console.log(chalk.yellow(`No usage found in the past 30 days${modelFilter ? ` for ${modelFilter} models` : ''}.`));
    }
    console.log();
  }

  // Estimate for Anthropic's limits
  console.log(chalk.bold.cyan('=== ANTHROPIC LIMIT COMPARISON (WORST CASE) ===\n'));
  
  // Define subscription limits
  const limits = {
    pro: { opus4: { min: 0, max: 0 }, sonnet4: { min: 40, max: 80 } },
    max5x: { opus4: { min: 15, max: 35 }, sonnet4: { min: 140, max: 280 } },
    max20x: { opus4: { min: 24, max: 40 }, sonnet4: { min: 240, max: 480 } }
  };
  
  
  // Find worst week for each metric
  let worstLinearWeek = null;
  let worstLinearHours = 0;
  let worstWorkingHoursWeek = null;
  let worstWorkingHours = 0;
  let worstWallClockWeek = null;
  let worstWallClockHours = 0;
  
  for (const week of weeks) {
    const linear = (weeklyLinear[week] || 0) / 60;
    const workingHours = (weeklyWorkingHours[week] || 0) / 60;
    const wallClock = (weeklyWallClock[week] || 0) / 60;
    
    if (linear > worstLinearHours) {
      worstLinearHours = linear;
      worstLinearWeek = week;
    }
    if (workingHours > worstWorkingHours) {
      worstWorkingHours = workingHours;
      worstWorkingHoursWeek = week;
    }
    if (wallClock > worstWallClockHours) {
      worstWallClockHours = wallClock;
      worstWallClockWeek = week;
    }
  }
  
  // Calculate model usage based on selected tier
  const tierMetrics = {
    hours: weeklyWorkingHours,
    active: weeklyWallClock,
    parallel: weeklyLinear
  };
  
  const selectedMetric = tierMetrics[usageMetric];
  const metricLabel = {
    hours: 'Hours with Activity',
    active: 'Active Conversation Time',
    parallel: 'Parallel Session Total'
  }[usageMetric];
  
  console.log(chalk.gray(`Using ${chalk.bold(metricLabel)} for limit comparison\n`));
  
  // Calculate model usage for the selected tier
  const modelUsageByTier = {};
  
  if (usageMetric === 'parallel') {
    // For parallel tier, use the existing modelUsage (based on linear time)
    Object.assign(modelUsageByTier, modelUsage);
  } else {
    // For hours or active tier, we need to recalculate based on the appropriate metric
    // This is a simplified approach - in reality, we'd need to track model usage per metric
    // For now, we'll scale the model usage proportionally
    const scaleFactor = Object.values(selectedMetric).reduce((a, b) => a + b, 0) / 
                       Object.values(weeklyLinear).reduce((a, b) => a + b, 0);
    
    for (const [model, usage] of Object.entries(modelUsage)) {
      modelUsageByTier[model] = {
        totalMinutes: usage.totalMinutes * scaleFactor,
        weekly: {}
      };
      
      for (const [week, minutes] of Object.entries(usage.weekly)) {
        modelUsageByTier[model].weekly[week] = minutes * scaleFactor;
      }
    }
  }
  
  // Check for Opus 4 and Sonnet 4 models
  const opus4 = modelUsageByTier['claude-opus-4-20250514'];
  const sonnet4 = modelUsageByTier['claude-sonnet-4-20250514'];
  
  // Calculate worst-case usage for intelligent tier selection
  let worstOpus4Hours = 0;
  let worstSonnet4Hours = 0;
  
  if (opus4) {
    for (const week in opus4.weekly) {
      const hours = opus4.weekly[week] / 60;
      if (hours > worstOpus4Hours) {
        worstOpus4Hours = hours;
      }
    }
  }
  
  if (sonnet4) {
    for (const week in sonnet4.weekly) {
      const hours = sonnet4.weekly[week] / 60;
      if (hours > worstSonnet4Hours) {
        worstSonnet4Hours = hours;
      }
    }
  }
  
  // Automatically determine appropriate tier based on usage
  let detectedTier = null;
  
  // Check usage against lower limits to determine tier
  if (worstOpus4Hours > 0 || worstSonnet4Hours > limits.pro.sonnet4.max) {
    // Need at least Max tier if using Opus or exceeding Pro Sonnet limits
    if (worstOpus4Hours >= limits.max20x.opus4.min || worstSonnet4Hours >= limits.max20x.sonnet4.min) {
      detectedTier = 'max20x';
    } else if (worstOpus4Hours >= limits.max5x.opus4.min || worstSonnet4Hours >= limits.max5x.sonnet4.min) {
      detectedTier = 'max5x';
    } else if (worstOpus4Hours > 0) {
      // Any Opus usage requires at least max5x
      detectedTier = 'max5x';
    } else {
      detectedTier = 'pro';
    }
  } else {
    detectedTier = 'pro';
  }
  
  // Use manual subscription if provided, otherwise use detected tier
  const effectiveSubscription = subscription || detectedTier;
  const subKey = effectiveSubscription;
  const subLimits = limits[subKey];
  
  const tierColor = effectiveSubscription === 'pro' ? chalk.blue :
                   effectiveSubscription === 'max5x' ? chalk.yellow :
                   effectiveSubscription === 'max20x' ? chalk.magenta : chalk.white;
  console.log(`${chalk.gray('Comparing against:')} ${tierColor.bold(effectiveSubscription.toUpperCase())} ${chalk.gray('tier limits\n')}`);
  
  if (opus4) {
    // Find worst week for Opus 4 (already calculated hours above)
    let worstOpus4Week = null;
    
    for (const week in opus4.weekly) {
      const hours = opus4.weekly[week] / 60;
      if (hours === worstOpus4Hours) {
        worstOpus4Week = week;
        break;
      }
    }
    
    console.log(`${chalk.hex('#9333EA').bold('Opus 4')} worst week: ${chalk.white(worstOpus4Week)} with ${chalk.hex('#9333EA').bold(worstOpus4Hours.toFixed(1) + 'h')}`);
    if (subLimits.opus4.max === 0) {
      console.log(chalk.red(`✗ Opus 4 is not available on ${effectiveSubscription.toUpperCase()} subscription`));
    } else if (worstOpus4Hours < subLimits.opus4.min) {
      console.log(chalk.green(`✓ Within the expected ${subLimits.opus4.min}-${subLimits.opus4.max}h Opus 4 limit`));
    } else if (worstOpus4Hours <= subLimits.opus4.max) {
      if (effectiveSubscription === 'max20x') {
        console.log(chalk.green(`✓ Within the ${subLimits.opus4.min}-${subLimits.opus4.max}h Opus 4 limit`));
      } else {
        console.log(chalk.yellow(`⚠ In the upper range of the ${subLimits.opus4.min}-${subLimits.opus4.max}h Opus 4 limit`));
      }
    } else {
      console.log(chalk.red(`✗ Exceeds the ${subLimits.opus4.min}-${subLimits.opus4.max}h Opus 4 limit`));
    }
  }
  
  if (sonnet4) {
    // Find worst week for Sonnet 4 (already calculated hours above)
    let worstSonnet4Week = null;
    
    for (const week in sonnet4.weekly) {
      const hours = sonnet4.weekly[week] / 60;
      if (hours === worstSonnet4Hours) {
        worstSonnet4Week = week;
        break;
      }
    }
    
    console.log(`\n${chalk.hex('#0EA5E9').bold('Sonnet 4')} worst week: ${chalk.white(worstSonnet4Week)} with ${chalk.hex('#0EA5E9').bold(worstSonnet4Hours.toFixed(1) + 'h')}`);
    if (subLimits.sonnet4.max === 0) {
      console.log(chalk.red(`✗ Sonnet 4 is not available on ${effectiveSubscription.toUpperCase()} subscription`));
    } else if (worstSonnet4Hours < subLimits.sonnet4.min) {
      console.log(chalk.green(`✓ Within the expected ${subLimits.sonnet4.min}-${subLimits.sonnet4.max}h Sonnet 4 limit`));
    } else if (worstSonnet4Hours <= subLimits.sonnet4.max) {
      if (effectiveSubscription === 'max20x') {
        console.log(chalk.green(`✓ Within the ${subLimits.sonnet4.min}-${subLimits.sonnet4.max}h Sonnet 4 limit`));
      } else {
        console.log(chalk.yellow(`⚠ In the upper range of the ${subLimits.sonnet4.min}-${subLimits.sonnet4.max}h Sonnet 4 limit`));
      }
    } else {
      console.log(chalk.red(`✗ Exceeds the ${subLimits.sonnet4.min}-${subLimits.sonnet4.max}h Sonnet 4 limit`));
    }
  }
  
  console.log(`\n${chalk.bold('Worst week metrics across all models:')}`);
  console.log(`  ${chalk.magenta('Highest Hours with Activity:')} ${chalk.white(worstWorkingHoursWeek)} with ${chalk.magenta.bold(worstWorkingHours.toFixed(1) + 'h')}`);
  console.log(`  ${chalk.blue('Highest Active Conversation Time:')} ${chalk.white(worstWallClockWeek)} with ${chalk.blue.bold(worstWallClockHours.toFixed(1) + 'h')}`);
  console.log(`  ${chalk.green('Highest Parallel Session Total:')} ${chalk.white(worstLinearWeek)} with ${chalk.green.bold(worstLinearHours.toFixed(1) + 'h')}`);
}

module.exports = analyzeUsage;