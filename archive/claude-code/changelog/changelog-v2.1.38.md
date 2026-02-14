# Changelog for version 2.1.38


## Summary

This release introduces session effort levels (low/medium/high) for controlling Claude's response intensity, auto-memory as a research preview for persistent learning across sessions, and browser switching for multi-Chrome automation setups. The update also adds file snapshot persistence for plan recovery, conditional skills that activate based on file patterns, improved elicitation with natural language date/time parsing, and new security checks for command validation.


### Effort Level Control

What: Control how much effort Claude puts into responses during a session.

Usage:
```bash
claude --effort medium
claude --effort high
```

Details:
- Valid levels: `low`, `medium`, `high`
- The `max` level exists but is restricted:
  - Not available in interactive mode
  - Not available for Claude.ai subscribers
- Use `high` for complex analysis, `low` for quick tasks

Evidence: CLI flag definition (search for `"--effort <level>"`)


### Auto-Memory (Research Preview)

What: Claude can now automatically learn and remember patterns across sessions, writing insights to a persistent memory directory.

**Activation**: Auto-memory has a three-layer activation cascade (checked in order):
1. **Environment variable** (highest priority): `CLAUDE_CODE_DISABLE_AUTO_MEMORY=true` forces off, `=false` forces on
2. **User setting**: `autoMemoryEnabled` in `~/.claude/settings.json` (per-project, overrides the feature flag)
3. **GrowthBook feature flag** `tengu_oboe` (default fallback): server-side rollout control, defaults to `false`

If the flag is off for your account and you haven't set the user setting, auto-memory is disabled by default. Remote sessions (`CLAUDE_CODE_REMOTE=true`) also disable it unless `CLAUDE_CODE_REMOTE_MEMORY_DIR` is set.

**How to enable**: The toggle is in the `/memory` panel (not `/settings`). Type `/memory` to see "Auto-memory (research preview): off" at the top, then confirm to toggle it on. This writes `autoMemoryEnabled: true` to settings, overriding the feature flag. After enabling, "Open auto-memory folder" and per-agent memory entries also appear in the `/memory` panel.

**Note**: The feature flag `tengu_oboe` existed in v2.1.37 but with no user-facing toggle — auto-memory was purely server-gated. v2.1.38 added the `autoMemoryEnabled` setting, the `/memory` panel toggle, and the bidirectional env var override, making it opt-in for everyone.

Details:
- Per-project setting: `autoMemoryEnabled` controls whether Claude reads/writes to auto-memory
- Memory guidance updated from "write down key learnings as you complete tasks" to "save patterns worth preserving across sessions"
- New guidelines for what to save:
  - Stable patterns and conventions confirmed across multiple interactions
  - User preferences for workflow, tools, and communication style
  - Key architectural decisions and important file paths
  - Solutions to recurring problems and debugging insights
- What NOT to save:
  - Session-specific context (current task details, in-progress work)
  - Speculative conclusions from reading a single file
  - Information that duplicates CLAUDE.md instructions
- Supports explicit user requests: "always use bun", "never auto-commit", or "forget X"

Evidence: Activation logic (search for `tengu_oboe`), settings schema (search for `"Enable auto-memory for this project"`), `/memory` panel toggle (search for `"Auto-memory (research preview):"`)


### Browser Switching for Chrome Automation

What: Switch between multiple Chrome browsers when using Claude's browser automation features.

Usage: Invoke the `switch_browser` tool when you want to connect to a different Chrome instance.

Details:
- Broadcasts a connection request to all Chrome browsers with the Claude extension installed
- User clicks 'Connect' in the desired browser to switch
- Only available with bridge connections (shows error otherwise)
- Useful for multi-browser development/testing workflows

Evidence: Tool definition (search for `"Switch which Chrome browser is used for browser automation"`)


### Conditional Skills

What: Skills can now activate automatically when you work with files matching specific patterns.

Details:
- Skills are stored with file pattern matchers
- When a matching file is touched, the skill activates automatically
- Log message shows: `[skills] Activated conditional skill '<name>' (matched path: <path>)`
- Tracked via telemetry for optimization

Evidence: Skill activation system (search for `"Activated conditional skill"`)


### File Snapshot Persistence for Plan Recovery

What: Plan mode now persists file snapshots to the conversation transcript, enabling recovery if files are deleted.

Details:
- File snapshots are stored as system messages with subtype `file_snapshot`
- Recovery sequence when resuming a conversation:
  1. Try to read plan file from disk
  2. If missing, recover from file snapshot in message history
  3. If no snapshot, attempt recovery from serialized plan content
- Log messages indicate recovery source: "Plan recovered from file snapshot"
- Protects against accidental file deletion during long planning sessions

Evidence: Recovery system (search for `"Plan recovered from file snapshot"`)


### Worktree Symlink Configuration

What: Configure directories to symlink when using git worktrees, preventing disk bloat from duplicated dependencies.

Usage: Add to your settings:
```json
{
  "worktree": {
    "symlinkDirectories": ["node_modules", ".cache", ".bin"]
  }
}
```

Details:
- No directories are symlinked by default — must be explicitly configured
- Common candidates: `node_modules`, `.cache`, `.bin`
- Prevents duplicating large directories across worktrees
- Part of the `--worktree` flag configuration

Evidence: Settings schema (search for `"Directories to symlink from main repository"`)


### Enhanced Elicitation with Natural Language Date/Time Parsing

What: MCP elicitation now supports natural language date/time input with intelligent parsing.

Details:
- Accepts natural language: "tomorrow", "next Monday", "jan 1st 2025", "in 2 hours"
- Converts to ISO 8601 format automatically
- Prefers future dates over past dates when ambiguous
- For dates without times, omits the time component
- Supports multiple formats: `uri`, `email`, `date`, `date-time`
- Shows current context (date, time, timezone, day of week) to help parsing
- Includes `minItems`/`maxItems` validation for selection elicitations
- Gracefully handles invalid input with clear error messages

Evidence: Date parser prompt (search for `"You are a date/time parser"`)


### Auto-Compact Notification

Claude now displays a helpful message when auto-compact is enabled: "Auto-compact is enabled. When the context window is nearly full, older messages will be automatically summarized so you can continue working seamlessly. There is no need to stop or rush — you have unlimited context through automatic compaction."

Evidence: Notification message (search for `"Auto-compact is enabled"`)


### Memory Search Improvements

Added structured guidance for searching past context:
1. Search topic files in memory directory first (fast)
2. Session transcript logs as last resort (large files, slow)
- New tip: "Use narrow search terms (error messages, file paths, function names) rather than broad keywords"

Evidence: Memory search section (search for `"Searching past context"`)


### Thinking Mode Deprecation Warning

When using `thinking.type=enabled`, Claude now warns that this is deprecated and recommends `thinking.type=adaptive` for better performance, with a link to documentation.

Evidence: Deprecation warning (search for `"thinking.type=enabled' is deprecated"`)


### WebSocket Reconnection Improvements

Changed reconnection handling from a fixed retry count to a time budget approach, providing more predictable behavior during network instability.

Evidence: Transport logging (search for `"Reconnection time budget exhausted"`)


### Output Format Deprecation

The `output_format` parameter is now deprecated in favor of `output_config.format`. Using both together produces a warning.

Evidence: Deprecation check (search for `"output_format is deprecated"`)


### Opus 4.6 Extended Context Messaging

Clear error message when trying to use Opus 4.6 with 1M extended context on unsupported plans, with link to documentation.

Evidence: Error message (search for `"Opus 4.6 with extended context (1M) is not available"`)


### MCP Bash Tool Enhancement

New `noOutputExpected` boolean field in command schemas indicates when a command is expected to produce no output on success, improving semantic interpretation of exit codes.

Evidence: Schema definition (search for `"Whether the command is expected to produce no output"`)


### Credential Refresh Improvements

Improved handling of token refresh failures with `invalid_grant` errors, including automatic credential invalidation and token clearing for smoother re-authentication.

Evidence: Token handling (search for `"Token refresh failed with invalid_grant"`)

## Bug Fixes

- Fixed handling of orphaned permissions when `updatedInput` is undefined, now falls back to original tool input (search for `"Orphaned permission for"`)
- Added security check for commands containing single-quoted backslash patterns that could bypass security checks (search for `"single-quoted backslash pattern"`)
- Improved sync agent error recovery with automatic retry mechanism (search for `"Sync agent recovering from error"`)
- Fixed compaction error handling when response is not text as expected (search for `"Expected text response for compaction"`)
- Added validation for elicitation responses with proper "This field is required" messaging

## Internal

- Updated Azure Identity SDK integration with additional credential types (AzurePipelinesCredential, VisualStudioCodeCredential, etc.)
- Added bridge staging URL for development/testing environments
- Improved Symbol.dispose/Symbol.asyncDispose handling for resource cleanup
- Enhanced session title update logging with success/failure tracking
