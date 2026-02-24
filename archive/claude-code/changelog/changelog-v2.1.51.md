# Changelog for version 2.1.51


## Summary

This release introduces the `/commit-push-pr` command for one-step PR creation with Claude Code attribution stats, a substantially rebuilt Remote Control bridge for controlling CLI sessions from claude.ai/code, enterprise MDM (Mobile Device Management) settings support on macOS and Windows, and significantly expanded auto-approve safe command lists for Docker Compose, ripgrep, pyright, and more.

### `/commit-push-pr` Command

What: A new built-in slash command that creates a branch, commits staged changes, pushes to origin, and opens (or updates) a pull request — all in a single action.

Usage:
```bash
# Inside a Claude Code session:
/commit-push-pr
/commit-push-pr add reviewer @teammate
```

Details:
- Automatically detects the base branch and creates a feature branch using your username prefix
- Drafts a commit message following your repository's commit style
- Creates or updates a PR with summary, test plan, and changelog sections
- Includes enhanced PR attribution: `🤖 Generated with Claude Code (X% N-shotted by claude-model-name, M memories recalled)`
- If CLAUDE.md references Slack channels, optionally posts the PR URL via Slack MCP tools
- Auto-approves the git and GitHub CLI commands needed (no manual permission prompts)

Evidence: Skill definition with `name: "commit-push-pr"` and `description: "Commit, push, and open a PR"` (search for `"/commit-push-pr"`)


### `.worktreeinclude` File Support

What: A new configuration file that specifies gitignored files to copy into git worktrees, solving the problem of missing config files or local secrets in worktree-based workflows.

Usage:
```bash
# Create .worktreeinclude in your project root
# List gitignored files/patterns that should be copied to worktrees:
.env
.env.local
config/local.json
```

Details:
- Placed at the project root alongside `.gitignore`
- When a worktree is created, files matching `.worktreeinclude` patterns that are also gitignored are automatically copied from the main working directory into the worktree
- Blank lines and lines starting with `#` are treated as comments
- Uses `git ls-files --others --ignored --exclude-from=.worktreeinclude` to identify matching files

Evidence: New function `lc4` reads `.worktreeinclude` and copies files (search for `".worktreeinclude"`)


### Enterprise MDM Settings Support

What: Claude Code can now read enterprise-managed configuration policies from platform-native MDM (Mobile Device Management) sources, enabling IT administrators to enforce organizational settings.

Details:
- macOS: Reads managed preferences from `/Library/Managed Preferences/com.anthropic.claudecode.plist` (device-level and per-user)
- Windows: Reads registry keys from `HKLM\SOFTWARE\Policies\ClaudeCode` and `HKCU\SOFTWARE\Policies\ClaudeCode`
- Falls back to file-based managed settings (`managed-settings.json`) on other platforms
- Polls for MDM settings changes every 30 minutes and applies updates live
- Settings are parsed through the same Zod schema validation as regular settings

Evidence: Domain identifier `"com.anthropic.claudecode"`, registry paths `"HKLM\\SOFTWARE\\Policies\\ClaudeCode"`, function `pE1()` reads platform-specific MDM sources (search for `"com.anthropic.claudecode"`)


### Expanded Safe Command Auto-Approval

What: The bash permission classifier now auto-approves significantly more read-only commands without prompting the user.

Details:
- Docker Compose: `docker compose ps`, `docker compose logs`, `docker compose top`, `docker compose config`
- Docker: `docker logs`, `docker inspect` (with safe flag validation)
- Ripgrep (`rg`): comprehensive flag support for search operations
- Pyright: type-checking with safe flags (blocks `--watch` mode)
- Package managers: `npm list`, `pip list` with safe flags
- Version checks: `node -v`, `npm -v`, `python --version`, `python3 --version`
- Python removed from the "suspicious command" blocklist — `python` and `python3` are no longer flagged

Evidence: New safe command definitions for `"docker compose ps"`, `"docker compose logs"`, `rg`, `pyright`, `"npm list"`, `"pip list"` (search for `"docker compose ps"`)


### Brace Expansion Security Check

What: Commands containing shell brace expansion patterns (e.g., `{a,b}` or `{1..5}`) are now detected and flagged, preventing potential command injection through expansion tricks.

Details:
- Detects balanced brace pairs containing commas or range operators (`..`)
- Properly handles nested braces and escaped characters
- Blocks commands where brace expansion could alter command parsing

Evidence: New function `ve9()` performs brace detection; error message `"Command contains brace expansion that could alter command parsing"` (search for `"brace expansion"`)

### Remote Control Bridge Overhaul

The Remote Control feature (`/remote-control`) has been substantially rebuilt with a full bridge architecture for controlling CLI sessions from claude.ai/code. The feature flag was changed from `tengu_worktree_mode` to `tengu_ccr_bridge`, and the implementation now includes:

- Full work-polling loop with session spawn/teardown lifecycle
- WebSocket-based session ingress for real-time communication
- QR code display (togglable with spacebar) for quick mobile connection
- Automatic OAuth token refresh with JWT expiry tracking
- Environment registration, deregistration, and re-registration on failure
- Reconnection with exponential backoff and error budget
- Session activity tracking (tool starts, text output, results)
- `remoteControlAtStartup` setting to auto-enable Remote Control for all sessions
- `allow_remote_sessions` policy for organization-level control

Evidence: Feature flag `tengu_ccr_bridge`, command definition `name: "remote-control"` with aliases `["rc"]` (search for `"tengu_ccr_bridge"`)


### LLM-Based Memory Retrieval

The memory system has been redesigned to use LLM-based retrieval instead of grep-based keyword search. Previously, memories were found by extracting search terms and grep-matching against markdown files. Now:

- Memories are listed with filenames and descriptions
- An LLM selects the most relevant memories (up to 5) based on the user's query
- Memories already read via the `Read` tool in the current conversation are filtered out to avoid duplication
- Memory files support a `description` frontmatter field for better retrieval

Evidence: Selection prompt `"You are selecting relevant memories for a user's query..."` and function `x8q` for deduplication (search for `"You are selecting relevant memories"`)


### MCP OAuth Improvements

- Step-up scopes are now persisted across auth revocations, preventing users from having to re-authorize expanded permissions
- OAuth discovery state (authorization server URL, resource metadata) is cached to avoid repeated discovery requests
- New `skipBrowserOpen` option for headless environments — logs the authorization URL instead of opening a browser
- `preserveStepUpState` flag during MCP authentication prevents loss of elevated permissions

Evidence: `"Persisted step-up scope:"` log message, `"Saving discovery state"` log message (search for `"Persisted step-up scope"`)


### WebSocket Transport Enhancements

- New `autoReconnect` option to disable automatic reconnection (useful for bridge sessions that manage their own lifecycle)
- `onConnect` callback fires when connection is established
- `getStateLabel()` exposes current connection state
- Close callbacks now receive the WebSocket close code for better error handling

Evidence: `autoReconnect` parameter in constructor, new `setOnConnect` and `getStateLabel` methods (search for `"autoReconnect"`)


### Model Selector Version Hints

When selecting a model in the CLI, if you have a pinned older model version (e.g., `claude-sonnet-4-5`), the selector now shows a helpful hint like "Newer version available · select Sonnet for claude-sonnet-4-6", guiding you to the latest version.

Evidence: Function `o_z` returns `description: "Newer version available · select ${alias} for ${currentVersionName}"` (search for `"Newer version available"`)


### Plugin Registry and Version Support

npm-sourced plugins now accept `--registry` and `--version` options, allowing installation from private registries or pinning to specific versions.

Evidence: Plugin install function now passes `{ registry: A.registry, version: A.version }` (search for `"--registry"`)


### Workspace Trust Enforcement for Hooks

StatusLine and FileSuggestion hook commands now verify workspace trust before executing. If the workspace trust dialog hasn't been accepted, these hooks are skipped with a warning, preventing untrusted workspaces from running arbitrary hook commands.

Evidence: `"Skipping StatusLine command execution - workspace trust not accepted"` and `"Skipping FileSuggestion command execution - workspace trust not accepted"` (search for `"workspace trust not accepted"`)


### Vim Mode ESC Fix

Pressing Escape in Vim NORMAL mode now properly resets the command state to idle, fixing cases where partial command sequences could leave the input in an unexpected state.

Evidence: New condition `if (M.escape && W.mode === "NORMAL")` resets to `{ mode: "NORMAL", command: { type: "idle" } }` (search for `"NORMAL"` in the Vim handler)


### Duplicate Permission Response Handling

The structured transport now tracks resolved tool-use IDs and silently ignores duplicate `control_response` messages, preventing race conditions where a late-arriving permission response could cause errors.

Evidence: `"Ignoring duplicate control_response for already-resolved toolUseID="` (search for `"Ignoring duplicate control_response"`)

## Bug Fixes

- Fixed notification content rendering crash when `content` is not a string — now returns `null` gracefully instead of attempting to render non-string content (search for `"typeof $ !== \"string\""`)
- Removed the "Denied by auto mode classifier" banner that previously displayed when permissions were auto-denied, reducing UI noise
- Permission rule normalization now properly trims and normalizes stored rules when checking against new requests, preventing duplicate or stale rules (search for `"r5(nX(j))"`)
- HTTP hooks now properly skip when conditions aren't met instead of potentially erroring (search for `"Skipping HTTP hook"`)

### Smart Tool Deferral [Gradual Rollout]

What: An intelligent tool deferral system that tracks your tool usage patterns and only defers tools you haven't used recently, keeping frequently-used tools immediately available.

Status: Feature-flagged behind `tengu_coral_whistle` (default: `true`)

Details:
- Tracks tool usage count and last-used timestamp in config (`toolUsage`)
- Uses a 7-day half-life decay function to compute a "recency-weighted usage score"
- Tools below the threshold are deferred (loaded on demand via ToolSearch)
- MCP tools are always deferred regardless of this flag
- When enabled, the `shouldDefer` flag on a tool triggers the usage-based check

Evidence: `tengu_coral_whistle` feature flag, functions `h84` (track usage), `I84` (compute score with decay), `b84` (check threshold) (search for `"tengu_coral_whistle"`)


### Multiple Stubbed Commands [In Development]

Several new slash command slots have been added as stubs (`isEnabled: () => !1, isHidden: !0`), indicating upcoming features. At least 15 new stub commands were added in this version, suggesting significant new functionality in the pipeline.

Evidence: Multiple `{ isEnabled: () => !1, isHidden: !0, name: "stub" }` definitions throughout the added code


### Built-in Claude API / Agent SDK Skill [In Development]

What: A comprehensive built-in skill for helping users build LLM-powered applications with Claude, including code examples for Python, TypeScript, Java, Go, Ruby, C#, PHP, and cURL.

Status: Added as part of the skills system, contains full documentation for:
- All current Claude models (Opus 4.6, Sonnet 4.6, Haiku 4.5)
- Adaptive thinking, effort parameter, compaction
- Tool use, streaming, batches, files API
- Agent SDK patterns
- Language-specific SDK examples including a new C# SDK section

Evidence: Large string literal beginning with `"# Building LLM-Powered Applications with Claude"` (search for `"Building LLM-Powered Applications with Claude"`)
