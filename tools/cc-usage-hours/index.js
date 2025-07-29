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
  const subscription = options.subscription || null;
  const usageTier = options.usageTier || 'parallel';
  const showWeekly = options.showWeekly || false;
  const showModels = options.showModels || false;
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

  let totalWallClock = 0;
  let totalLinear = 0;
  let totalWorkingHours = 0;

  // Calculate totals
  for (const week of weeks) {
    const wallClock = weeklyWallClock[week] || 0;
    const linear = weeklyLinear[week] || 0;
    const workingHours = weeklyWorkingHours[week] || 0;
    totalWallClock += wallClock;
    totalLinear += linear;
    totalWorkingHours += workingHours;
  }

  // Show weekly breakdown if requested
  if (showWeekly) {
    console.log('=== WEEKLY USAGE ANALYSIS ===\n');
    console.log(`Gap threshold: ${gapThresholdMinutes} minutes\n`);

    for (const week of weeks) {
      const wallClock = weeklyWallClock[week] || 0;
      const linear = weeklyLinear[week] || 0;
      const workingHours = weeklyWorkingHours[week] || 0;

      console.log(`Week ${week}:`);
      console.log(`  Hours with Activity:      ${formatDuration(workingHours)} (${(workingHours / 60).toFixed(1)}h)`);
      console.log(`  Active Conversation Time: ${formatDuration(wallClock)} (${(wallClock / 60).toFixed(1)}h)`);
      console.log(`  Parallel Session Total:   ${formatDuration(linear)} (${(linear / 60).toFixed(1)}h)`);
      console.log(`  Parallel factor:          ${linear > 0 ? (linear / wallClock).toFixed(2) : 'N/A'}x\n`);
    }
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

  // Model breakdown if requested
  if (showModels) {
    console.log('\n=== MODEL USAGE BREAKDOWN ===\n');
    
    let sortedModels = Object.entries(modelUsage)
      .sort((a, b) => b[1].totalMinutes - a[1].totalMinutes);
    
    // Apply model filter if specified
    if (modelFilter) {
      sortedModels = sortedModels.filter(([model]) => 
        model.toLowerCase().includes(modelFilter)
      );
      
      if (sortedModels.length === 0) {
        console.log(`No usage found for ${modelFilter} models.\n`);
        return;
      }
      
      console.log(`Showing only ${modelFilter.charAt(0).toUpperCase() + modelFilter.slice(1)} models:\n`);
    }
    
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
    
    // Show time metric comparisons
    console.log('=== TIME METRIC COMPARISON ===\n');
    console.log('Different ways to measure usage time:');
    console.log('1. Hours with Activity: Count of unique hours where Claude was used');
    console.log('2. Active Conversation Time: Actual time spent in conversation (gap-based)');
    console.log('3. Parallel Session Total: Sum of all session times (parallel sessions add up)');
    console.log('\nFormulas:');
    console.log('- Utilization Rate = Active Conversation Time / Hours with Activity');
    console.log('- Parallel Factor = Parallel Session Total / Active Conversation Time');
    console.log('- Effective Usage = Hours with Activity × Utilization Rate × Parallel Factor');
  }

  // Estimate for Anthropic's limits
  console.log('=== ANTHROPIC LIMIT COMPARISON (WORST CASE) ===\n');
  
  // Define subscription limits
  const limits = {
    pro: { opus4: { min: 0, max: 0 }, sonnet4: { min: 40, max: 80 } },
    max5x: { opus4: { min: 15, max: 35 }, sonnet4: { min: 140, max: 280 } },
    max20x: { opus4: { min: 24, max: 40 }, sonnet4: { min: 240, max: 480 } }
  };
  
  // For 'max' subscription, intelligently choose between 5x and 20x based on usage
  let effectiveSubscription = subscription;
  if (subscription === 'max') {
    // We'll determine this after calculating worst-case usage
    effectiveSubscription = null;
  }
  
  let subKey = effectiveSubscription === 'max' ? 'max5x' : effectiveSubscription;
  let subLimits = subKey ? limits[subKey] : null;
  
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
  
  const selectedMetric = tierMetrics[usageTier];
  const tierLabel = {
    hours: 'Hours with Activity',
    active: 'Active Conversation Time',
    parallel: 'Parallel Session Total'
  }[usageTier];
  
  console.log(`Using ${tierLabel} for limit comparison\n`);
  
  // Calculate model usage for the selected tier
  const modelUsageByTier = {};
  
  if (usageTier === 'parallel') {
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
  
  console.log(`Comparing against: ${effectiveSubscription.toUpperCase()} tier limits\n`);
  
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
    
    console.log(`Opus 4 worst week: ${worstOpus4Week} with ${worstOpus4Hours.toFixed(1)}h`);
    if (subLimits.opus4.max === 0) {
      console.log(`✗ Opus 4 is not available on ${effectiveSubscription.toUpperCase()} subscription`);
    } else if (worstOpus4Hours < subLimits.opus4.min) {
      console.log(`✓ Within the expected ${subLimits.opus4.min}-${subLimits.opus4.max}h Opus 4 limit`);
    } else if (worstOpus4Hours <= subLimits.opus4.max) {
      if (effectiveSubscription === 'max20x') {
        console.log(`✓ Within the ${subLimits.opus4.min}-${subLimits.opus4.max}h Opus 4 limit`);
      } else {
        console.log(`⚠ In the upper range of the ${subLimits.opus4.min}-${subLimits.opus4.max}h Opus 4 limit`);
      }
    } else {
      console.log(`✗ Exceeds the ${subLimits.opus4.min}-${subLimits.opus4.max}h Opus 4 limit`);
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
    
    console.log(`\nSonnet 4 worst week: ${worstSonnet4Week} with ${worstSonnet4Hours.toFixed(1)}h`);
    if (subLimits.sonnet4.max === 0) {
      console.log(`✗ Sonnet 4 is not available on ${effectiveSubscription.toUpperCase()} subscription`);
    } else if (worstSonnet4Hours < subLimits.sonnet4.min) {
      console.log(`✓ Within the expected ${subLimits.sonnet4.min}-${subLimits.sonnet4.max}h Sonnet 4 limit`);
    } else if (worstSonnet4Hours <= subLimits.sonnet4.max) {
      if (effectiveSubscription === 'max20x') {
        console.log(`✓ Within the ${subLimits.sonnet4.min}-${subLimits.sonnet4.max}h Sonnet 4 limit`);
      } else {
        console.log(`⚠ In the upper range of the ${subLimits.sonnet4.min}-${subLimits.sonnet4.max}h Sonnet 4 limit`);
      }
    } else {
      console.log(`✗ Exceeds the ${subLimits.sonnet4.min}-${subLimits.sonnet4.max}h Sonnet 4 limit`);
    }
  }
  
  console.log(`\nWorst week metrics across all models:`);
  console.log(`  Highest Hours with Activity: ${worstWorkingHoursWeek} with ${worstWorkingHours.toFixed(1)}h`);
  console.log(`  Highest Active Conversation Time: ${worstWallClockWeek} with ${worstWallClockHours.toFixed(1)}h`);
  console.log(`  Highest Parallel Session Total: ${worstLinearWeek} with ${worstLinearHours.toFixed(1)}h`);
  
  // Show the selected metric's worst week
  const worstSelectedMetric = {
    hours: { week: worstWorkingHoursWeek, hours: worstWorkingHours },
    active: { week: worstWallClockWeek, hours: worstWallClockHours },
    parallel: { week: worstLinearWeek, hours: worstLinearHours }
  }[usageTier];
  
  console.log(`\n📊 Selected tier (${tierLabel}): ${worstSelectedMetric.week} with ${worstSelectedMetric.hours.toFixed(1)}h`);
  
  // Recommend appropriate subscription tier
  console.log('\n=== RECOMMENDED SUBSCRIPTION TIER ===\n');
  
  // Check if user has any usage at all
  const hasUsage = Object.keys(modelUsage).length > 0;
  
  const tierFits = {
    pro: worstOpus4Hours === 0 && (worstSonnet4Hours <= limits.pro.sonnet4.max || !hasUsage),
    max5x: worstOpus4Hours <= limits.max5x.opus4.max && worstSonnet4Hours <= limits.max5x.sonnet4.max,
    max20x: worstOpus4Hours <= limits.max20x.opus4.max && worstSonnet4Hours <= limits.max20x.sonnet4.max
  };
  
  let recommendedTier = null;
  for (const tier of ['pro', 'max5x', 'max20x']) {
    if (tierFits[tier]) {
      recommendedTier = tier;
      break;
    }
  }
  
  if (recommendedTier) {
    console.log(`Your usage fits within: ${recommendedTier.toUpperCase()}`);
    
    const currentTier = effectiveSubscription || subscription;
    if (currentTier !== recommendedTier) {
      if ((currentTier === 'pro' && ['max5x', 'max20x'].includes(recommendedTier)) ||
          (currentTier === 'max5x' && recommendedTier === 'max20x')) {
        console.log(`⚠️  You may need to upgrade to ${recommendedTier.toUpperCase()} to avoid hitting limits.`);
      }
    } else {
      console.log(`✅ Your current subscription is appropriate for your usage.`);
    }
  } else {
    console.log(`❌ Your usage exceeds all available subscription tiers!`);
  }
}

module.exports = analyzeUsage;