# Changelog for version 2.0.10

## Highlights

Version 2.0.10 introduces intelligent shell completion for Bash commands, MCP server management in the command palette, enhanced plugin error tracking, and several improvements to model switching and telemetry handling. The release also includes internal rendering system refactoring for better maintainability.

### Shell Completion Support
**What:** Added intelligent tab-completion for bash and zsh shells when typing commands in the Bash tool
**How to use:**
While typing a command in the Bash tool, press Tab to see completion suggestions for:
- Commands (e.g., `git st` → `git status`)
- Files and directories (with trailing `/` for directories)
- Shell variables (for inputs starting with `$`)

**Details:**
- Automatically detects your shell type (bash or zsh) from `$SHELL` environment variable
- Context-aware completion: determines whether you're typing a command, file path, or variable based on cursor position
- Bash completion uses `compgen -c` (commands), `compgen -f` (files), `compgen -v` (variables)
- Zsh completion uses native zsh parameter and command arrays
- Limited to 100 suggestions per request for performance
- **Evidence**: `M0Q()` at line 420086, `wn5()` at line 420018, `qn5()` at line 420051, `En5()` at line 420059, `Nn5()` at line 420067 in v2.0.10

### MCP Server Toggling in Command Palette
**What:** MCP servers now appear in the command palette and can be toggled on/off with a keystroke
**How to use:**
```bash
# Open command palette (typically Ctrl+P or Cmd+P)
# Type server name to filter
# Press Enter to toggle server on/off
```

**Details:**
- Servers are displayed with visual indicators: `✓` (enabled) or `○` (disabled)
- Format: `[mcp] server-name` with description `enabled (⏎ to toggle)`
- The `ide` server is excluded from the list
- Filtering works on server names (case-insensitive)
- Toggle action immediately enables/disables the server
- **Evidence**: `On5()` at line 420158 in v2.0.10 (was empty array stub `bF5()` at line 419342 in v2.0.9)

### Model Switching from Plan Mode
**What:** Claude can now suggest switching to a different model when exiting plan mode
**How to use:**
When Claude presents a plan and exits plan mode, it may automatically switch to a more appropriate model based on task complexity. The model choice is shown in the status display.

**Details:**
- New `model` parameter in ExitPlanMode tool schema
- Session-scoped model override via `mainLoopModelForSession` state variable
- Session override takes precedence over base model setting
- Status command shows: `Current model: <model> (session override from plan mode)` when active
- Base model remains unchanged for future sessions
- **Evidence**: `bY7` schema at line 416861, `mainLoopModelForSession` state at line 448805 in v2.0.10 (did not exist in v2.0.9)

### Telemetry Flush on Logout
**What:** Telemetry data is now properly flushed when logging out, with configurable timeout
**How to use:**
Set the `CLAUDE_CODE_OTEL_FLUSH_TIMEOUT_MS` environment variable to control flush timeout (default: 5000ms):
```bash
export CLAUDE_CODE_OTEL_FLUSH_TIMEOUT_MS=10000
claude
```

**Details:**
- New `DEB()` async function handles telemetry flushing with timeout protection
- Default timeout is 5000ms (vs 1000ms for shutdown)
- Uses `Promise.race()` to enforce timeout
- Flushes both trace provider and metrics provider
- Logs success/timeout/error messages at appropriate levels
- Integrated into logout flow via `IL0()` function
- **Evidence**: `DEB()` at line 398367 in v2.0.10 (did not exist in v2.0.9)

### Dynamic Environment Selection
**What:** Environment providers are now fetched dynamically from the API instead of using hardcoded values
**How to use:**
This happens automatically when creating remote sessions. The first available environment is selected and logged.

**Details:**
- New API endpoint: `/v1/environment_providers`
- Fetches available environments with authentication headers
- Validates that environments are available before session creation
- Logs selected environment: `Selected environment: <id> (<name>)`
- 15-second timeout for API request
- Replaces hardcoded environment ID `env_011CSUkSjSxeWzWtatWym6Yn`
- **Evidence**: `mMB()` at line 404246 in v2.0.10 (different function in v2.0.9)

### Dynamic Configuration Caching
**What:** Statsig dynamic configurations are now cached in application state for faster access
**How to use:**
This is automatic. Config values are returned immediately from cache while fresh values are fetched in the background.

**Details:**
- New `cachedDynamicConfigs` object in state stores config values by key
- `B2Q(configName, defaultValue)` retrieves cached value immediately, fetches fresh value asynchronously
- `Q2Q(configName)` clears a specific cached config
- Reduces repeated API calls to Statsig
- Improves initial render performance
- **Evidence**: `cachedDynamicConfigs` at line 440962, `B2Q()` at line 441924, `Q2Q()` at line 441937 in v2.0.10 (did not exist in v2.0.9)

### Enhanced Plugin Error Tracking
**What changed:** Plugin loading failures are now tracked individually with structured error information instead of failing silently

**Details:**
- New `errors` array in plugins state stores error details with source attribution
- Individual try-catch blocks around commands, agents, and hooks loading prevent cascading failures
- Error objects include `source` field: `"plugin-commands"`, `"plugin-agents"`, `"plugin-hooks"`, or `"plugin-loading"`
- Error count included in startup logs: `Loaded plugins - ... Errors: ${count}`
- If one plugin component fails to load, others still attempt to load
- **Evidence**: `ad1()` at line 423922, errors field at line 448824 in v2.0.10 (errors ignored in `dMB()` at line 422999 in v2.0.9)

### External Editor Experience
**What changed:** External editors now launch in alternate screen buffer for cleaner terminal experience

**Details:**
- Added `AAQ()` function that wraps editor invocation with terminal screen switching
- Uses `\x1B[?1049h` to enable alternate screen before launching editor
- Uses `\x1B[?1049l` to restore original screen after editor exits
- Prevents editor output from polluting the Claude Code interface
- Cleans up temporary files after editor closes
- Supports `$VISUAL`, `$EDITOR`, and fallback editors (code, vi, nano)
- **Evidence**: `AAQ()` at line 422356 in v2.0.10 (screen buffer codes existed but not integrated in v2.0.9)

### Model Descriptions for Claude
**What changed:** Model options now include descriptions specifically tailored for Claude's decision-making

**Details:**
- Added `descriptionForModel` field to model configurations
- Sonnet 4.5: "the most powerful model. Generally best for most coding tasks"
- Sonnet (1M context): "with 1M context window - for long sessions with large codebases"
- Opus 4.1: "slower and more expensive than Sonnet, generally not recommended over Sonnet 4.5"
- Helps Claude make better model switching decisions when exiting plan mode
- **Evidence**: `kB4.descriptionForModel` at line 364157, `fL1.descriptionForModel` at line 364164, `wtA.descriptionForModel` at line 364173 in v2.0.10 (did not exist in v2.0.9)

### Environment Variable Parsing for MCP Commands
**What changed:** Enhanced validation of environment variable formats in `claude mcp add` command

**Details:**
- New `OI6()` function validates `KEY=value` format using regex `/^[A-Za-z_][A-Za-z0-9_]*=/`
- Validates variable names start with letter or underscore
- Variable names can contain letters, numbers, and underscores
- Prevents malformed environment variables from being added to MCP server configurations
- **Evidence**: `OI6()` at line 386305 in v2.0.10 (did not exist in v2.0.9)

### Installation Notification System
**What changed:** Installation messages and warnings are now managed through a centralized notification system

**Details:**
- New `N2Q()` hook processes installation messages on startup
- Messages categorized by priority: high (errors, action required), medium (path/alias issues), low (info)
- Messages displayed with appropriate colors: error (red), warning (yellow)
- Uses `XO()` to fetch installation messages
- Integrates with the notification queue system
- **Evidence**: `N2Q()` at line 425522 in v2.0.10 (did not exist in v2.0.9)

### Top-of-Feed Tips
**What changed:** Added configurable tips system that displays messages at the top of the conversation feed

**Details:**
- New `u_0()` component renders tips with color options: warning, error, or dimmed
- Tips cached in dynamic configs via `A2Q` config key
- `Ma5()` hook retrieves current tip using `B2Q()`
- Automatically invalidates cache when tip changes
- Default state: `{ tip: "", color: "dim" }`
- **Evidence**: `u_0()` at line 424743, `Ma5()` at line 424769 in v2.0.10 (did not exist in v2.0.9)

### Authentication Token Handling
**What changed:** Authentication functions now accept optional `allowedSettingSources` parameter for better source control

**Details:**
- `FO(allowedSettingSources)` function signature updated (was `VO()`)
- `he(allowedSettingSources)` function now accepts sources parameter
- `z4Q(allowedSettingSources)` ensures token availability (was `qjB()`)
- Allows filtering which settings sources can provide authentication tokens
- **Evidence**: `FO()` at line 440418, `Xr4()` at line 376327 in v2.0.10 (different signatures in v2.0.9)

### Debug Log Symlink Management
**What changed:** Latest debug log file now has a symlink for easier access

**Details:**
- New `G$Q` function creates `latest` symlink to current debug log
- `MH1()` returns debug log path (with `CLAUDE_CODE_DEBUG_LOGS_DIR` support)
- `On1()` returns path to `latest` symlink
- Symlink automatically updated on each run
- Located in debug directory: `~/.cache/claude-code/<workspace>/debug/latest`
- **Evidence**: `G$Q` at line 341114, `MH1()` at line 341106, `On1()` at line 341111 in v2.0.10 (did not exist in v2.0.9)

### Rendering System Architecture
**What changed:** Terminal rendering logic refactored into dedicated classes for better separation of concerns

**Details:**
- Main component class renamed from `MC1` to `OC1` and simplified
- New `dt1` class encapsulates all terminal output rendering logic
- Rendering function `ft1()` now uses closure pattern (was `giQ()`)
- Layout calculation moved into renderer (was separate `calculateLayout()` method)
- Frame state (`prevFrame`, `fullStaticOutput`) moved to `dt1.state`
- Buffer class renamed from `b41` to `f41` (functionally identical)
- Improved code organization and maintainability
- No user-visible changes
- **Evidence**: `OC1` at line 358599, `dt1` at line 357561, `ft1()` at line 357320 in v2.0.10 (was `MC1` at line 358357, inline rendering in v2.0.9)

### Model Status Display
**What changed:** `/model` command now shows session override information when active

**Details:**
- Displays both current model and base model when session override is active
- Format: `Current model: <bold>ModelName</bold> (session override from plan mode)\nBase model: <base-model>`
- Bold formatting applied to session override model name via `p1.bold()` / `HM()` function
- Helps users understand when plan mode has changed their model
- **Evidence**: `Yr5()` at line 431964 in v2.0.10 (was simpler `zz5()` at line 431016 in v2.0.9)

### Console Patching Behavior
**What:** Console.log and console.error now route through global error handlers instead of internal write methods

**Details:**
- Console output now logged via `r()` function with prefix: `console.log: <message>`
- Console errors now reported via `J1()` with error object and category code `Fa0` (292)
- Removed special case filtering for React error message "The above error occurred"
- More consistent error tracking and logging
- **Evidence**: `patchConsole()` in `OC1` at line 358722 in v2.0.10 (was different in `MC1.patchConsole()` at line 358579 in v2.0.9)

### Lodash Utility Functions
**What:** Added proper implementations of `trim`, `toNumber`, `debounce`, and `throttle` from lodash

**Details:**
- `b7Q()` (trim) - removes leading/trailing whitespace at line 335245
- `d7Q()` (toNumber) - converts values to numbers, handles special formats at line 335259
- `CXQ()` (debounce) - debounces function calls with leading/trailing options at line 336928
- `tXQ()` (throttle) - throttles function calls with configurable timing at line 337236
- These replace or supplement existing implementations for better compatibility
- **Evidence**: Added functions at lines 335238-337246 in v2.0.10 (partial or missing in v2.0.9)

### State Management Updates
- Added `mainLoopModelForSession: null` to initial state for session-scoped model overrides
- Added `errors: []` to plugins state structure
- Added `cachedDynamicConfigs: {}` to state for configuration caching
- Default state object renamed from `QH` to `Iz`

### Import Reorganization
- Added `import { cwd as w7A } from "node:process"` at line 357756
- Added `import { createHash as dt4, randomBytes as ct4 } from "crypto"` at line 379140
- Added `import { exec as yt5 } from "child_process"` at line 440404
- Added `import { PassThrough as a18 } from "stream"` at line 445653
- Removed `import NzQ from "stream"` (replaced with named import)
- Removed `import q6Q from "node:process"` (no longer needed)
- Removed `import { resolve as A5Q } from "path"` (renamed to `L5Q`)

### Function Removals
- Removed `giQ()` rendering function (replaced by `ft1()`)
- Removed `HnQ()` log factory (replaced by `dt1` class)
- Removed `DnQ` log factory wrapper (replaced by `dt1` class)
- Removed `c3A` and `p3A` React contexts for stdout/stderr (unused)
- Removed `MC1` class (replaced by `OC1`)
- Removed `wU1()` no-op function at line 361922
- Removed `i81()` and `o24()` opus plan detection functions
- Removed `js4()` auth header function (replaced by `Xr4()`)
- Removed `bF6()` and `jD0` static renderer class
- Removed `qD6()` editor helper (replaced by `$Y1()`)
- Removed `Eb()` model hook (replaced by `sb()`)
- Removed `bF5()` empty MCP server filter (replaced by `On5()`)
- Removed `dMB()` plugin loading (replaced by `ad1()`)
- Removed `RV5` opus plan welcome banner
- Removed `zz5()` simple model status (replaced by `Yr5()`)

### File Path Constants
- Log directory structure simplified in `cO` object (was `oJ`)
- Removed `debugLog()` function from path helpers (now uses `MH1()`)
- Added path separator constant `OK` at line 438815

### Thinking Feature Constants
- Added `Ny2 = "tmp-preserve-thinking-2025-10-01"` constant at line 376351


This changelog represents a careful analysis of v2.0.10, distinguishing between truly new features, enhancements to existing functionality, and internal refactoring. All claims have been verified against both versions with specific line number references.
