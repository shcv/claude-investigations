# cc-usage-hours

Analyze your Claude Code usage hours from session data stored in `~/.claude/projects`.

## Installation

```bash
npm install -g cc-usage-hours
```

## Usage

```bash
# Use default 5-minute gap threshold
cc-usage-hours

# Use custom gap threshold (in minutes)
cc-usage-hours --gap 10
```

## What it calculates

The tool provides three levels of time measurement:

1. **Hours with Activity**: Number of unique hours in which Claude was used
   - Counts each hour where you had any interaction with Claude
   - Example: Messages at 9:15am and 9:45am = 1 hour of activity

2. **Active Conversation Time**: Actual time spent actively using Claude
   - Uses a gap threshold (default 5 minutes) to separate conversation sessions
   - Time from first to last message in each continuous conversation

3. **Parallel Session Total**: Sum of all session times
   - Adds up all parallel sessions (if you have multiple Claude instances open)
   - Will be higher than Active Conversation Time if you use parallel sessions

## Output

The tool provides:
- Weekly breakdown of all three metrics
- Overall summary with averages
- Usage intensity percentages
- Model usage breakdown (Opus 4, Sonnet 4, etc.)
- Comparison against Anthropic's estimated weekly limits

## Example Output

```
Week 2025-W30:
  Hours with Activity:      66h 0m (66.0h)
  Active Conversation Time: 24h 33m (24.6h)
  Parallel Session Total:   33h 35m (33.6h)
  Parallel factor:          1.37x
```

## Requirements

- Node.js >= 14.0.0
- Claude Code with session data in `~/.claude/projects`

## License

CC0 1.0 Universal - Public Domain Dedication