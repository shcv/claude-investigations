# Changelog for version 2.1.40


## Summary

This release adds a new `claude auth` command group for managing authentication, introduces a snippet picker UI with `Ctrl+Q` for copying code snippets, and adds enterprise model restriction capabilities. The macOS sandbox gains support for TLS certificate verification in Go programs, and the `/rename` command can now auto-generate session names using LLM.


### `claude auth` Command Group
What: New CLI subcommands for managing authentication outside interactive mode.

Usage:
```bash
claude auth login              # Sign in to your Anthropic account
claude auth login --email me@example.com  # Pre-populate email on login page
claude auth login --sso        # Force SSO login flow
claude auth status             # Show authentication status
claude auth status --text      # Human-readable output
claude auth logout             # Log out from your Anthropic account
```

Details:
- Replaces the need to use `/login` and `/logout` slash commands
- `--json` flag outputs machine-readable status (default)
- `--text` flag outputs human-readable status

Evidence: Auth command group (search for `"Manage authentication"`, `"Sign in to your Anthropic account"`)


### Snippet Picker UI
What: New interface for selecting and copying code snippets from Claude's responses.

Usage:
- Press `Ctrl+Q` to open the snippet picker
- Select from multiple snippets when available
- Status bar shows snippet count: "ctrl+q to copy · N snippets"

Details:
- Keybinding changed from `Ctrl+Y` (copy single) to `Ctrl+Q` (picker)
- Works with SSH sessions
- Displays "Select a snippet to copy:" when multiple snippets exist

Evidence: Snippet picker keybinding (search for `"chat:snippetPicker"`, `"ctrl+q to copy"`)


### Enterprise Model Allowlist
What: Administrators can restrict which models users can select.

Usage:
Configure in managed settings:
```json
{
  "availableModels": ["opus", "sonnet-4"]
}
```

Details:
- Accepts family aliases ("opus" allows any opus version)
- Accepts version prefixes ("opus-4-5" allows only that version)
- Accepts full model IDs
- Empty array restricts to default model only
- Clear error messages when restricted: "Model 'X' is not available. Your organization restricts model selection."

Evidence: Model allowlist setting (search for `"Allowlist of models that users can select"`, `"restricts model selection"`)


### Nested Session Detection
What: Prevents launching Claude Code inside another Claude Code session.

Details:
- Detects when running inside an existing Claude Code session
- Displays clear error explaining the issue
- Provides bypass instructions via `CLAUDECODE` environment variable

Evidence: Nested session check (search for `"cannot be launched inside another Claude Code session"`)


### LLM-Generated Session Names
What: `/rename` can now auto-generate kebab-case session names from conversation context.

Usage:
```
/rename          # Auto-generates name from conversation
/rename my-name  # Still accepts manual names
```

Details:
- Generates 2-4 word kebab-case names (e.g., "fix-login-bug", "add-auth-feature")
- Shows "Could not generate a name: no conversation context yet" if no messages exist
- Falls back to manual name requirement if generation fails

Evidence: LLM name generation (search for `"Generate a short kebab-case name"`, `"no conversation context yet"`)


### Streaming Idle Timeout
What: Streams now abort automatically if no data is received for extended periods.

Details:
- Warning logged when stream is idle
- Automatic abort after configurable timeout
- Throws "Stream idle timeout - no chunks received" error

Evidence: Idle timeout handling (search for `"Streaming idle timeout"`, `"no chunks received"`)


### macOS Sandbox: TLS Certificate Verification
What: New setting to allow Go programs to verify TLS certificates via trustd agent.

Usage:
Configure in sandbox settings:
```json
{
  "enableWeakerNetworkIsolation": true
}
```

Details:
- Required for Go programs (gh, gcloud, terraform, kubectl) using MITM proxies with custom CAs
- Enables access to `com.apple.trustd.agent` mach service
- Security trade-off: Opens potential data exfiltration vector through trustd

Evidence: Trustd agent setting (search for `"Enable weaker network isolation"`, `"com.apple.trustd.agent"`)


### Expanded Network Binding in Sandbox
Network sandbox rules now allow binding to all interfaces (`*:*`) instead of just localhost.

Evidence: Network rules (search for `'(allow network-bind (local ip "*:*"))'`)


### Linux Sandbox Improvements
- Glob patterns are now expanded for deny paths on Linux
- Better handling of symlink-based deny path attacks (mounts `/dev/null`)
- Cleanup of bwrap mount points after sandbox teardown
- More nuanced logging for skipped deny paths

Evidence: Linux sandbox improvements (search for `"Cleaned up bwrap mount point"`, `"Expanded glob pattern"`, `"Mounted /dev/null"`)


### Improved Model Error Messages
Error messages now suggest alternative models when the selected model fails:
- 429 errors suggest switching to a fallback model
- 404 errors indicate model availability issues and suggest alternatives

Evidence: Model error handling (search for `"to switch to"`, `"to pick a different model"`)


### Better File Type Detection for Read Tool
The Read tool now properly rejects special files (devices, pipes, sockets) with clear error messages.

Evidence: File type check (search for `"not a regular file (it may be a device, pipe, or socket)"`)


### Team Plan Auto-Approval
When running as a team member, pending plan approval requests from teammates can be auto-approved based on team context.

Evidence: Auto-approval logging (search for `"Auto-approved plan from"`, `"auto-approving"`)


### VS Code Connection Indicator
New notification when only one Claude Code instance can connect to VS Code at a time.

Evidence: Connection note (search for `"Only one Claude Code instance can be connected to VS Code"`)


### Bypass Permissions Migration
Automatic migration from `bypassPermissionsModeAccepted` to `skipDangerousModePermissionPrompt` setting.

Evidence: Migration code (search for `"tengu_migrate_bypass_permissions_accepted"`)

## Bug Fixes

- Fixed read tool to reject special file types (devices, pipes, sockets) instead of hanging (search for `"not a regular file"`)
- Improved memory learning prompt to be more specific about saving corrections and preferences (search for `"consider saving that to memory"`)

## Internal Changes (Not User-Facing)

The following changes are internal and do not affect user behavior:

- Removed `fine-grained-tool-streaming-2025-05-14` beta header
- Removed cache marker fallback logging ("No stable tool found for cache marker")
- Removed "IDE disconnected" status indicator
- Removed proxy server reconnection logging
- Removed "Team/Task files are allowed for writing" logging
- Added maxVersion capping for auto-updater
- Improved interrupt handling with stream mode logging
