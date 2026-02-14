# Changelog for version 2.1.19


## Summary

This release introduces settings sync for Pro users using remote mode, renames the KillShell tool to TaskStop with broader task support, adds new keybinding commands for git workflows, and includes improved agent tool permission prompts. The ToolSearch tool documentation has been significantly enhanced, and the thinking indicator display has been simplified.


### Settings Sync for Remote Sessions

What: Pro users on remote sessions can now sync their Claude Code settings (CLAUDE.md, settings.json) from the cloud.

Details:
- Syncs user settings (`~/.claude/settings.json`), user memory (`~/.claude/CLAUDE.md`), project settings, and project memory
- Automatically downloads settings at session start when using remote mode
- Includes size limit protection (512KB max per file) to prevent syncing oversized configurations
- Settings are fetched from `/api/claude_code/user_settings` endpoint

Evidence: `yMK()` at line 533174 (settings sync download, contains `"Settings sync: Download starting"`)


### Git Workflow Keybindings

What: New keyboard shortcuts for common git operations, bindable in the Chat context.

Usage: Add to `keybindings.json`:
```json
{
  "context": "Chat",
  "bindings": {
    "ctrl+k ctrl+c": "command:commit",
    "ctrl+k ctrl+d": "command:diff",
    "ctrl+k ctrl+r": "command:rebase-push"
  }
}
```

Details:
- `command:commit` - Trigger the /commit command
- `command:diff` - Trigger the /diff command  
- `command:rebase-push` - Trigger the /rebase-push command
- Commands are executed from keybindings without needing to type in the input

Evidence: `VHK` at line 483273 (keybinding definitions, contains `"command:commit"`)


### Plugin Keybindings

What: New keybinding actions for managing plugins from the plugin browser.

Usage: While in the plugin browser:
- `space` - Toggle plugin on/off (`plugin:toggle`)
- `i` - Install selected plugin (`plugin:install`)

Evidence: Line 178083 (bindings: `{ space: "plugin:toggle", i: "plugin:install" }`)


### Tool Use Summaries

What: The agent can now generate brief summaries of tool execution batches for better context awareness.

Details:
- Uses a lightweight model to summarize what tools accomplished
- Summaries are under 8 words, using past tense (e.g., "Searched codebase for authentication code")
- Creates a new `tool_use_summary` message type in the conversation
- Helps maintain context without re-reading full tool outputs

Evidence: `qe7()` at line 421001 (tool use summary generator, contains `"Provide a brief summary of what was accomplished"`)


### TaskStop Replaces KillShell

The `KillShell` tool has been renamed to `TaskStop` with expanded capabilities:

- Now supports stopping any background task type, not just bash shells
- `shell_id` parameter is deprecated in favor of `task_id`
- `KillShell` remains as an alias for backwards compatibility
- Returns additional `task_type` field in the response

Evidence: `Kj1` at line 416670 (`"TaskStop"` with `aliases: ["KillShell"]`)


### Agent Tool Permission UI

What: New dedicated UI for when agents request tool permissions.

Details:
- Shows a clear "Agent tool permissions" dialog
- Displays the requesting tools and their purpose
- New "Allow for session" option grants permission for the entire session
- Options: Allow (once), Allow for session, Deny

Evidence: `QVK()` at line 543289 (contains `"Agent requests tool permissions"`, `"Allow for session"`)


### Improved ToolSearch Documentation

What: Enhanced ToolSearch tool documentation with clearer usage patterns.

Details:
- Clarifies that keyword search loads tools immediately (no need for follow-up `select:` calls)
- Adds new `+keyword` syntax for required matches (e.g., `+slack send` only returns slack tools)
- Includes anti-patterns showing what NOT to do
- Better explains that both query modes (keyword and select) load tools equally

Evidence: `V47` at line 268991 (contains `"keyword search already loaded"`, `"Required keyword"`)


### Improved HTTPS Clone Error Messages

What: Better error guidance when git clone fails with HTTPS authentication.

Details:
- Removed automatic token injection logic (previously tried injecting GitHub/GitLab/Bitbucket tokens)
- Now provides clearer message: "Please ensure your credential helper is configured (e.g., gh auth login)"
- Simplifies troubleshooting by pointing users to standard git authentication setup

Evidence: `eM9()` at line 211687 (contains `"gh auth login"`)


### Simplified Thinking Indicator

What: The thinking indicator no longer shows a character count.

Details:
- Changed from `"∴ Thinking (N)"` to simply `"∴ Thinking"`
- Cleaner visual presentation during extended thinking

Evidence: Line 384362 (`"∴ Thinking"` without parenthetical count)


### Global Prompt Cache Scope Support

What: Added support for global-scoped prompt caching.

Details:
- Prompt cache can now specify `scope: "global"` for cross-session caching
- Part of the ephemeral cache control structure
- Works with the existing 1-hour TTL experiment

Evidence: `iMA()` at line 525119 (cache control with `scope: A` when `A === "global"`)


### Streaming Fallback on Empty Responses

What: Better handling of edge cases where API streaming fails to start.

Details:
- Detects when stream completes without receiving `message_start` event
- Automatically triggers non-streaming fallback
- Prevents hanging on incomplete stream connections

Evidence: Line 525690 (`"Stream completed without receiving message_start event - triggering non-streaming fallback"`)


### Plugin UI Shows Description Token Count

What: Plugin browser now displays the token count for plugin descriptions.

Evidence: Line 505857 (displays `"description tokens"`)


### Model Selector Default Label Change

What: The default model option label changed from "Sonnet (default)" to "Inherit (default)".

Details:
- Better reflects that subagents inherit the parent model by default
- More accurate terminology for model selection in agent configuration

Evidence: Line 158543 (`"Inherit (default)"`)

## Bug Fixes

- Fixed session memory and transcript access telemetry tracking (`ti2()` at line 566939, tracks `"tengu_session_memory_accessed"`)
- Improved keybinding context validation with clearer error messages for bindings in wrong contexts (contains `"must be in \"Chat\" context"`)

## Internal

- Deprecated `claude-code-plugins` marketplace in favor of `claude-plugins-official` with migration message
- Added telemetry for settings sync operations (download success/failure/empty states)
- Removed legacy async worker initialization code that checked for Node 10-11
- Keybindings schema URL updated to `platform.claude.com/docs/schemas/claude-code/keybindings.json`
- Keybindings documentation URL updated to `code.claude.com/docs/en/keybindings`
