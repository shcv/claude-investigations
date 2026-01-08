# Changelog for version 2.0.66

## Highlights
This release introduces a new PID-based version locking system for more reliable updates, adds extra usage request capabilities for team/enterprise users, implements a prompt stash feature with `Ctrl+S`, and includes LSP (Language Server Protocol) server manager support for enhanced code intelligence.

### Prompt Stash (`Ctrl+S`)
**What:** Save your current prompt input and retrieve it later - useful when you want to temporarily switch to a different task without losing your in-progress prompt.
**How to use:**
```bash
# With text in prompt, press Ctrl+S to stash it
# Later, with empty prompt, press Ctrl+S to restore
```
**Details:**
- Stash indicator appears when you have a saved prompt
- First-time users see a hint after deleting significant text
- **Evidence**: `$()` function at line 21215-21220, stash hint logic at `$A.current` tracking

### Extra Usage Requests for Teams/Enterprise
**What:** Team and enterprise users can now request extra usage allocation from their organization admins directly from the CLI.
**How to use:**
```bash
/extra-usage
```
**Details:**
- Sends a `limit_increase` request to your organization administrator
- Checks for existing pending requests to prevent duplicates
- Different messaging for enabling vs increasing extra usage
- **Evidence**: `Sz2()` at line 425819, `xz2()` at line 425825, command handler at line 425842+

### LSP Server Manager
**What:** Full Language Server Protocol integration for enhanced code intelligence capabilities.
**How to use:**
Configure in `.lsp.json` files in your project or plugins.
**Details:**
- Automatic server initialization based on file extensions
- Supports `textDocument/didOpen`, `didChange`, `didSave`, `didClose` notifications
- Configurable `extensionToLanguage` mapping per server
- Tracks open files to avoid duplicate notifications
- **Evidence**: `$qB()` (LSP SERVER MANAGER) at line 285468, config loading at line 14717-14760

### Remote Agent Tasks
**What:** Support for remote agent task execution and monitoring.
**Details:**
- New `remote_agent` task type alongside `local_agent` and `local_bash`
- Progress monitoring with delta summaries
- Task notifications when remote tasks complete/fail
- **Evidence**: `RemoteAgentTask` at line 355509, `FJ8()` notification function at line 355382

### Browser Control Flags
**What:** Explicit control over Chrome browser usage for authentication flows.
**How to use:**
```bash
claude --chrome        # Force Chrome usage
claude --no-chrome     # Prevent Chrome usage
```
**Details:**
- Useful when multiple browsers are installed
- Controls authentication and web-based flows
- **Evidence**: `d85()` at line 16281-16282

### PID-Based Version Locking
**What:** More reliable version lock system that tracks process IDs instead of just file modification times.
**Details:**
- Detects if locking process is actually running
- Better stale lock cleanup on startup
- Enhanced error reporting showing which PID holds a lock
- Automatic cleanup of locks from crashed processes
- Feature-flagged via `tengu_pid_based_version_locking`
- **Evidence**: `ai()` at line 397742, `K91()` at line 397747, `V91()` cleanup at line 397896

### Plugin Caching Improvements
**What:** Enhanced plugin cache handling with empty directory detection and `.lsp.json`/`.mcp.json` file support.
**Details:**
- Removes empty cache directories before re-caching
- Copies `.mcp.json` and `.lsp.json` files from plugins
- Better error handling when cache copy fails
- **Evidence**: `UsA()` at line 259791, empty dir check at line 20246-20249, config file copy at line 20292-20296

### Plugin File Migration
**What:** Automatic migration of plugin metadata files.
**Details:**
- Renames `installed_plugins_v2.json` to `installed_plugins.json`
- Converts V1 format to V2 format automatically
- Cleans up orphaned plugin cache directories
- **Evidence**: Log message at line 16307, migration function around line 441936

### IDE Connection UX
**What:** Improved prompts and messaging for IDE auto-connect configuration.
**Details:**
- New confirmation dialog: "Do you wish to disable auto-connect to IDE?"
- Better help text: "You can also configure this in /config or with the --ide flag"
- Tip shown when no IDE connected: "You can enable auto-connect to IDE in /config or with the --ide flag"
- **Evidence**: Dialog at line 16472, tip at line 19792

### Glob Pattern Improvements
**What:** Better handling of glob patterns with directory prefixes.
**Details:**
- Extracts base directory from patterns like `src/**/*.ts`
- Passes relative pattern to ripgrep for more accurate matching
- **Evidence**: `GRB()` at line 489713, `EK5()` pattern extraction

### Update Lock Error Reporting
**What:** When updates fail due to locks, the error now includes which process ID is blocking.
**Details:**
- Returns structured `{success, lockHolderPid}` instead of boolean
- Helps debug update failures in multi-instance scenarios
- **Evidence**: Lock failure handling returning `lockHolderPid` in update function

### Think-back/Year in Review Feature
**What:** New `/think-back` command for viewing your Claude Code year in review animation.
**Details:**
- Installs thinkback plugin automatically
- Supports edit, fix, and regenerate modes
- Companion `/thinkback-play` command
- **Evidence**: Command definitions at lines 16872-16995, skill invocation prompts at line 16846-16850

### Message Management
- Added `removeMessageByUuid()` function for removing specific messages from conversation history
- **Evidence**: `Kn1()` at line 286854, `removeMessageByUuid()` at line 18839

### MCP Server Status Detection
- Added detection for "unknown" server status with `Op1()` helper
- **Evidence**: `Op1()` at line 260849, `xHB = "unknown"` at line 260852

### Semver Library Update
- Updated semver parsing and comparison utilities
- Added new comparison functions and range handling
- **Evidence**: New semver exports at line 14508-14554

### File Cache Size
- Added 50MB (`52428800` bytes) constant for file size limits
- **Evidence**: `Tw8` at line 393122
