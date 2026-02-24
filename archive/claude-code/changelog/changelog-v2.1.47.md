# Changelog for version 2.1.47


## Summary

This release introduces Remote Control (`/remote-control`), enabling access to CLI sessions from claude.ai/code or the Claude app. It adds a new `--thinking` flag with adaptive thinking support for Opus 4.6+, enhanced dangerous command warnings with detailed notes, and the ability to kill background agents via `ctrl+f`. Plugin security improvements include automatic flagging of delisted plugins.

### Remote Control

What: Access your CLI session from the web (claude.ai/code) or the Claude app, continuing conversations across devices.

Usage:
```bash
/remote-control
```

Details:
- Opens a secure connection to claude.ai
- Shows "Remote Control active" status in the CLI
- Reconnects automatically if connection drops
- Run `/remote-control` again to disconnect remote access
- Can be enabled for all sessions or just the current session

Evidence: Remote Control UI and SSETransport infrastructure (search for `"/remote-control"`, `"Remote Control lets you access"`)


### Adaptive Thinking with --thinking Flag

What: New `--thinking` flag provides semantic control over Claude's thinking/reasoning behavior, replacing the deprecated `--max-thinking-tokens`.

Usage:
```bash
claude --thinking enabled   # Claude decides when and how much to think
claude --thinking disabled  # No extended thinking
claude --thinking 10000     # Fixed thinking token budget (older models)
```

Details:
- For Opus 4.6+, adaptive mode lets Claude autonomously decide thinking depth
- Takes precedence over the deprecated `maxThinkingTokens` setting
- The old `--max-thinking-tokens` flag is now deprecated with guidance to use `--thinking` instead

Evidence: Thinking mode options (search for `"--thinking <mode>"`, `"Claude decides when and how much to think (Opus 4.6+)"`)


### Kill Background Agents

What: Quickly terminate all running background agents with a keyboard shortcut.

Usage:
- Press `ctrl+f` once to open search
- Press `ctrl+f` again to kill all background agents

Details:
- New `chat:killAgents` action bound to double `ctrl+f`
- Shows "All background agents killed" confirmation
- Also available via text commands: "kill agents", "kill all agents"

Evidence: Agent termination system (search for `"All background agents killed"`, `"chat:killAgents"`)


### SSH Connection Configuration

What: Pre-configured SSH connections for remote environments, typically set by enterprise administrators.

Details:
- New `sshConfigs` setting for managed settings
- Supports configuration of:
  - SSH host (user@hostname or alias from ~/.ssh/config)
  - SSH port (default: 22)
  - Display name for the connection
  - Path to SSH identity file (private key)
  - Unique identifier for matching configs across settings sources

Evidence: SSH config schema (search for `"SSH connection configurations for remote environments"`)


### Enhanced Dangerous Command Warnings

What: Bash commands that may have destructive effects now show detailed warning notes explaining the potential impact.

Details:
- New warning notes for potentially dangerous commands:
  - `Note: may delete Kubernetes resources`
  - `Note: may delete all rows from a database table`
  - `Note: may destroy Terraform infrastructure`
  - `Note: may discard all working tree changes`
  - `Note: may discard uncommitted changes`
  - `Note: may drop or truncate database objects`
  - `Note: may force-delete a branch`
  - `Note: may force-remove files`
  - `Note: may overwrite remote history`
  - `Note: may permanently delete untracked files`
  - `Note: may permanently remove stashed changes`
  - `Note: may recursively force-remove files`
  - `Note: may rewrite the last commit`
  - `Note: may skip safety hooks`
- Blocked commands show "Permission for this action was denied by the dangerous action safety classifier"

Evidence: Warning note strings (search for `"Note: may delete"`, `"dangerous action safety classifier"`)

### Plugin Security System

What: Automatic detection and handling of security-flagged plugins from the official marketplace.

Details:
- Fetches security messages from `https://raw.githubusercontent.com/anthropics/claude-plugins-official/refs/heads/security/security.json`
- Auto-uninstalls delisted plugins when `autoUninstallDelisted` is enabled
- Shows "Plugins flagged. Check /plugins" notification
- New `blocklist.json` and `flagged-plugins.json` files for tracking
- "Removed from marketplace" indicator with optional reason

Evidence: Plugin security infrastructure (search for `"Fetching plugin security messages"`, `"flagged-plugins.json"`)


### Version Manager Detection

What: Automatic detection and logging of asdf and mise version manager installations.

Details:
- Logs "Detected asdf installation:" when asdf is found
- Logs "Detected mise installation:" when mise is found
- Helps diagnose shell environment issues

Evidence: Version manager detection (search for `"Detected asdf installation"`)


### Plugin Settings from settings.json

What: Plugins can now load settings from a `settings.json` file in addition to manifest settings.

Details:
- Looks for `settings.json` in plugin directory
- Falls back to manifest settings if not found
- Settings can specify `agent` configuration to merge when plugin is enabled
- Logs which settings source was used

Evidence: Plugin settings loader (search for `"Loaded settings from settings.json for plugin"`)


### Improved Fast Mode Status Display

What: Better messaging when fast mode encounters issues.

Details:
- "Fast mode overloaded and is temporarily unavailable" message
- Shows reset time: "resets in X"
- "· Fast mode ON" indicator

Evidence: Fast mode messages (search for `"Fast mode overloaded"`)


### BMP Image Support in Clipboard

What: Added BMP format support for clipboard image operations on Linux.

Details:
- Now detects `image/bmp` in clipboard alongside png, jpeg, gif, webp
- Uses `wl-paste --type image/bmp` or `xclip -selection clipboard -t image/bmp`

Evidence: BMP handling (search for `"image/bmp"`)


### Warp Terminal Native Shift+Enter Support

What: Warp now supports Shift+Enter natively, removing previous workaround messaging.

Details:
- Updated tip: "Note: iTerm2, WezTerm, Ghostty, Kitty, and Warp support Shift+Enter natively."
- Removed previous warnings about Warp not supporting custom Shift+Enter keybindings
- Warp removed from the list of terminals requiring manual configuration

Evidence: Terminal compatibility notes (search for `"Warp support Shift+Enter natively"`)


### Improved /rename Behavior Setting

What: New setting to control whether `/rename` updates the terminal tab title.

Details:
- Setting: "Whether /rename updates the terminal tab title (defaults to true)"
- Set to false to keep auto-generated topic titles
- Replaces the previous inverse setting behavior

Evidence: Rename setting (search for `"Whether /rename updates the terminal tab title"`)


### Permission Validation Improvements

What: Invalid permission rules in configuration files are now validated and skipped with warnings.

Details:
- Non-string values in permission arrays are removed with warning
- Invalid permission rules show specific error messages
- Logs which file and path contained the invalid rule

Evidence: Permission validation (search for `"Invalid permission rule"`, `"was skipped"`)


### Agent Worktree Cleanup

What: Better management and cleanup of git worktrees created by agents.

Details:
- Detects when agent worktree has uncommitted changes: "Agent worktree has changes, keeping:"
- Logs worktree removal: "Removed agent worktree at:"
- Handles branch cleanup failures gracefully

Evidence: Worktree management (search for `"Agent worktree has changes"`, `"worktreePath:"`)


### In-Process Chrome MCP Server

What: Chrome browser automation MCP server can now run in-process for better performance.

Details:
- Logs "In-process Chrome MCP server started" when initialized
- Uses new SSE transport infrastructure
- Cleaner shutdown handling

Evidence: Chrome MCP server (search for `"In-process Chrome MCP server started"`)


### Pure JavaScript Path Conversion on Windows

What: Windows path conversion (Unix ↔ Windows) is now done in pure JavaScript, removing the dependency on cygpath.

Details:
- Handles `/cygdrive/` prefix conversion
- Converts forward/backslashes appropriately
- Works with UNC paths (starting with `//` or `\\`)

Evidence: Path conversion logic (search for `"/cygdrive/"`)

## Bug Fixes

- Fixed backslash-escaped whitespace warning for commands that could alter command parsing (search for `"Command contains backslash-escaped whitespace"`)
- Fixed plugin hooks reload to only trigger on actual `enabledPlugins` changes, not all policySettings changes (search for `"Plugin hooks: skipping reload, enabledPlugins unchanged"`)
- Fixed hook file reading errors to log properly: "Failed to read hook file" (search for `"Failed to read hook file"`)
- Added validation for parent directory existence: "Parent directory does not exist or is not accessible:" (search for `"Parent directory does not exist"`)

## Notes

**Deprecation**: The `--max-thinking-tokens` flag is deprecated. Use `--thinking <mode>` instead for newer models. The flag still works for backward compatibility.

**Removed Features**: Delegate Mode infrastructure has been removed. References to TeammateTool, delegate mode, and team coordination are no longer present in the codebase.
