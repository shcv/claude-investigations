# Changelog for version 2.1.48

## Summary
Version 2.1.48 introduces a `claudeMdExcludes` setting for selectively blocking CLAUDE.md files by glob pattern, a new `ConfigChange` hook event that fires when settings files change during a session, and PowerShell support as a named shell provider alongside Bash. Several internal subsystems are refactored including the prompt suggestion pipeline, worktree session management, and Ink rendering.

## New Features


### CLAUDE.md Exclusion by Glob Pattern
What: A new `claudeMdExcludes` setting lets users and projects specify glob patterns or absolute paths of CLAUDE.md files that should not be loaded into the context.

Details:
- Accepts an array of strings: absolute paths or glob patterns matched against full file paths using picomatch
- Example values: `"/home/user/monorepo/CLAUDE.md"`, `"**/code/CLAUDE.md"`, `"**/some-dir/.claude/rules/**"`
- Only applies to User, Project, and Local memory types; Managed/policy files cannot be excluded
- Matching is performed with `dot: true` so dotfiles are covered
- Backslash path separators are normalized before matching

Evidence: New setting added to the main settings schema (search for `"claudeMdExcludes"`)


### ConfigChange Hook Event
What: A new `ConfigChange` hook event fires whenever a configuration file is modified during a running session, letting hooks inspect or block runtime settings changes.

Details:
- Hook receives JSON input with `source` (one of `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills`) and `file_path`
- Exit code 0 allows the change; exit code 2 blocks it from being applied to the session; other exit codes show stderr to the user only
- `policy_settings` changes cannot be blocked (all results from the hook have `blocked: false` forced)
- `ConfigChange` is also now a valid enum value in the SDK hook event name schema

Evidence: New hook definition with description (search for `"ConfigChange"`)


### PowerShell Shell Provider
What: Claude Code can now use PowerShell (`pwsh` or `powershell`) as a named shell provider in addition to Bash, enabling native Windows shell execution.

Details:
- Discovers `pwsh` first (PowerShell Core), falls back to `powershell` (Windows PowerShell)
- Captures the working directory after each command using `Get-Location` written to a temp file
- Shell invoked with `-NoProfile -NonInteractive -Command`
- The shell registry now explicitly maps `"bash"` and `"powershell"` as named providers
- Not yet user-selectable from settings; this is provider infrastructure

Evidence: New `Ea7` builder function and `bV9` discovery function (search for `"-NoProfile"`)


### MCP Needs-Auth Cache
What: A persistent cache (`mcp-needs-auth-cache.json`) records which MCP servers require authentication so Claude Code can remember auth state across restarts.

Details:
- Cache entries store a timestamp; entries expire after a configurable TTL (`hi9`)
- Writes are serialized through a promise chain to avoid concurrent write corruption
- `g54` function clears the cache file when called

Evidence: New functions `OG8`, `FY4`, `Ii9`, `wG8`, `g54` (search for `"mcp-needs-auth-cache.json"`)


### Sandbox Network Permission Prompts
What: The WebSocket transport now supports prompting the user for approval before allowing a sandboxed process to make a network connection to a given host.

Details:
- New `createSandboxAskCallback` method on the WebSocket client class sends a `can_use_tool` request with `subtype: "can_use_tool"` and the target host
- User sees a prompt: "Allow network connection to [host]?"
- Returns `true` if the user approves, `false` otherwise (including on errors)

Evidence: New method `createSandboxAskCallback` (search for `"Allow network connection to"`)


### Prompt Suggestions in SDK
What: The `promptSuggestions` setting is now propagated through the SDK request path, and prompt suggestion telemetry now distinguishes between `"cli"` and `"sdk"` sources.

Details:
- `promptSuggestions` field forwarded from SDK options into the API request builder
- New `A$4` function emits `tengu_prompt_suggestion` telemetry with `source: "sdk"`
- The CLI path now emits telemetry with `source: "cli"`
- Suggestion generation in the CLI is refactored into a shared `af8` helper used by both paths
- A new `prompt_suggestion` SDK event type is added to the union of streamable event types (schema: `{ type: "prompt_suggestion", suggestion, uuid, session_id }`)

Evidence: `promptSuggestions` forwarding (search for `"promptSuggestions"`)


### Agent Task Completion Usage Stats in SDK
What: The SDK's agent completion event now includes a `usage` object with token count, tool call count, and duration.

Details:
- New optional field: `usage: { total_tokens, tool_uses, duration_ms }`
- Appears on the agent completion event alongside `status`, `output_file`, and `summary`

Evidence: New `usage` field in agent completion event schema (search for `"total_tokens"` near `"tool_uses"`)


### Model Capability Fields in SDK Schema
What: The SDK model info schema now exposes whether a model supports effort levels and adaptive thinking.

Details:
- New optional fields on the model object: `supportsEffort` (boolean), `supportedEffortLevels` (array of `"low" | "medium" | "high" | "max"`), and `supportsAdaptiveThinking` (boolean)

Evidence: New schema fields (search for `"supportsEffort"`)

## Improvements


### Hook Display Now Shows Hook Label and Duration
What: The hook result display component is rewritten to show the hook label (e.g., "PreToolUse") alongside the hook count, and to sum and display total hook duration.

Details:
- Old component (`oVY`) rendered a fixed "stop hook" message; the new `rdY` component is generic across all hook types
- When `hookLabel` is present, the component renders "Ran N [label] hooks" rather than "Ran N stop hooks"
- In verbose mode, individual hook command details (including prompt text for prompt-type hooks) are shown via `odY`
- Total duration is computed by summing `durationMs` across all hook info entries

Evidence: New component `rdY` replaces `oVY` (search for `"hook_label"` or `"durationMs"`)


### Memory Recall Display Improved
What: The display for auto-memory recall events is updated to show a summary count ("Recalled N memories") unconditionally, with individual paths shown only in verbose mode.

Details:
- Previously the non-verbose path showed a compact single-line summary; the verbose path showed individual "Recalled memory: [path]" entries
- Now both paths use the same container; the count summary is always visible; individual paths (dimmed) are shown only when verbose is true
- Memory paths are rendered using the `cdY` formatter rather than the bold `iVY` formatter

Evidence: Structural change to `x6q` / `Wg4` function (search for `"Recalled"`)


### Worktree Session Management Refactored
What: The `--worktree` and `--tmux` session setup code is substantially refactored, consolidating worktree creation and setup into shared helpers.

Details:
- `oS8` handles creating or resuming a worktree for a named session, including PR checkout support via `prNumber`
- `sS8` copies `settings.local.json` to the worktree and configures git hooks path to point at the main repo's hooks directory
- `NuY` symlinks configured directories from the main repo to avoid disk bloat
- `hG6` resolves the git common directory to find the true repo root even inside a worktree
- `IU6` is the main entry point for interactive worktree sessions
- The `--tmux` flag handling now reads the user's tmux prefix key and detects conflicts with common control sequences
- `Ln4` parses a GitHub PR URL or `#NNN` shorthand into a PR number for checkout

Evidence: New functions `oS8`, `sS8`, `IU6`, `kuY` (search for `"Linked worktree preserved at"`)


### IDE Command Gains "open" Subcommand
What: The `/ide` command handler now accepts an `open` argument that opens the current project (or active worktree) in a detected IDE.

Details:
- If the argument is `"open"`, Claude Code lists connected IDEs with the extension installed
- For VS Code, Cursor, and Windsurf, it runs `code [path]` to open the project
- For other IDEs it prints a manual instruction
- If multiple IDEs are detected, a selection UI is shown

Evidence: New `xuY` function with `K?.trim() === "open"` branch (search for `"open"` in context of `"tengu_ext_ide_command"`)


### WebSocket Transport Message Eviction Logging
What: When the WebSocket transport evicts confirmed messages from its buffer, it now logs the count of evicted and remaining messages.

Details:
- Emits a debug log: "WebSocketTransport: Evicted N confirmed messages, M remaining"
- Also emits a `cli_websocket_evicted_confirmed_messages` telemetry event with `{ evicted, remaining }`
- The `lastSentId` is cleared to `null` when the buffer becomes empty after eviction

Evidence: New logging in class `Rl6` (search for `"WebSocketTransport: Evicted"`)


### Ink Rendering: Periodic Yoga Layout Reset
What: The Ink renderer now resets the Yoga layout tree periodically to prevent memory accumulation from stale layout nodes.

Details:
- Every 5 minutes (300,000 ms), if the renderer is in a stable state, the yoga node tree is freed and rebuilt from scratch using `D27` (recursive free) followed by `X27` (recursive rebuild)
- The yoga root node is also explicitly freed on renderer unmount
- A `lastYogaResetTime` field tracks when the last reset occurred

Evidence: New `D27`, `X27`, `lW5` functions and `lastYogaResetTime` field (search for `"lastYogaResetTime"`)


### OAuth Metadata Caching for Remote MCP Servers
What: When a remote MCP server's OAuth flow needs to refresh tokens, the server's OAuth metadata is now cached on the client object instead of re-fetched on each refresh.

Details:
- `this._metadata` stores the result of the initial metadata discovery
- Subsequent token refresh attempts reuse the cached value, falling back to a live fetch only if the cache is empty

Evidence: `this._metadata` assignment in class `F36` (search for `"Failed to discover OAuth metadata"`)


### Tool Input Parameter Aliasing
What: A new feature-flagged mechanism (`tengu_tool_input_aliasing`) allows tool definitions to declare `inputParamAliases`, mapping deprecated parameter names to current ones before input validation.

Details:
- If enabled, `qX1` rewrites incoming tool input keys using the tool's `inputParamAliases` map before the schema validation step runs
- Only aliases to a new key if the new key is not already present in the input
- Emits `tengu_tool_input_alias_applied` telemetry listing the applied renames

Evidence: New function `qX1` gated on `"tengu_tool_input_aliasing"` (search for `"inputParamAliases"`)


### Several MCP and Agent Tools Marked as Deferred
What: Multiple internal tools now carry `shouldDefer: true`, making them eligible to be deferred (loaded on demand) rather than always sent to the model.

Details:
- Tools affected include: TaskCreate, TaskUpdate, TaskGet, BashTask (stop), AgentMessage (send), LSPTool, AgentCreate/TeamCreate

Evidence: `shouldDefer: !0` additions across tool definitions (search for `"shouldDefer"`)


### Untracked File Capture for Issue Reporting
What: New helpers collect untracked files from a git repository to include in issue/patch reports sent to remote sessions.

Details:
- `Zq1` runs `git ls-files --others --exclude-standard`, skips binary files (detected by null bytes), and respects per-file and total size limits (`f97` = 500 MB per file, `T97` = 5 GB total)
- `P05` assembles a complete patch context: remote base SHA, diff from base, and untracked file contents; falls back to `HEAD-only` mode for shallow clones or repos without a remote

Evidence: New functions `Zq1`, `P05`, `E97` (search for `"Untracked file capture"`)

## Bug Fixes

- Fixed file suggestion hook (`gy8`) skipping hooks when `disableAllHooks` was set, by routing through the unified `sc6()` check instead of reading the setting directly. (search for `"disableAllHooks"`)
- Fixed permission check for write operations to now pass `suggestions` to the decision response, enabling the UI to show alternative allowed paths when a write is denied. (search for `"suggestions: Jl6"`)
- Fixed the `mcp-cli` mode case being incorrectly handled in the permission mode check; it is now removed from the switch statement since it is not a valid interactive mode. (search for `"mcp_cli_mode"`)
- Fixed marketplace file parse errors to include the file path in the error message rather than rethrowing the raw parse error. (search for `"Failed to parse marketplace file at"`)
- Fixed extra usage rate limit message for `org_level_disabled_until` from "extra usage temporarily unavailable" to "extra usage spending cap reached". (search for `"spending cap reached"`)
- Fixed CLAUDE.md loading to skip excluded files before resolving symlinks, avoiding unnecessary filesystem access. (search for `"claudeMdExcludes"`)
- Fixed an early return in the model server content streaming path that caused an empty content callback to be skipped rather than reporting zero bytes read. (search for `"bytesRead"` near `"bytesTotal"`)

## In Development


### Moth Copse (Relevant Memories in Context) [In Development]
What: Infrastructure for injecting "relevant memories" based on the current user message into the context window, gated behind the feature flag `tengu_moth_copse`.

Status: Feature-flagged and recently partially disabled

Details:
- The `A0Y` (was `txY`) context builder previously had a conditional block that invoked `WuY` to find relevant memories when `tengu_moth_copse` was enabled; this block has been removed in v2.1.48
- The new `tC4` function checks `tengu_moth_copse` and invokes `G0Y` (memory relevance search) against the last user message
- The feature is still reachable through the `tC4` path; the context builder path was removed/refactored

Evidence: Feature flag `"tengu_moth_copse"` (search for `"tengu_moth_copse"`)


### Pebble Leaf Pruning [In Development]
What: An alternative algorithm for pruning orphaned leaf messages from the transcript tree, behind the feature flag `tengu_pebble_leaf_prune`.

Status: Feature-flagged

Details:
- When enabled, the pruning pass first builds a set of parent UUIDs from all messages, then only adds leaf nodes (messages with no children) to the pruning candidate set
- The existing algorithm (without the flag) adds all ancestor UUIDs unconditionally

Evidence: Feature flag `"tengu_pebble_leaf_prune"` in `nY6` (search for `"tengu_pebble_leaf_prune"`)


### Tool Input Aliasing [In Development]
What: Mechanism for tools to declare deprecated input parameter names that are silently remapped to current names before validation.

Status: Feature-flagged (`tengu_tool_input_aliasing`)

Details:
- Infrastructure is fully in place; the flag is checked at `qX1` call time
- No built-in tools currently use `inputParamAliases` in the diff

Evidence: `"tengu_tool_input_aliasing"` feature flag (search for `"inputParamAliases"`)
