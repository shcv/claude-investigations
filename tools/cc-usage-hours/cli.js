#!/usr/bin/env node

const analyzeUsage = require('./index.js');

// Parse command line arguments
const args = process.argv.slice(2);

if (args.includes('--help') || args.includes('-h')) {
  console.log(`
cc-usage-hours - Analyze Claude Code usage hours from session data

Usage: 
  cc-usage-hours [options]

Options:
  -g, --gap <minutes>     Minutes of inactivity before new session (default: 5)
  -s, --subscription      Subscription type: pro, max5x, or max20x (optional)
  -t, --tier <metric>     Usage tier for limits: hours, active, or parallel (default: parallel)
  -w, --weekly            Show detailed weekly breakdown
  -m, --models [type]     Show model usage (optional: opus or sonnet to filter)
  -d, --detailed          Show all detailed information (weekly + models)
  -h, --help              Show this help message
  -v, --version           Show version number

This tool analyzes ~/.claude/projects session data and calculates:
- Hours with Activity: Number of unique hours in which Claude was used
- Active Conversation Time: Actual time spent actively using Claude
- Parallel Session Total: Sum of all session times (parallel sessions add up)

Example:
  cc-usage-hours              # Auto-select tier based on usage
  cc-usage-hours --gap 10     # Use 10-minute gap for sessions
  cc-usage-hours -s pro       # Force Pro subscription limits
  cc-usage-hours -s max5x     # Force Max 5x subscription limits
  cc-usage-hours -m opus      # Show only Opus model usage
  cc-usage-hours -m sonnet    # Show only Sonnet model usage
`);
  process.exit(0);
}

if (args.includes('--version') || args.includes('-v')) {
  const pkg = require('./package.json');
  console.log(pkg.version);
  process.exit(0);
}

// Parse gap threshold
let gapThreshold = 5;
const gapIndex = args.findIndex(arg => arg === '-g' || arg === '--gap');
if (gapIndex !== -1 && args[gapIndex + 1]) {
  const gap = parseInt(args[gapIndex + 1]);
  if (!isNaN(gap) && gap > 0) {
    gapThreshold = gap;
  } else {
    console.error('Error: Gap threshold must be a positive number');
    process.exit(1);
  }
}

// Parse subscription type
let subscription = null;
const subIndex = args.findIndex(arg => arg === '-s' || arg === '--subscription');
if (subIndex !== -1 && args[subIndex + 1]) {
  const sub = args[subIndex + 1].toLowerCase();
  if (['pro', 'max', 'max5x', 'max20x'].includes(sub)) {
    subscription = sub;
  } else {
    console.error('Error: Subscription must be one of: pro, max5x, max20x');
    process.exit(1);
  }
}

// Parse usage tier
let usageTier = 'parallel';
const tierIndex = args.findIndex(arg => arg === '-t' || arg === '--tier');
if (tierIndex !== -1 && args[tierIndex + 1]) {
  const tier = args[tierIndex + 1].toLowerCase();
  if (['hours', 'active', 'parallel'].includes(tier)) {
    usageTier = tier;
  } else {
    console.error('Error: Usage tier must be one of: hours, active, parallel');
    process.exit(1);
  }
}

// Parse display options
const showWeekly = args.includes('-w') || args.includes('--weekly');
const showDetailed = args.includes('-d') || args.includes('--detailed');

// Parse model filter
let showModels = false;
let modelFilter = null;
const modelIndex = args.findIndex(arg => arg === '-m' || arg === '--models');
if (modelIndex !== -1) {
  showModels = true;
  // Check if there's a model type specified
  if (modelIndex + 1 < args.length && !args[modelIndex + 1].startsWith('-')) {
    const modelType = args[modelIndex + 1].toLowerCase();
    if (['opus', 'sonnet'].includes(modelType)) {
      modelFilter = modelType;
    }
  }
}

// Run the analysis
analyzeUsage({ 
  gapThresholdMinutes: gapThreshold, 
  subscription,
  usageTier,
  showWeekly: showWeekly || showDetailed,
  showModels: showModels || showDetailed,
  modelFilter
})
  .then(() => process.exit(0))
  .catch(error => {
    console.error('Error:', error.message);
    process.exit(1);
  });