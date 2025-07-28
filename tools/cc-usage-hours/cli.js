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
  -h, --help              Show this help message
  -v, --version           Show version number

This tool analyzes ~/.claude/projects session data and calculates:
- Hours with Activity: Number of unique hours in which Claude was used
- Active Conversation Time: Actual time spent actively using Claude
- Parallel Session Total: Sum of all session times (parallel sessions add up)

Example:
  cc-usage-hours              # Use default 5-minute gap
  cc-usage-hours --gap 10     # Use 10-minute gap for sessions
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

// Run the analysis
analyzeUsage({ gapThresholdMinutes: gapThreshold })
  .then(() => process.exit(0))
  .catch(error => {
    console.error('Error:', error.message);
    process.exit(1);
  });