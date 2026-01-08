# Changelog for version 1.0.116

## Highlights
Version 1.0.116 introduces reverse search history (Ctrl+R) for the interactive prompt, refactors the sandbox system with a centralized manager and flexible security policies, and adds support for environment-specific OAuth credentials to prevent developers from accidentally overwriting production tokens.

### Reverse Search History (Ctrl+R)
**What:** Interactive command history search similar to bash's reverse-i-search

**How to use:**
```bash
# In the interactive prompt, press Ctrl+R
# Type your search query - matches appear from command history
# Press Ctrl+R again to cycle through matches
# Press Enter to execute, Escape/Tab to accept without executing
```

**Details:**
- Displays "bck-i-search: " prompt when active
- Shows "failing bck-i-search: " when no matches found
- Searches through full command history including pasted content
- Ctrl+C cancels and restores previous input
- **Evidence**: `YNB() at line 429227`, `ZW5() at line 429311`

### Environment-Specific OAuth Credentials
**What:** Separate OAuth credential storage for local development vs production

**How to use:**
```bash
# Production credentials (default)
# Stored in: ~/.claude.json

# Local development credentials
export USE_LOCAL_OAUTH=1
# Stored in: ~/.claude-local-oauth.json
```

**Details:**
- Prevents accidentally overwriting production OAuth tokens during development
- Separate keychain entries: "Claude Code" vs "Claude Code-local-oauth"
- Configuration files: `.claude.json` (prod) or `.claude-local-oauth.json` (local)
- Infrastructure for staging environment included but not yet active
- **Evidence**: `Uo1() at line 339682`, `KZ9() at line 339686`, `uJ() at line 339696`

### Network Permission Session Memory
**What:** Remember network access decisions for the current session

**How to use:**
```bash
# When prompted for network access outside sandbox:
# - "Yes" - Allow once
# - "Yes, and allow accessing host:port for this session" - Remember for session
# - "No, and disable accessing host:port for this session" - Block for session
```

**Details:**
- Reduces repetitive permission prompts for trusted hosts
- Session-scoped - resets when Claude Code restarts
- Works with sandbox network restrictions
- **Evidence**: `pNB() at line 431799`, `Bx6() at line 374794`

### Sessions API Integration (Feature-Flagged)
**What:** New backend API for fetching session events and metadata

**Details:**
- Currently disabled by feature flag (`YD1()` returns false)
- Uses `/v1/sessions/` endpoints instead of `/api/oauth/`
- Supports fetching session events for replay capability
- New data structure with `session_context.sources` and `session_context.outcomes`
- Will enable enhanced teleport functionality when activated
- **Evidence**: `P55() at line 413749`, `S55() at line 413999`, `j55() at line 413991`

### Refactored Sandbox System
**What:** Complete architectural overhaul of the sandboxing implementation

**Key Changes:**
- Centralized sandbox manager with clean API (`hV` object at line 374998)
- New configuration model: `allowAllExcept` (blacklist) vs `denyAllExcept` (whitelist)
- Network deny-lists alongside allow-lists for more granular control
- macOS sandbox profiles now use deny-by-default security model
- Recommended defaults for common development tools (npm, cargo, yarn, etc.)
- Dynamic permission callbacks for interactive network access control
- **Evidence**: `wBB() at line 374755`, `Zx6() at line 374844`, `DBB() at line 374642`

**Migration Notes:**
- Existing sandbox configurations continue to work
- New `includeRecommendedDefaults` option automatically allows access to common tools
- Deny-by-default macOS profiles are more secure but may require configuration updates

### Enhanced Model Validation Errors
**What:** More specific error messages when model validation fails

**Details:**
- Distinguishes between "model not found", "authentication failed", and "network error"
- Provides actionable error messages instead of generic failures
- Better parsing of API error responses
- **Evidence**: `yJ5() at line 436574`

### Optimized Editor Selection
**What:** Editor detection is now memoized for better performance

**Details:**
- Checks `VISUAL` and `EDITOR` environment variables
- Falls back to ["code", "vi", "nano"] in order
- Result is cached to avoid repeated filesystem checks
- **Evidence**: `Cf1 at line 404874` (previously `Jf1() at line 404673` in v1.0.115)

### Improved Session Resume Messages
**What:** Better error handling for session resume operations

**Details:**
- Shows "Session resumed" (info) on success
- Shows "Session resumed without branch: [error]" (warning) on partial failure
- Uses formatted error messages when available
- **Evidence**: `bzB() at line 413552` (previously `o65() at line 413908` in v1.0.115)

### Sandbox Configuration Deep Cloning
**What:** Prevents mutation of original sandbox configuration

**Details:**
- Uses deep clone when processing sandbox config
- Prevents unexpected side effects when adding recommended defaults
- **Evidence**: `EBB.cloneDeep(A) at line 374849` in `Zx6()`

### Renamed Functions and Variables
- OAuth config selector: `D6()` → `L4()`
- Config file path: `bJ()` → `uJ()`
- OAuth configs: `HS9` → `pPA`, `DS9` → `gS9`, `fPA` → `iPA`
- Sandbox functions: `GBB()` → `wBB()`, `JBB()` → `Zx6()`, `FBB()` → `Ix6()`
- Linux wrapper: `YBB()` → `zBB()`

### Refactored Session Memory
- Session memory config: `bd5()` → `cp5 object`
- Session memory processor: `_$3` → `E_3`
- Now uses agent definition pattern for consistency

### OAuth Configuration Structure
- Added `OAUTH_FILE_SUFFIX` field to all OAuth configs
- Production: `OAUTH_FILE_SUFFIX: ""`
- Local: `OAUTH_FILE_SUFFIX: "-local-oauth"`

## Notes

- The Sessions API integration is implemented but disabled by feature flag
- Sandbox recommended defaults include paths for npm, yarn, pnpm, cargo, rustup, homebrew
- Environment-specific OAuth credentials prevent common development workflow issues
- Reverse search history uses React hooks for state management in the terminal UI
