# Changelog for version 2.0.42

## Highlights
Version 2.0.42 introduces bidirectional LSP communication support, enhanced GitHub authentication, and improved LSP workspace initialization. The LSP system can now respond to server requests (not just send them), GitHub CLI authentication is more robust with JSON output parsing, and LSP servers receive proper workspace context from initialization.

### LSP Request Handler Support
**What:** LSP servers can now send requests back to Claude Code and receive responses, enabling full bidirectional communication required by the LSP protocol.

**How it works:**
The LSP client now supports `onRequest()` to handle incoming requests from language servers, complementing the existing `onNotification()` for one-way messages. This enables proper LSP protocol compliance.

**Details:**
- Added `onRequest()` method to LSP client wrapper at `y$Q() at line 283672`
- Implemented request handler queueing system (variable `X = []` at line 283555) for handlers registered before connection establishment
- Exposed `onRequest` in high-level LSP server API at `x$Q() at line 283868`
- Immediately utilized to handle `workspace/configuration` requests at line 286293, returning `null` for all configuration items (safe default)
- **Evidence**: `y$Q() at line 283547-283803` (new LSP client), `x$Q() at line 283893` (exposed API)

**Why it matters:** Many LSP servers (TypeScript, Python, etc.) require clients to respond to `workspace/configuration` requests during initialization. Without this, some language servers may fail to initialize properly or operate with reduced functionality.

### GitHub App Installation Validation
**What:** Background tasks now verify that the Claude GitHub app is installed on the repository before allowing execution.

**How to use:**
When initiating background tasks in a GitHub repository, Claude Code automatically checks if the Claude app is installed. If not, you'll receive a clear error message with installation link.

**Details:**
- New validation function `KT2()` at line 426828 checks app installation via API endpoint `/api/oauth/organizations/{orgId}/code/repos/{owner}/{repo}`
- GitHub repository detection function `Fb()` at line 426624 extracts owner/repo from git remote URL
- Added fourth validation check to background task prerequisites (alongside login, remote environment, and git repo checks) in `TT2() at line 427717`
- New error type `github_app_not_installed` with user-friendly message and installation link at line 427972
- **Evidence**: `KT2() at line 426828`, `TT2() at line 427717`, `Fb() at line 426624`

**Why it matters:** Ensures background tasks have proper GitHub integration permissions before execution, preventing mysterious failures when app permissions are missing.

### Enhanced GitHub Authentication Detection
**What:** GitHub CLI authentication detection now uses JSON output parsing for more reliable credential extraction.

**How it works:**
The `gh auth status` command is now called with `--active --json hosts` flags, parsing structured JSON instead of text output. This improves reliability across different `gh` CLI versions and configurations.

**Details:**
- New function `Xi5()` at line 426046 uses `gh auth status --active --json hosts` for structured output
- Parses JSON response to extract `hosts` object and active account login
- Handles multiple GitHub hosts (github.com, Enterprise instances) by iterating through host entries
- Replaces old shell parsing approach that used `sh -c "gh auth status 2>&1 | head -n 1"` and regex matching
- **Evidence**: `Xi5() at line 426046-426076`

**Why it matters:** More robust GitHub authentication detection prevents false negatives and works consistently across different GitHub CLI versions and Enterprise configurations.

### Git User Email Detection
**What:** Added function to retrieve git user email from git configuration.

**How to use:**
Automatically detects `git config user.email` value when linking VCS accounts.

**Details:**
- New function `Wi5()` at line 426065 executes `git config --get user.email`
- Integrated with VCS account linking in `QT2()` at line 426023, now includes `git_user_email` field
- Used to associate git commits with Claude Code user accounts
- **Evidence**: `Wi5() at line 426065`, `QT2() at line 426023`

### LSP Workspace Initialization
**What:** LSP servers now receive proper workspace root information during initialization instead of null values.

**Details:**
- Changed `rootPath` from `null` to actual workspace folder path in LSP initialize request at `x$Q() at line 283755`
- Changed `rootUri` from `null` to `file://` URI of workspace folder at line 283756
- Improves backward compatibility with LSP servers that rely on deprecated `rootPath`/`rootUri` fields
- **Evidence**: `x$Q() at line 283750-283756`

**Why it matters:** Some language servers use the deprecated `rootPath` and `rootUri` fields for workspace detection. Providing actual values instead of `null` improves compatibility with older LSP implementations.

### Settings Update Error Handling
**What:** Plugin enable/disable operations now properly propagate errors to callers.

**Details:**
- Function `sQ0()` at line 489317 now captures and throws errors from `B2()` settings update
- Added error destructuring: `let { error: Z } = B2("userSettings", { enabledPlugins: G })`
- Throws error if settings update fails: `if (Z) throw Z;`
- **Evidence**: `sQ0() at line 489317-489323`

**Why it matters:** Previously, settings update failures could be silently ignored. Now callers can properly handle and report errors when plugin state changes fail.

### Plugin Hook Filtering
**What:** Function-type hooks are now filtered out when serializing plugin hooks.

**Details:**
- Function `Er2()` at line 472146 adds `.filter((Q) => Q.type !== "function")` to hook serialization
- Prevents function-type hooks from being included in serialized plugin configurations
- **Evidence**: `Er2() at line 472146-472151`

**Why it matters:** Function-type hooks cannot be serialized to JSON, so filtering them prevents serialization errors.

### Hook Type Handling
**What:** Hook execution now handles multiple hook types including callback and function types.

**Details:**
- Updated `vz()` function at line 472202 to handle four hook types: command, prompt, callback, and function
- Function `PBI()` at line 473700 executes function-type hooks with proper timeout and abort signal handling
- Callback hook execution in `jBI()` at line 473754 simplified with cleaner abort handling
- **Evidence**: `vz() at line 472202`, `PBI() at line 473700`, `jBI() at line 473754`

### LSP Definition Result Normalization
**What:** Go-to-definition results are now normalized to handle both Location and LocationLink formats.

**Details:**
- New helper functions `Ih2()` at line 441143 and `Qh2()` at line 441140 detect and convert LocationLink format
- Function `ds5()` at line 441543 normalizes LocationLink to Location format
- Updated `Yh2()` at line 441146 to handle mixed result arrays with both formats
- **Evidence**: `Ih2() at line 441143`, `Qh2() at line 441140`, `ds5() at line 441543`, `Yh2() at line 441146`

**Why it matters:** LSP spec allows servers to return either Location or LocationLink for definitions. Normalization ensures consistent handling regardless of format.

### Hook Matching Logic
**What:** Hook matching now considers both matcher name and hook event when finding applicable hooks.

**Details:**
- Function `Hr2()` at line 472167 updated to match hooks by matcher name first, then by hook criteria
- Supports empty matcher string for wildcard matching
- Returns full hook entry (not just `onMatch` callback) for more context
- **Evidence**: `Hr2() at line 472167-472185`

### MCP Configuration Lookup
**What:** Added helper functions for looking up MCP server configurations and resources by normalized names.

**Details:**
- Function `Te2()` at line 495603 retrieves MCP server config by name with fallback to normalized name
- Function `Pe2()` at line 495609 retrieves MCP resources by name with normalized name fallback
- Handles case-insensitive lookups via `normalizedNames` mapping
- **Evidence**: `Te2() at line 495603`, `Pe2() at line 495609`

### Environment Variable Telemetry
**What:** Added `claude_code_container_id` to telemetry payload when running in containerized environments.

**Details:**
- Function `Wp2()` at line 450308 now includes `claudeCodeContainerId` in telemetry
- Mapped to `claude_code_container_id` field at line 450398
- Sourced from `CLAUDE_CODE_CONTAINER_ID` environment variable
- **Evidence**: `Wp2() at line 450398-450399`

### Bash Command Execution in Plugins
**What:** Simplified plugin bash command execution by removing plugin root directory injection.

**Details:**
- Function `cc()` at line 432214 no longer wraps commands with `An5()` to inject `CLAUDE_PLUGIN_ROOT`
- Commands now execute directly without environment variable manipulation
- **Evidence**: `cc() at line 432214-432236`

### Callback Hook Abort Handling
**What:** Improved abort signal handling in callback hooks to prevent unhandled promise rejections.

**Details:**
- Function `jBI()` at line 473754 simplified to let errors propagate naturally
- Removed try-catch block that was catching and converting abort errors
- Abort signals now handled by upstream code
- **Evidence**: `jBI() at line 473754-473794`

### Import Reorganization
- Consolidated `node:process` imports: Added `cwd as Xy0` at line 77734
- Consolidated `node:stream` imports: Added `Readable as Hs9` at line 87712
- Split `node:child_process` imports: Added `execSync as $UQ, spawn as eR6` at line 279661
- Reorganized `node:path` imports: Changed to `posix as O9I, win32 as VQ0` at line 482076
- Added specific imports: `join as K19, basename as w8I` from path at line 489603
- Added `PassThrough as p8I` from stream at line 490866
- Added `homedir as G6I` from node:os at line 492712

### Variable Renaming (Minification)
Multiple variables renamed due to code minification:
- `Ev0` → `OUB` (TodoWrite tool description)
- `JLQ` → `y$Q` (LSP client wrapper)
- `cl5` → `Xi5` (GitHub auth detection)
- `An5` → (removed, plugin env wrapper)
- `Pi2` → `Er2` (plugin hook serializer)
- `Dt` → `vz` (hook type extractor)
- `FLQ` → `x$Q` (LSP server manager)
- `WT2` → `QT2` (VCS account linker)
- `aQ0` → `sQ0` (plugin enabler)
- `_T2` → `TT2` (background task validator)
- `$BI` → `jBI` (callback hook executor)
- `Qh2` → `Yh2` (definition result formatter)
- Various function identifiers changed due to obfuscation
