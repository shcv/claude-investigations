# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Node.js CLI tool that analyzes Claude Code usage hours from session data stored in `~/.claude/projects`. It provides three levels of time measurement:

1. **Hours with Activity**: Counts unique hours where Claude was used
2. **Active Conversation Time**: Actual time spent in conversation (configurable gap threshold)
3. **Parallel Session Total**: Sum of all parallel session times

## Commands

**Running the tool:**
```bash
node cli.js                  # Use default 5-minute gap threshold
node cli.js --gap 10        # Use custom gap threshold
node cli.js --help          # Show help
node cli.js --version       # Show version
```

**Development:**
```bash
npm test                    # No tests currently implemented
```

## Architecture

The codebase consists of:

- `cli.js`: Command-line interface entry point that handles arguments and invokes the analyzer
- `index.js`: Core analysis logic that:
  - Reads JSONL session files from `~/.claude/projects/*/*.jsonl`
  - Parses messages and tracks timestamps, models, and session IDs
  - Calculates three different time metrics using configurable gap thresholds
  - Generates weekly breakdowns and model usage statistics
  - Compares usage against Anthropic's estimated limits for Opus 4 and Sonnet 4

Key concepts:
- **Sessions**: Identified by sessionId, contain messages with timestamps
- **Segments**: Continuous conversation periods within a session (separated by gap threshold)
- **Gap threshold**: Configurable time (default 5 minutes) that defines when a new conversation segment begins
- **Parallel factor**: Ratio of parallel session total to active conversation time

The tool processes all available session data and provides comprehensive usage analytics including weekly breakdowns, model-specific usage, and comparison to Anthropic's usage limits.