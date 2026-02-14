# Changelog for version 0.2.60

# Claude Code v0.2.60 Changelog


### Git Worktree Tips
- **New contextual tip system**: Claude Code now provides helpful tips based on your usage patterns. The first tip encourages users to leverage git worktrees for running multiple Claude sessions in parallel.
  - The tip appears after 50+ startups when you have only 1 or 0 git worktrees configured
  - Tips have a cooldown period (30 sessions for the git worktree tip) to avoid being repetitive
  - Example: You'll see "※ Tip: Use git worktrees to run multiple Claude sessions in parallel. [Learn more]" with a link to documentation


### Enhanced Telemetry
- Added startup telemetry that tracks:
  - Whether you're in a git repository
  - Number of git worktrees configured
  - Memory usage patterns


### Non-Interactive Mode (-p/--print)
- **Improved transcript output**: When using `claude -p` for non-interactive mode, the transcript now filters out progress messages, providing cleaner output
- The JSON output structure remains unchanged but benefits from the cleaner transcript


### Configuration Storage
- Added new configuration fields:
  - `tipsHistory`: Tracks which tips have been shown and when
  - `memoryUsageCount`: Tracks memory feature usage


### Conversation Compaction
- Improved conversation compaction with better context handling:
  - Now properly clears file timestamps after compaction
  - Better integration with the conversation context system


### Import Optimizations
- Switched from default imports to named imports for better tree-shaking:
  - `import { PassThrough as V39 } from "stream"` instead of `import og4 from "stream"`
  - `import { cwd as gH0 } from "node:process"` instead of `import Zr2 from "node:process"`


### Code Organization
- Refactored the main entry point to separate concerns:
  - Input handling logic extracted to `ra5()` function
  - Main application logic moved to `aa5()` function
  - Better separation between interactive and non-interactive modes

## Bug Fixes

- Fixed issues with non-interactive mode (-p) that were mentioned as resolved in v0.2.59
- Improved error handling in the startup sequence


### Running Claude in non-interactive mode with cleaner output:
```bash
# Get a clean response without progress indicators
claude -p "Explain this code" < myfile.js

# Get structured JSON output
claude -p --json "Summarize this file" < README.md
```


### The git worktree tip will appear automatically when relevant:
```
$ claude
※ Tip: Use git worktrees to run multiple Claude sessions in parallel. Learn more
> 
```

This tip helps users discover that they can use git worktrees to run multiple Claude sessions simultaneously in different directories, which is particularly useful for large refactoring tasks or when working on multiple features.
