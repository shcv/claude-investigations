const fs = require('fs');
const path = require('path');
const readline = require('readline');

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
          
          messages.push({
            timestamp: new Date(entry.timestamp),
            type: entry.type,
            sessionId: entry.sessionId,
            model: entry.type === 'assistant' ? entry.message?.model : lastModel
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

  console.log(`Found ${sessionFiles.length} session files to analyze...\n`);

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
        segments: []
      };
    }
    
    sessions[sessionId].messages.push(msg);
  }

  // Analyze each session for segments
  const weeklyLinear = {};  // Total time per session (parallel sessions add up)
  const weeklyWallClock = {};  // Actual elapsed time (parallel sessions merged)
  const weeklyWorkingHours = {}; // Working hours (1hr gap threshold)
  const modelUsage = {};  // Track usage by model

  for (const [sessionId, session] of Object.entries(sessions)) {
    const messages = session.messages;
    if (messages.length === 0) continue;

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
    }
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

  console.log('=== WEEKLY USAGE ANALYSIS ===\n');
  console.log(`Gap threshold: ${gapThresholdMinutes} minutes\n`);

  let totalWallClock = 0;
  let totalLinear = 0;
  let totalWorkingHours = 0;

  for (const week of weeks) {
    const wallClock = weeklyWallClock[week] || 0;
    const linear = weeklyLinear[week] || 0;
    const workingHours = weeklyWorkingHours[week] || 0;
    totalWallClock += wallClock;
    totalLinear += linear;
    totalWorkingHours += workingHours;

    console.log(`Week ${week}:`);
    console.log(`  Hours with Activity:      ${formatDuration(workingHours)} (${(workingHours / 60).toFixed(1)}h)`);
    console.log(`  Active Conversation Time: ${formatDuration(wallClock)} (${(wallClock / 60).toFixed(1)}h)`);
    console.log(`  Parallel Session Total:   ${formatDuration(linear)} (${(linear / 60).toFixed(1)}h)`);
    console.log(`  Parallel factor:          ${linear > 0 ? (linear / wallClock).toFixed(2) : 'N/A'}x\n`);
  }

  console.log('=== OVERALL SUMMARY ===\n');
  console.log(`Total weeks analyzed: ${weeks.length}`);
  console.log(`Total Hours with Activity: ${formatDuration(totalWorkingHours)} (${(totalWorkingHours / 60).toFixed(1)}h)`);
  console.log(`Total Active Conversation Time: ${formatDuration(totalWallClock)} (${(totalWallClock / 60).toFixed(1)}h)`);
  console.log(`Total Parallel Session Total: ${formatDuration(totalLinear)} (${(totalLinear / 60).toFixed(1)}h)`);
  console.log(`Average Hours with Activity per week: ${formatDuration(totalWorkingHours / weeks.length)} (${(totalWorkingHours / 60 / weeks.length).toFixed(1)}h)`);
  console.log(`Average Active Conversation Time per week: ${formatDuration(totalWallClock / weeks.length)} (${(totalWallClock / 60 / weeks.length).toFixed(1)}h)`);
  console.log(`Average Parallel Session Total per week: ${formatDuration(totalLinear / weeks.length)} (${(totalLinear / 60 / weeks.length).toFixed(1)}h)`);
  console.log(`Overall parallel factor: ${totalLinear > 0 ? (totalLinear / totalWallClock).toFixed(2) : 'N/A'}x`);
  console.log(`\nUsage intensity:`);
  console.log(`  Hours with Activity → Active Conversation: ${(totalWallClock / totalWorkingHours * 100).toFixed(1)}% of active hours had conversations`);
  console.log(`  Active Conversation → Parallel Total: ${(totalLinear / totalWallClock).toFixed(2)}x parallel sessions`);

  // Model breakdown
  console.log('\n=== MODEL USAGE BREAKDOWN ===\n');
  
  const sortedModels = Object.entries(modelUsage)
    .sort((a, b) => b[1].totalMinutes - a[1].totalMinutes);
  
  for (const [model, usage] of sortedModels) {
    const hours = usage.totalMinutes / 60;
    console.log(`${model}:`);
    console.log(`  Total: ${formatDuration(usage.totalMinutes)} (${hours.toFixed(1)}h)`);
    console.log(`  Average per week: ${formatDuration(usage.totalMinutes / weeks.length)} (${(hours / weeks.length).toFixed(1)}h)`);
    
    // Show weekly breakdown for this model
    const modelWeeks = Object.keys(usage.weekly).sort();
    if (modelWeeks.length > 1) {
      console.log(`  Weekly breakdown:`);
      for (const week of modelWeeks) {
        const weekMinutes = usage.weekly[week];
        console.log(`    ${week}: ${formatDuration(weekMinutes)} (${(weekMinutes / 60).toFixed(1)}h)`);
      }
    }
    console.log();
  }

  // Estimate for Anthropic's limits
  console.log('=== ANTHROPIC LIMIT COMPARISON ===\n');
  const avgWallClockPerWeek = totalWallClock / 60 / weeks.length;
  const avgLinearPerWeek = totalLinear / 60 / weeks.length;
  
  // Check for Opus 4 and Sonnet 4 models
  const opus4 = modelUsage['claude-opus-4-20250514'];
  const sonnet4 = modelUsage['claude-sonnet-4-20250514'];
  
  if (opus4) {
    const opus4PerWeek = opus4.totalMinutes / 60 / weeks.length;
    console.log(`Opus 4 usage: ${opus4PerWeek.toFixed(1)}h per week average`);
    if (opus4PerWeek < 24) {
      console.log(`✓ Within the expected 24-40h Opus 4 limit`);
    } else if (opus4PerWeek < 40) {
      console.log(`⚠ In the upper range of the 24-40h Opus 4 limit`);
    } else {
      console.log(`✗ Exceeds the typical 24-40h Opus 4 limit`);
    }
  }
  
  if (sonnet4) {
    const sonnet4PerWeek = sonnet4.totalMinutes / 60 / weeks.length;
    console.log(`\nSonnet 4 usage: ${sonnet4PerWeek.toFixed(1)}h per week average`);
    if (sonnet4PerWeek < 240) {
      console.log(`✓ Within the expected 240-480h Sonnet 4 limit`);
    } else if (sonnet4PerWeek < 480) {
      console.log(`⚠ In the upper range of the 240-480h Sonnet 4 limit`);
    } else {
      console.log(`✗ Exceeds the typical 240-480h Sonnet 4 limit`);
    }
  }
  
  console.log(`\nTotal Parallel Session hours per week: ${avgLinearPerWeek.toFixed(1)}h`);
}

module.exports = analyzeUsage;