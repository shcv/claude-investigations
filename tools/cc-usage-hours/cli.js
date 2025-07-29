#!/usr/bin/env node

const analyzeUsage = require('./index.js');
const chalk = require('chalk');

// Parse command line arguments
const args = process.argv.slice(2);

if (args.includes('--help') || args.includes('-h')) {
  console.log(`
${chalk.bold.cyan('cc-usage-hours')} - ${chalk.gray('Analyze Claude Code usage hours from session data')}

${chalk.bold('Usage:')} 
  ${chalk.green('cc-usage-hours')} ${chalk.gray('[options]')}

${chalk.bold('Options:')}
  ${chalk.yellow('-g, --gap')} ${chalk.gray('<minutes>')}     ${chalk.gray('Minutes of inactivity before new session (default: 5)')}
  ${chalk.yellow('-s, --subscription')}      ${chalk.gray('Subscription type: pro, max5x, or max20x (optional)')}
  ${chalk.yellow('-t, --metric')} ${chalk.gray('<type>')}     ${chalk.gray('Usage metric for limits: hours, active, or parallel (default: parallel)')}
  ${chalk.yellow('-w, --weekly')}            ${chalk.gray('Show detailed weekly breakdown')}
  ${chalk.yellow('-m, --models')} ${chalk.gray('[type]')}     ${chalk.gray('Show model usage (optional: opus or sonnet to filter)')}
  ${chalk.yellow('-c, --charts')}            ${chalk.gray('Show sparkline charts of daily usage over past month')}
  ${chalk.yellow('-d, --detailed')}          ${chalk.gray('Show all detailed information (weekly + models)')}
  ${chalk.yellow('-h, --help')}              ${chalk.gray('Show this help message')}
  ${chalk.yellow('-v, --version')}           ${chalk.gray('Show version number')}

${chalk.bold('This tool analyzes')} ${chalk.cyan('~/.claude/projects')} ${chalk.bold('session data and calculates:')}
${chalk.magenta('• Hours with Activity:')} ${chalk.gray('Number of unique hours in which Claude was used')}
${chalk.blue('• Active Conversation Time:')} ${chalk.gray('Actual time spent actively using Claude')}
${chalk.green('• Parallel Session Total:')} ${chalk.gray('Sum of all session times (parallel sessions add up)')}

${chalk.bold('Example:')}
  ${chalk.green('cc-usage-hours')}              ${chalk.gray('# Auto-select tier based on usage')}
  ${chalk.green('cc-usage-hours')} ${chalk.yellow('--gap 10')}     ${chalk.gray('# Use 10-minute gap for sessions')}
  ${chalk.green('cc-usage-hours')} ${chalk.yellow('-s pro')}       ${chalk.gray('# Force Pro subscription limits')}
  ${chalk.green('cc-usage-hours')} ${chalk.yellow('-s max5x')}     ${chalk.gray('# Force Max 5x subscription limits')}
  ${chalk.green('cc-usage-hours')} ${chalk.yellow('-m opus')}      ${chalk.gray('# Show only Opus model usage')}
  ${chalk.green('cc-usage-hours')} ${chalk.yellow('-m sonnet')}    ${chalk.gray('# Show only Sonnet model usage')}
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
    console.error(chalk.red('Error: Gap threshold must be a positive number'));
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
    console.error(chalk.red('Error: Subscription must be one of: pro, max5x, max20x'));
    process.exit(1);
  }
}

// Parse usage metric
let usageMetric = 'parallel';
const metricIndex = args.findIndex(arg => arg === '-t' || arg === '--metric');
if (metricIndex !== -1 && args[metricIndex + 1]) {
  const metric = args[metricIndex + 1].toLowerCase();
  if (['hours', 'active', 'parallel'].includes(metric)) {
    usageMetric = metric;
  } else {
    console.error(chalk.red('Error: Usage metric must be one of: hours, active, parallel'));
    process.exit(1);
  }
}

// Parse display options
const showWeekly = args.includes('-w') || args.includes('--weekly');
const showDetailed = args.includes('-d') || args.includes('--detailed');
const showCharts = args.includes('-c') || args.includes('--charts');

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
  usageMetric,
  showWeekly: showWeekly || showDetailed,
  showModels: showModels || showDetailed,
  showCharts: showCharts || showDetailed,
  modelFilter
})
  .then(() => process.exit(0))
  .catch(error => {
    console.error(chalk.red('Error:'), chalk.red(error.message));
    process.exit(1);
  });