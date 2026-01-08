# Changelog for version 1.0.41

# Claude Code v1.0.41 Changelog

### Enhanced Hook System with Per-Command Timeouts
The hook execution system now supports individual timeout configurations for each command within a hook. Previously, all commands shared a single global timeout, but now each command can specify its own timeout value.

**Usage Example:**
When configuring hooks, you can now specify a timeout for individual commands:
```json
{
  "hook_event_name": "pre-commit",
  "commands": [
    {
      "command": "npm test",
      "timeout": 30  // 30 seconds timeout
    },
    {
      "command": "npm run lint",
      "timeout": 10  // 10 seconds timeout
    }
  ]
}
```

### New SubagentStop Hook Event
A new hook event type `SubagentStop` has been added to the available hook events. This allows you to configure commands that run when a subagent completes its execution.

**Available hook events now include:**
- `PreToolUse` - Before a tool is executed
- `PostToolUse` - After a tool completes
- `Notification` - For notification events
- `Stop` - When the main process stops
- `SubagentStop` - When a subagent completes (NEW)

### Hook Input Structure Update
The hook system now passes the complete hook configuration object to commands instead of just the `userFacingInput` field. This provides hooks with more context about the event that triggered them.

**Before:** Hooks received only `userFacingInput` as JSON
**After:** Hooks receive the entire hook configuration object including `hook_event_name` and other metadata

### Import Optimizations
- Consolidated stream imports to use named imports from `node:stream` and `stream` modules
- Optimized process imports to use named import `{ cwd }` from `node:process`
- Added `PassThrough` stream imports for improved stream handling

### Better Error Handling
- Individual command timeouts are now properly cleared on both success and failure
- Improved cleanup of abort controllers to prevent memory leaks
- More consistent error reporting across hook executions

### Code Structure
- Simplified the global timeout logic by moving timeout handling to individual command execution
- Removed redundant timeout abort message since timeouts are now handled per-command
- Cleaner separation of concerns between hook orchestration and command execution
