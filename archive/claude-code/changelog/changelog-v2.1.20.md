# Changelog for version 2.1.20


## Summary

Version 2.1.20 introduces a comprehensive keybindings customization system via a new `/keybindings` skill, adds several new CLI debugging flags (`--debug-file`, `--hard-fail`, `--who-owns`), significantly enhances sandbox security with Unix socket ownership verification, and refactors the teammate messaging system with a new `SendMessageTool`. The release also removes the git attribution system and improves UI notifications throughout.


### Keybindings Customization Skill

What: New `/keybindings` skill enables full customization of keyboard shortcuts via `~/.claude/keybindings.json` configuration file.

Usage:
```bash
/keybindings
```

Details:
- Create custom keybindings organized by context (Global, Chat, Autocomplete, etc.)
- Support for chord bindings (multi-keystroke shortcuts like `ctrl+k ctrl+s`)
- Validation integrated into `/doctor` command with detailed error/warning messages
- Unbind default shortcuts by setting them to `null`
- Schema validation with JSON Schema support for editor autocomplete
- Documentation at https://code.claude.com/docs/en/keybindings

Evidence: Skill registration at line 748555 (`name: "keybindings-help"`, contains `"Use when the user wants to customize keyboard shortcuts"`)


### Debug Logging to File

What: New `--debug-file` CLI flag writes debug logs to a specific file path.

Usage:
```bash
claude --debug-file /path/to/debug.log
claude --debug-file=/path/to/debug.log
```

Details:
- Implicitly enables debug mode when specified
- Useful for persistent debugging and troubleshooting

Evidence: Argument parser at line 2836 (`if (K.startsWith("--debug-file="))`) and help text at line 577087 (`"--debug-file <path>"`)


### Hard Fail Mode

What: New `--hard-fail` CLI flag causes Claude Code to exit immediately on certain errors rather than attempting recovery.

Usage:
```bash
claude --hard-fail
```

Details:
- Useful for CI/CD pipelines and automated testing
- Ensures failures are detected rather than silently handled

Evidence: Detection at line 5582 (`return process.argv.includes("--hard-fail")`)


### Package Manager Ownership Detection

What: New `--who-owns` integration for Alpine Linux (apk) package manager to verify file ownership.

Usage:
Internal feature - automatically used when verifying Claude Code installation on Alpine Linux.

Details:
- Detects apk-managed installations with logging: "Detected apk installation: ..."
- Also detects deb, rpm, and pacman installations
- Enables better package manager integration and update guidance

Evidence: APK query at line 419998 (`OP1("apk", ["info", "--who-owns", K]`) and detection logs at lines 420004, 420011, 420018, 420025


### SendMessageTool for Teammate Communication

What: New `SendMessageTool` replaces previous teammate messaging implementation with clearer protocol separation.

Usage:
Internal tool used by agents in swarm mode.

Details:
- Handles message, broadcast, request, and response types
- Protocol subtypes for shutdown and plan approval workflows
- Better error messages for missing parameters
- Improved in-process teammate abort handling

Evidence: Tool definition at line 448126 (`SendMessageTool: () => tT2`) with logging prefix `[SendMessageTool]` at lines 448249, 448275, 448284


### Compact Conversation Keybinding

What: New `ctrl+k ctrl+k` chord keybinding to trigger `/compact` command.

Usage:
```
ctrl+k ctrl+k
```

Details:
- Quick access to conversation compaction
- Uses the new chord keybinding system
- Replaces removed `ctrl+k ctrl+c` for `/commit`

Evidence: Keybinding definition at line 486662 (`"ctrl+k ctrl+k": "command:compact"`)


### "Newspapering" Feature

What: New feature or mode referenced in codebase (details unclear from minified code).

Usage:
Internal implementation detail.

Evidence: String literal at line 388067 (`"Newspapering"`)


### Enhanced Sandbox Security

What: Significantly improved Unix domain socket security with ownership verification and stale socket cleanup.

Details:
- Socket directory ownership check: warns if directory owned by different user
- Stale socket cleanup: removes sockets for non-running PIDs
- Better seccomp filter path discovery for global `@anthropic-ai/sandbox-runtime` installations
- Added `.npm-global` to seccomp binary search paths
- Improved error messages with actionable installation instructions
- Warning when seccomp binaries unavailable: "[Sandbox Linux] Seccomp binaries not available - unix socket blocking disabled. Install @anthropic-ai/sandbox-runtime globally for full protection."

Evidence: Socket ownership check at line 523583 (`"Socket directory not owned by current user"`), stale socket cleanup messages, seccomp search paths at line 95936 (`".npm-global"`), warning at line 96398


### Browser MCP Accessibility Tree Improvements

What: MCP browser tool's accessibility tree output limit is now configurable.

Details:
- Default limit remains 50,000 characters
- New parameter allows setting custom limits for clients that can handle larger outputs
- More flexible description: "Output is limited to 50000 characters by default" (was: "Output is limited to 50000 characters")
- New parameter: "Maximum characters for output (default: 50000). Set to a higher value if your client can handle large outputs."

Evidence: Description change at line 522359 and parameter at line 522387


### Updated Conversation Compaction Notification

What: Compaction notification now shows "✻ Conversation compacted" with visual symbol instead of plain text.

Details:
- Old: `Conversation compacted · {keybinding} for history`
- New: `✻ Conversation compacted ({keybinding} for history)`
- More visually distinct in transcript

Evidence: Notification text at line 410281 (`"✻ Conversation compacted ("`)


### Improved Permission Dialog Text

What: Refined safety check messaging for workspace trust.

Details:
- Slightly more concise wording in safety prompt
- Old: "Quick safety check: ... If not, take a moment to review what's in this folder first."
- New: "Quick safety check: ... If not, take a moment to review what"
- Message continues with context about Claude Code's file access capabilities

Evidence: Safety message at line 570322


### Guest Pass Notification Enhancement

What: Clearer guest pass sharing notification in UI.

Details:
- More prominent formatting: "You have free guest passes to share · /passes"
- Encourages user engagement with referral system

Evidence: Notification at line 562731


### Enhanced Task and Agent Status Logging

What: More detailed logging for task claiming and agent operations.

Details:
- New logs: `[inProcessRunner] Claimed task #N: {subject}`
- Task failure logging: `[inProcessRunner] Failed to claim task #N`
- Task list check errors: `[inProcessRunner] Error checking task list:`
- New logs for task assignment and completion

Evidence: Logs at lines 422622, 522622, 522628 with prefix `[inProcessRunner]`


### Layout Engine Identification

What: Explicit layout engine logging for debugging rendering issues.

Details:
- Logs: "Layout engine: yoga" and "[render] initLayout starting/complete"
- Helps diagnose UI rendering problems

Evidence: Engine log at line 174577, render logs at lines 182436-182438


### Message Structure Repair

What: Automatic repair of malformed tool result pairings in conversation history.

Details:
- Detects and repairs missing `tool_result` blocks
- Logs: `ensureToolResultPairing: repaired missing tool_result blocks (X -> Y messages)`
- Prevents conversation corruption from improperly paired tool uses

Evidence: Repair logging at line 469512


### Team Workflow Enhancements

What: Improved teammate communication and protocol handling.

Details:
- Operation descriptions now mention "discoverTeams to list available teams to join"
- Better error messages for missing parameters in teammate operations
- Clearer separation between message types (message, broadcast, request, response)

Evidence: Operation description updates in SendMessageTool schema, error messages for missing `recipient`, `request_id`, etc.


### Git Attribution System

What: Removed automatic git commit trailer attribution system.

Details:
- Removed all "Attribution hook:" logging
- Removed `Claude-Generated-By:` git trailers
- Removed `Claude-Escapes:`, `Claude-Permission-Prompts:`, `Claude-Session:`, `Claude-Steers:` trailers
- No longer tracks file contributions or calculates Claude percentage
- Simplifies git workflow and removes potentially confusing commit metadata

Evidence: All `Attribution:` and `Attribution hook:` log strings removed from codebase (verified absent in v2.1.20)


### Removed `/commit` Keybinding

What: Removed `ctrl+k ctrl+k` keybinding for `/commit` command.

Details:
- Previous binding: `ctrl+k ctrl+c` → `/commit`
- Now unbound by default
- Users can re-add via custom keybindings if desired

Evidence: Binding `"ctrl+k ctrl+c": "command:commit"` existed in v2.1.19 line 483280, not present in v2.1.20


### Removed Permission UI Elements

What: Simplified permission request UI removed some verbose text and interactive elements.

Details:
- Removed: "Do you trust the files in this folder?"
- Removed: "(shift+↑/↓ to select)" navigation hints
- Removed: Several verbose permission dialog messages
- Streamlined to clearer, more concise safety checks

Evidence: Strings like "Do you trust the files in this folder?", "shift+↑/↓ to select" removed from v2.1.20


### PR Status Footer [Gradual Rollout]

What: GitHub pull request status displayed in footer area.

Status: Feature-flagged behind `tengu_pr_status_cli`

Details:
- Settings option: "Show PR status footer" (enabled by default when flag is on)
- Infrastructure exists in settings menu at line 480230
- Will display PR status information in CLI footer when enabled

Evidence: Feature flag check at line 480226 (`i4("tengu_pr_status_cli", !1)`) with settings UI at line 480230 (`label: "Show PR status footer"`)
