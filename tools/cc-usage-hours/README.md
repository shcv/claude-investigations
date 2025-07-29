# cc-usage-hours

Analyze Claude Code usage from session data in `~/.claude/projects`.

## Install

```bash
npm install -g cc-usage-hours
```

## Usage

```bash
cc-usage-hours                # Auto-detect subscription
cc-usage-hours -s pro         # Specify subscription
cc-usage-hours -t active      # Use active time for limits
cc-usage-hours -w             # Show weekly breakdown
cc-usage-hours -m             # Show model breakdown
cc-usage-hours -m opus        # Show only Opus usage
```

## Options

- `-g, --gap <minutes>` - Inactivity before new session (default: 5)
- `-s, --subscription` - Subscription: pro, max5x, max20x (default: auto)
- `-t, --tier <metric>` - Limit comparison: hours, active, parallel (default: parallel)
- `-w, --weekly` - Show weekly breakdown
- `-m, --models [type]` - Show model usage (optional: opus/sonnet)
- `-d, --detailed` - Show all details

## Metrics

- **Hours with Activity**: Unique hours with Claude usage
- **Active Conversation Time**: Actual conversation time (gap-based)
- **Parallel Session Total**: Sum of all sessions

## Requirements

- Node.js >= 14.0.0
- Claude Code with session data in `~/.claude/projects`

## License

CC0 1.0 Universal - Public Domain Dedication