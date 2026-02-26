# Changelog for version 2.1.59


## Summary

This is a major release that introduces **voice dictation mode**, allowing users to hold Space to speak instead of typing. It also adds a new **`fastModePerSessionOptIn` setting** so fast mode resets each session, overhauls the **copy-to-clipboard experience** to let users pick specific code blocks, adds support for **`CLAUDE_CODE_OAUTH_REFRESH_TOKEN`** for headless login, and bundles a **ZIP-based plugin caching system** for headless/CI environments. Opus 4.6 model routing via the `coral_reef_opus` flag is also introduced.


### Voice Dictation Mode

What: Hold the Space bar to dictate text via speech-to-text, with real-time transcription streamed over WebSocket to Claude.ai's `/api/ws/speech_to_text/voice_stream` endpoint.

Usage:
```
/voice          # Toggle voice mode on/off
```
Then hold Space to record; release to stop. The transcript is injected into the input field.

Details:
- Requires a Claude.ai account (OAuth); run `/login` first if not signed in
- Persisted via the `voiceEnabled` setting in `settings.json`
- Audio capture uses a bundled native module (`audio-capture.node`) on macOS/Linux, with fallback to `sox` (`rec` command) or `arecord` on Linux
- Offers guided SoX installation (detects `brew`, `apt-get`, `dnf`, `pacman`) if no audio tool is found
- Supports a "focus mode" that continuously records when the terminal has focus, flushing each finalized segment immediately
- Cursor displays an animated audio-level indicator (bar graph characters ` ▁▂▃▄▅▆▇█`) with color cycling while recording
- Shows "listening…" while recording and an animated "Voice: processing…" while finalizing
- Supports 11 languages: English, Spanish, French, Japanese, German, Portuguese, Italian, Korean, Chinese, Hindi, Indonesian — configured via the `language` setting
- Microphone permission checks with platform-specific guidance (macOS: System Settings → Privacy & Security → Microphone; Linux: system audio settings; Windows: Settings → Privacy → Microphone)
- Not available in remote/headless environments — prints helpful message directing users to run locally

Evidence: `/voice` command (search for `"Toggle voice mode"`), WebSocket client (search for `"/api/ws/speech_to_text/voice_stream"`), settings definition (search for `"voiceEnabled"`)

**[Gradual Rollout]** — Gated behind the `tengu_amber_quartz` feature flag (defaults to `!1`/false). The `/voice` command is hidden when the flag is off. Users with the flag enabled who are logged in to Claude.ai can use this feature.


### Headless Login via Refresh Token

What: Log in to Claude Code non-interactively by providing an OAuth refresh token via environment variables, enabling automated CI/CD and headless deployments without a browser.

Usage:
```bash
export CLAUDE_CODE_OAUTH_REFRESH_TOKEN="your-refresh-token"
export CLAUDE_CODE_OAUTH_SCOPES="user:inference"
claude /login
```

Details:
- `CLAUDE_CODE_OAUTH_SCOPES` is required when using the refresh token — the CLI exits with a helpful error message if missing
- Scopes should be space-separated (e.g., `"user:profile user:inference user:sessions:claude_code user:mcp_servers"`)
- Bypasses the browser-based OAuth flow entirely

Evidence: Refresh token login flow (search for `"CLAUDE_CODE_OAUTH_REFRESH_TOKEN"`)


### Fast Mode Per-Session Opt-In Setting

What: A new `fastModePerSessionOptIn` setting makes fast mode non-persistent, so each new session starts with fast mode off.

Details:
- When `true`, fast mode does not carry over between sessions — users must re-enable it each session
- Useful for users who want fast mode available but not always on by default

Evidence: Setting description (search for `"When true, fast mode does not persist across sessions"`)


### Enhanced Copy to Clipboard

What: The copy command now lets you choose between copying the full response or individual code blocks, with language-aware file extensions for saved snippets.

Details:
- When Claude's response contains code blocks, pressing the copy shortcut presents a picker: "Full response" or each individual code block (with language label and line count)
- Falls back to saving to a file (e.g., `response.md`, `copy.py`) if clipboard access is unavailable, and shows the file path
- Replaces the old behavior that only copied the full response as markdown
- The old shell-snippet-only copy feature (`tengu_snippet_save`) has been removed

Evidence: New UI text (search for `"Select content to copy:"`), file save (search for `"response.md"`)


### Plugin ZIP Cache System

What: A new ZIP-based caching system for MCP plugins, enabling efficient plugin distribution in headless and CI environments.

Details:
- Controlled by the `CLAUDE_CODE_PLUGIN_CACHE_DIR` environment variable
- Creates versioned ZIP archives of plugin directories (with `.zip` extension)
- Session-scoped plugin cache directories (`claude-plugin-session-*`) are automatically created and cleaned up
- Marketplace JSON metadata is persisted alongside plugin ZIPs for offline resolution
- Handles symlink cycles during ZIP creation with cycle detection
- Includes `CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL` env var to disable automatic marketplace plugin installation

Evidence: ZIP cache mode (search for `"zip cache mode"`), session cache (search for `"claude-plugin-session-"`)


### VCS Type Detection

The platform detection module now identifies the version control system in use. It checks for `.git` (git), `.hg` (Mercurial), `.svn` (SVN), `.p4config`/`P4PORT` (Perforce), and `$tf`/`.tfvc` (TFS). This information is included in environment telemetry.

Evidence: VCS detection map (search for `"mercurial"`, `"perforce"`)


### Linux Distro Metadata Collection

On Linux systems, Claude Code now reads `/etc/os-release` to capture `linuxDistroId`, `linuxDistroVersion`, and `linuxKernel` for improved platform-specific diagnostics.

Evidence: Distro detection (search for `"linuxDistroId"`)


### Background Task Count in Turn Duration

The turn duration indicator now shows how many background tasks are still running after each turn (e.g., `· 2 background tasks still running ↓`), making it easier to track background task activity.

Evidence: Status line rendering (search for `"background task"` and `"still running"`)


### Auto-Memory Label No Longer "Research Preview"

The auto-memory feature label has been updated from "Auto-memory (research preview)" to simply "Auto-memory", indicating the feature has graduated from its experimental phase.

Evidence: String change — removed `"Auto-memory (research preview):"`, added `"Auto-memory:"`


### MCP Config File Atomic Writes

Writing `.mcp.json` now uses atomic file writes (write to temp file, then rename) to prevent corruption if the process is interrupted mid-write.

Evidence: Atomic write helper (search for `".mcp.json"` in added function `Vw7`)


### MCP OAuth Refresh Lock

A new file-based locking mechanism prevents concurrent MCP server OAuth token refreshes from colliding. Lock files (`mcp-refresh-*.lock`) coordinate between processes with retry logic and timeout handling.

Evidence: Lock file naming (search for `"mcp-refresh-"`)


### Hook Output Error Message Improvement

When a hook produces invalid JSON output, the error message now says "The hook's output was:" (previously "The hook's stdout was:"), more accurately reflecting that output may come from various sources.

Evidence: Error message (search for `"The hook's output was:"`)


### Working Directory Existence Check

Claude Code now detects when its working directory has been deleted and shows a clear error: `Working directory "..." no longer exists. Please restart Claude from an existing directory.`

Evidence: Error message (search for `"no longer exists. Please restart"`)


### Worktree Cleanup Error Handling

If git worktree cleanup fails during session exit, the error is now caught and logged (`"Worktree cleanup failed, exiting anyway"`) instead of potentially blocking shutdown.

Evidence: Error message (search for `"Worktree cleanup failed"`)


### Repo Text Size Metric

A new telemetry metric (`tengu_repo_text_file_size`) calculates the total byte size of text source files in the repo using `git ls-tree`. It counts files with common code extensions (.ts, .py, .js, .go, .rs, etc.) to help understand repository scale.

Evidence: Metric calculation (search for `"repoTextSize"`)


### Session Memory Loading Improvement

Session memory loading now uses async file reading and handles `ENOENT`/`EACCES`/`EPERM` errors gracefully by returning null, instead of synchronously checking file existence first.

Evidence: Error handling (search for `"tengu_session_memory_loaded"`)


## Bug Fixes

- Fixed safe-flag parsing for combined short flags in commands like `grep` and `rg` (e.g., `-A5` is now correctly recognized as `-A` with value `5` when `-A` accepts a number) (search for `"grep"` and `"rg"` in function `Hn7`)

- Improved Remote Control error messaging: users on unsupported plans now see "Error: Remote Control is not yet available on your plan." (search for `"Remote Control is not yet available"`)

- Fixed `line-reference` edit operations to properly validate hash mismatches with clear error messages showing expected vs actual hash, preventing silent corruption when files change between reads (search for `"LINE#HASH"`)


### Opus 4.6 Model Routing [Gradual Rollout]

What: Infrastructure for routing requests to the Opus 4.6 model when a `coral_reef_opus` feature flag is enabled server-side.

Status: Feature-flagged via `coral_reef_opus`

Details:
- When `coral_reef_opus` is `"true"` and the model string contains `"opus-4-6"`, a special token limit of 1,000,000 is applied
- Extended output is enabled for matching Opus 4.6 models via the `HbA()` function
- Gated behind multiple checks: not in test mode, not using custom provider

Evidence: Model routing (search for `"coral_reef_opus"`, `"opus-4-6"`)
