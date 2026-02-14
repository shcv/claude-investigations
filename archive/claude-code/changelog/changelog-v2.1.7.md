# Changelog for version 2.1.7


## Summary

This release introduces significant speculation execution infrastructure for predictive tool running, adds a new `/color` command for session-customizable prompt bar colors, implements Opus 4.5 migration handling for Pro users, and improves compaction reliability with streaming retry logic. Enhanced telemetry and crash handling have also been added.


### `/color` Command
What: Set a custom color for the prompt bar during your current session.

Usage:
```bash
/color cyan
```

Details:
- Available colors are configurable per session
- Color is persisted in the session file and can be used to visually distinguish multiple concurrent Claude Code sessions
- Sets the `standaloneAgentContext.color` property

Evidence: `VQ9` at line 466161 (color command handler, contains `"Set the prompt bar color for this session"`)


### Speculative Execution Infrastructure
What: Claude Code can now speculatively execute tool calls while waiting for user input, using isolated git clones to avoid affecting your working directory.

Details:
- Creates temporary `speculation-clones/speculation-{id}` directories for isolated execution
- Uses `git clone --shared --no-checkout` for fast, lightweight cloning
- Tracks time saved and tools executed via `tengu_speculation` telemetry
- Changes from accepted speculations are copied back to the main worktree
- Read operations outside git root are allowed; writes outside git root are blocked
- Speculation aborts cleanly on user input or errors
- Displays time saved indicator (e.g., `▶▶ 5s`) when speculation completes

Evidence: `g19()` at line 460815 (speculation entry point, contains `"speculation-clones"`)


### Opus 4.5 Pro Migration Notification
What: Pro users who hadn't set a model preference are automatically migrated to Opus 4.5, with a notification displayed.

Details:
- Only triggers for first-party auth users
- Shows "Model updated to Opus 4.5" notification on next session start
- Migration only occurs once, tracked via `opusProMigrationComplete` state

Evidence: `ww9()` at line 539875 (migration logic), `Xq9()` at line 533528 (notification display, contains `"Model updated to Opus 4.5"`)


### Chrome Browser Skill
What: Added a new `claude-in-chrome` skill that enables browser automation tools via the Skill tool.

Details:
- Provides comprehensive guidance for browser automation including GIF recording, console log debugging, and dialog handling
- Controlled by `tengu_chrome_auto_enable` feature flag
- Must invoke skill before using `mcp__claude-in-chrome__*` tools
- Includes instructions for tab context management and session startup

Evidence: `TI9()` at line 516042 (skill registration, contains `"claude-in-chrome"`)


### Compaction Streaming Retry
What: Compaction now includes retry logic when streaming responses fail.

Details:
- Controlled by `tengu_compact_streaming_retry` feature flag
- Retries up to 3 times with exponential backoff
- Improved error message: "Compaction interrupted · This may be due to network issues — please try again."
- Logs retry attempts and final failure for diagnostics

Evidence: `H97()` at line 449946 (compaction handler, contains `"tengu_compact_streaming_retry"`)


### Enhanced Crash and Signal Telemetry
What: Better crash and shutdown diagnostics through telemetry.

Details:
- Now logs `shutdown_signal` events for SIGINT/SIGTERM
- Captures `uncaught_exception` with error name and truncated message
- Captures `unhandled_rejection` for promise rejections
- All error messages are truncated to 2000 characters

Evidence: `yJ` at line 317867 (signal handlers, contains `"shutdown_signal"`, `"uncaught_exception"`)


### Keybindings File Format Update
What: Keybindings configuration now includes JSON schema and documentation references.

Details:
- New `$schema` field pointing to `https://code.claude.com/docs/schemas/keybindings.json`
- New `$docs` field linking to `https://code.claude.com/docs/s/claude-code-keybindings`
- Reserved (non-rebindable) keys are now filtered from generated config

Evidence: `R29()` at line 473546 (keybindings generator, contains `"$schema"`)


### Dynamic Tool Loading Diagnostics
What: Logs discovered tools found in message history when resuming sessions.

Details:
- Scans tool_result blocks in user messages for tool names
- Logs count of discovered tools for debugging dynamic tool loading behavior

Evidence: `_Z0()` at line 279909 (tool discovery, contains `"Dynamic tool loading"`)


### Plugin Forced Output Style
What: Plugins can now force a specific output style for the session.

Details:
- Plugins can set `forceForPlugin: true` on their output style
- If multiple plugins force styles, a warning is logged and the first is used
- Takes precedence over user-configured output style

Evidence: `sY9()` at line 508208 (output style selection, contains `"forceForPlugin"`)


### Orphaned Thinking Block Filtering
What: Filters out orphaned assistant thinking blocks that don't have associated content.

Details:
- Removes assistant messages that contain only thinking/redacted_thinking blocks
- Logs filtered messages via `tengu_filtered_orphaned_thinking_message` telemetry
- Prevents display issues from incomplete responses

Evidence: `Su2()` at line 510058 (filtering logic, contains `"tengu_filtered_orphaned_thinking"`)


### Prefetch System Context Optimization
What: System context is now prefetched more intelligently based on trust status.

Details:
- In non-interactive sessions, prefetch runs immediately
- In interactive sessions, only prefetches if trust has been established
- Logs prefetch status via `prefetch_system_context_*` telemetry events

Evidence: `tR7()` at line 543352 (prefetch logic, contains `"prefetch_system_context"`)


### Git Conflict Detection for Snapshots
What: Worktree snapshotting now detects in-progress git operations and provides clearer errors.

Details:
- Detects cherry-pick, rebase, merge, revert, am, and bisect operations
- Throws descriptive error: "Cannot snapshot worktree: in-progress {operation} operation detected"
- Also detects uninitialized repositories and prompts for initial commit

Evidence: `a77()` at line 458650 (conflict detection, contains `"cherry-picking"`, `"rebasing"`)


### Enhanced Symlink Resolution
What: File path resolution now follows symlink chains more thoroughly.

Details:
- Follows up to 40 levels of symlinks (protection against infinite loops)
- Skips special file types (FIFO, socket, character/block devices)
- Returns all paths in the symlink chain for better tracking

Evidence: `pAA()` at line 2374 (symlink resolution, contains `"isSymbolicLink"`)

## Bug Fixes

- Fixed `"File has been unexpectedly modified"` error message to be more actionable (`ZRA` at line 170468)
- Improved request size error messaging for non-interactive mode (`hs8()` at line 278885, contains `"Request too large"`)


### Enhanced Telemetry Beta
Status: Feature-flagged

What: Optional enhanced telemetry collection for debugging and analytics.

Details:
- Controlled by `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA` or `ENABLE_ENHANCED_TELEMETRY_BETA` env var
- Also gated by `enhanced_telemetry_beta` feature flag (defaults to false)

Evidence: `uI0` at line 303463 (feature definition, contains `"enhanced_telemetry_beta"`)
