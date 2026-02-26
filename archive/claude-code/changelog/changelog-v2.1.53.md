# Changelog for version 2.1.53


## Summary

This release focuses on security hardening for bash command execution (new Unicode whitespace and mid-word hash injection checks, UNC path blocking), improves the Remote Control experience with a QR code viewer and minimum version enforcement, and significantly restructures the system prompt and Bash tool description for clearer, modular guidance. Background task progress polling has been removed in favor of completion notifications.

### Bash Command Security Checks: Unicode Whitespace and Mid-Word Hash

What: Two new security checks detect potentially dangerous command patterns before execution.

Details:
- **Unicode whitespace detection**: Commands containing exotic Unicode whitespace characters (such as non-breaking spaces `\u00A0`, em spaces `\u2000-\u200A`, and others) are now flagged, as these can cause parsing inconsistencies between `shell-quote` and bash
- **Mid-word hash detection**: Commands containing `#` characters mid-word (e.g., not preceded by whitespace) are flagged because `shell-quote` and bash parse these differently — bash treats `#` as a comment start in some contexts while `shell-quote` does not
- Both checks trigger a user confirmation prompt ("ask" behavior) rather than blocking outright

Evidence: New security check IDs `UNICODE_WHITESPACE` and `MID_WORD_HASH` (search for `"UNICODE_WHITESPACE"` and `"MID_WORD_HASH"`)


### UNC Network Path Blocking

What: Windows UNC network paths (e.g., `\\server\share`) are now explicitly blocked in the sandbox path resolver, requiring manual user approval.

Details:
- Previously, UNC paths could potentially bypass sandbox restrictions
- Now returns a denial with the message "UNC network paths require manual approval"

Evidence: UNC path check in sandbox path resolution (search for `"UNC network paths require manual approval"`)


### Remote Control QR Code Viewer

What: The Remote Control disconnect dialog now includes an option to show/hide a QR code linking to the session URL.

Details:
- When a session is connected via Remote Control, the dialog shows three options: "Disconnect this session", "Show QR code" / "Hide QR code", and "Continue"
- The QR code is generated from the session URL, making it easy to share access from a terminal to a mobile device or another screen

Evidence: Bridge disconnect dialog component (search for `"Show QR code"` and `"Hide QR code"`)


### Remote Control Minimum Version Enforcement

What: The bridge (Remote Control) system now checks a server-specified minimum version requirement and blocks connections from outdated CLI versions.

Details:
- On startup, the bridge checks the `tengu_bridge_min_version` feature flag for a required minimum version
- If the running CLI version is too old, the user sees: "Your version of Claude Code (X.X.X) is too old for Remote Control. Version Y.Y.Y or higher is required. Run `claude update` to update."
- This applies to both standalone `claude bridge` mode and in-session REPL bridge connections

Evidence: Version check using `tengu_bridge_min_version` flag (search for `"tengu_bridge_min_version"`)


### `claude remote-control` CLI Command with `rc` Alias

What: A formal `claude remote-control` (aliased as `claude rc`) subcommand is now registered in the CLI's Commander.js command tree.

Details:
- Previously, the remote-control bridge was only accessible through internal paths
- Now it appears as a proper CLI subcommand with description: "Connect your local environment for remote-control sessions via claude.ai/code"
- The command is hidden when bridge is not enabled for the user's account

Evidence: Commander registration with alias (search for `"Connect your local environment for remote-control sessions via claude.ai/code"`)

### Restructured Bash Tool Description

The Bash tool system prompt has been completely rewritten from a monolithic template literal into a modular, array-based builder. While the overall guidance is similar, it now includes:
- A dedicated "# Instructions" section with clearer organization
- Explicit "For git commands:" subsection with safer defaults guidance
- A new "Avoid unnecessary `sleep` commands:" subsection with six specific anti-sleep rules, including: don't poll background tasks, use `run_in_background` for long-running commands, don't retry in sleep loops, and keep sleep durations to 1-5 seconds
- Sandbox description restructured into a more readable format

Evidence: New modular Bash description builder function (search for `"Avoid unnecessary"` and `"Do not sleep between commands"`)


### Background Task Notification Model Overhaul

Background agents and bash tasks no longer generate periodic progress polling messages. Instead, the system now relies entirely on completion notifications.

Details:
- The `getProgressMessage` function has been removed from all task types (local agents, background bash, remote agents, and teammates)
- The `task_progress` attachment type is no longer generated or rendered
- The Task tool description now explicitly states: "you will be automatically notified when it completes — do NOT sleep, poll, or proactively check on its progress"
- `lastReportedToolCount` and `lastReportedTokenCount` tracking fields removed from task state
- `deltaSummarySinceLastFlushToAttachment` and the delta summarization LLM call have been removed entirely

Evidence: Removed progress message infrastructure (search for `"do NOT sleep, poll"`)


### Background Agent Kill Notifications

When users kill running background agents (via the kill-agents shortcut), the system now sends a descriptive notification into the conversation.

Details:
- Single agent: `Background agent "description" was killed by the user.`
- Multiple agents: `N background agents were killed by the user: "desc1", "desc2".`
- Delivered as a task-notification mode message so the model understands context was interrupted

Evidence: Kill notification messages (search for `"was killed by the user"`)


### Improved Memory Selection Prompt

The system prompt for selecting relevant memories has been rewritten to be more selective and discerning.

Details:
- Old prompt: "Return the filenames of the most relevant memories (up to 5). Only include memories that are clearly relevant to the query."
- New prompt: "Return a list of filenames for the memories that will clearly be useful to Claude Code as it processes the user's query (up to 5)... Be selective and discerning. If there are no memories in the list that would clearly be useful, feel free to return an empty list."
- The new prompt also includes the instruction to describe memories with specific one-line descriptions to aid future retrieval

Evidence: Updated memory selection system prompt (search for `"Be selective and discerning"`)


### Updated Write Tool Description

The Write tool description now explicitly recommends the Edit tool for modifications:
- Old: "ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required."
- New: "Prefer the Edit tool for modifying existing files — it only sends the diff. Only use this tool to create new files or for complete rewrites."

Evidence: Updated Write tool instructions (search for `"Prefer the Edit tool"`)


### Improved File Operation Security

File creation and log file operations now use more secure flag combinations:
- `O_EXCL` flag added for temp file creation (prevents TOCTOU race conditions)
- `O_NOFOLLOW` flag used on supported platforms (prevents symlink-following attacks)
- Log file open now uses explicit flag combinations (`O_WRONLY | O_CREAT | O_APPEND | O_NOFOLLOW`) instead of the legacy `"a"` mode string

Evidence: New file security flags (search for `"O_NOFOLLOW"`)


### Improved `detectFileEncoding` Error Handling

The file encoding detection function now handles expected filesystem errors (ENOENT, EACCES, EPERM) gracefully with a debug-level log message instead of reporting them as unexpected errors.

Evidence: Improved error classification (search for `"detectFileEncoding failed for expected reason"`)


### Remote Control Bridge Improvements

Several improvements to the Remote Control bridge infrastructure:
- **State reporting**: The bridge now reports `"processing"` and `"idle"` states to the server, enabling better status visibility on claude.ai/code
- **SSE event handling refactored**: Delivery updates and catch-up truncation events are now handled via a generic `setOnEvent` callback, with catch-up truncation elevated to a proper error log
- **Session creation/archival** now accepts explicit `baseUrl` and `getAccessToken` parameters, improving BYOC (Bring Your Own Credentials) support
- **Compaction boundary events** are now tagged with `is_compaction: true` when written to the bridge transport
- **Bridge REPL error**: The `replBridgeError` state now preserves the first error rather than overwriting it

Evidence: State reporting infrastructure (search for `"reportState"`) and SSE handling (search for `"SSE catch-up truncated"`)


### Alternate Screen Buffer Support

The terminal renderer now supports entering and exiting an alternate screen buffer via `enterAlternateScreen()` / `exitAlternateScreen()` methods, replacing inline ANSI escape sequences. Used by the year-in-review playback feature.

Evidence: New screen buffer methods (search for `"enterAlternateScreen"`)


### Improved Newline Security Check

The bash command newline injection check has been updated with a more comprehensive regex pattern that better handles line continuations (backslash-newline sequences) as legitimate, while still catching suspicious newline patterns.

Evidence: Updated newline detection regex (search for `"NEWLINES"` in the security check)


### Improved Command Parsing

A new `unquotedKeepQuoteChars` field is now returned from command parsing, providing a third representation of commands alongside `withDoubleQuotes` and `fullyUnquoted`. This variant preserves quote characters in the output, enabling more accurate security analysis of commands where quote placement matters (e.g., the new mid-word hash check).

Evidence: New parsing field (search for `"unquotedKeepQuoteChars"`)


### Environment Variable Loading from Policy/Flag Settings

Environment variables are now loaded from `userSettings`, `flagSettings`, and `policySettings` in addition to user config, giving admins more control over the runtime environment.

Evidence: Settings-based env loading (search for `"policySettings"`)


### Session Metadata Schema for `listSessions`

A new Zod schema defines the structure returned by `listSessions`, including fields for `sessionId`, `summary`, `lastModified`, `fileSize`, `customTitle`, `firstPrompt`, `gitBranch`, and `cwd`.

Evidence: Schema with `.describe("Session metadata returned by listSessions.")` (search for `"listSessions"`)


### MCP Client State Update Batching

MCP client state updates are now batched using a 16ms debounce timer, reducing React re-renders when multiple MCP servers report status changes in quick succession.

Evidence: Batching with 16ms `setTimeout` in MCP client update callback


### Bash Agent Type Removed

The dedicated "Bash" agent type (described as "Command execution specialist for running bash commands") has been removed from the built-in agent list. This simplifies the agent architecture.

Evidence: Removed bash agent definition (search for `"Command execution specialist"`)


### Pipeline Command Parsing Fix

The tree-sitter command parser now recursively processes pipeline nodes instead of treating them the same as `redirected_statement`. This improves accuracy when analyzing piped commands for security checks.

Evidence: Recursive pipeline handling in command parser


### Glob Pattern Matching: Case-Insensitive Support

The internal glob-to-regex pattern matching function now accepts an optional case-insensitive flag, enabling case-insensitive permission rule matching.

Evidence: New parameter in glob matching function


### Trust Dialog Bypass Removed

The trust dialog bypass for `bypassPermissions` mode has been removed. Previously, `bypassPermissions` mode could skip the trust dialog entirely; now the standard trust checking flow applies regardless.

Evidence: Removed `bypassPermissions` check in trust dialog gate (search for `"bypassPermissions"`)

## Bug Fixes

- Fixed Remote Control initialization to preserve the first error message rather than overwriting it with a generic "initialization failed" message (search for `"replBridgeError"`)
- Fixed file index `.gitignore` loading to use async `readFile` instead of sync `readFileSync` with `existsSync`, preventing potential blocking I/O during file picker operations (search for `"[FileIndex] loaded ignore patterns"`)
- Fixed the glob base path extraction on Windows to consider both `/` and `\\` as path separators (search for `"lastIndexOf"`)
- Fixed conversation rewind to properly reset state by calling `Ft()` after rewind (search for `"tengu_conversation_rewind"`)
- Fixed atomic file write error logging to use `level: "error"` instead of the default level (search for `"Failed to write file atomically"`)
- Removed extraneous blank line before `<fast_mode_info>` in the environment info system prompt

### Session Time Cap (24h)

What: Infrastructure for capping bridge sessions to a maximum runtime of 24 hours in privileged namespaces.

Status: Stubbed — the check variable is hardcoded to `false` (`!1`), so the cap never activates.

Details:
- When enabled, sessions would log "Session capped to 24h in this namespace (privileged namespace policy)" and automatically shut down after the timeout
- Applies to both standalone bridge mode and REPL bridge sessions
- On expiry, logs "Maximum runtime reached, shutting down…" and aborts the session

Evidence: Session cap infrastructure (hardcoded to `!1`, search for `"Session capped to 24h"`)


### Session Turn Uploader

What: Infrastructure to upload per-turn data after each conversation turn completes.

Status: Stubbed — the uploader variable is initialized to `null` and never populated.

Details:
- A new `onTurnComplete` callback parameter has been added to the REPL configuration
- When a turn uploader is available, it would be called with turn data after each turn
- The `createSessionTurnUploader` function exists but the initialization path is disabled (`r4 = null`)

Evidence: Turn upload infrastructure (search for `"createSessionTurnUploader"`)


### `DISABLE_FEEDBACK_COMMAND` Environment Variable

What: A new `CLAUDE_CODE_DISABLE_FEEDBACK_COMMAND` environment variable has been added to the known env var list.

Status: The variable is recognized but the feedback command disabling behavior is not fully wired up in this version.

Evidence: Env var registration (search for `"DISABLE_FEEDBACK_COMMAND"`)
