# Changelog for version 2.0.77


## Summary

This release focuses on internal performance improvements with new slow operation detection and diagnostics, enhanced OAuth authentication recovery, better enterprise MCP policy enforcement, and updated max token handling for Claude Sonnet 4 with the 1M context beta. Several large dependency libraries (AJV JSON Schema validator, terminal setup helpers) were removed and replaced with more efficient alternatives.


### EPIPE Error Handling for Piped Output
What: Claude Code now gracefully handles broken pipe (EPIPE) errors when output is piped to another process that closes early.

Usage:
```bash
claude -p "list files" | head -1  # No longer crashes if head closes early
```

Details:
- Prevents crashes when Claude Code's output is piped to a process that terminates before reading all output
- Automatically destroys stdout/stderr streams on EPIPE instead of throwing an uncaught error
- Improves CLI scripting reliability

Evidence: `HS0()` at line 519 (EPIPE handler, contains `"EPIPE"`)


### Enterprise MCP Exclusive Mode
What: Enterprises can now configure MCP servers in exclusive mode, preventing users from adding custom MCP servers.

Usage: Configured via enterprise policy. When active, users see:
```
Cannot add MCP server: enterprise MCP configuration is active and has exclusive control over MCP servers
```

Details:
- Allows enterprises to lock down MCP server configuration
- Users cannot add MCP servers via `/mcp` command or config files when active
- Provides clear error messaging about why server addition is blocked

Evidence: `jd()` at line 398745 (MCP server add function, contains `"enterprise MCP configuration is active and has exclusive control over MCP servers"`)


### Custom Betas Validation for API Users
What: API key users can now specify custom beta headers, with validation against an allowlist.

Details:
- Only the `context-1m-2025-08-07` beta is currently allowed
- Warnings are shown for disallowed beta headers
- OAuth users cannot use custom betas (server-controlled)

Evidence: `JrQ()` at line 140738 (beta validation, contains `"Custom betas are only available for API key users"`)


### Slow Operation Detection and Diagnostics
Performance monitoring has been added for operations that may cause UI lag or delays:

- `JSON.stringify`, `JSON.parse`, and `structuredClone` operations now log warnings when they take >200ms
- `fs.writeFileSync` operations include size information in slow operation warnings
- `execSync` shell commands are monitored for slow execution
- All slow operations are reported via telemetry for aggregate analysis

Evidence: `duA()` at line 3224 (slow operation wrapper, contains `"[SLOW OPERATION DETECTED]"`)


### OAuth 401 Error Recovery
What: OAuth authentication now attempts to recover from 401 errors by re-reading credentials from the system keychain.

Details:
- When a 401 error occurs, Claude Code checks if the keychain has newer credentials
- If different credentials are found, they're used without requiring re-authentication
- Reduces unnecessary login prompts when tokens are refreshed externally
- Telemetry event: `tengu_oauth_401_recovered_from_keychain`

Evidence: `C1B()` at line 146443 (OAuth recovery, contains `"tengu_oauth_401_recovered_from_keychain"`)


### Claude Sonnet 4 with 1M Context Beta Support
What: The max tokens calculation now correctly handles Claude Sonnet 4 models using the 1M context beta.

Details:
- Previously only models with `[1m]` in the name got 1M max tokens
- Now also applies when `context-1m-2025-08-07` beta header is used with claude-sonnet-4 models
- Enables proper token limits for Sonnet 4 + 1M context combinations

Evidence: `R$()` at line 1818 (max tokens calculation, contains `"claude-sonnet-4"` and `T8A`)


### Filesystem Operations Logging Improvements
What: All filesystem operations now include descriptive context in debug logs.

Details:
- Operations like `readFileSync`, `writeFileSync`, `symlinkSync` now log with path information
- Improved format: `readFileSync(/path/to/file)` instead of just `readFileSync`
- Helps diagnose file-related issues in debug mode

Evidence: `CQ` variable at line 2388 (filesystem wrapper, contains descriptive operation strings)


### Plugin Hooks Cleanup
What: Added function to cleanly remove plugin-sourced hooks while preserving non-plugin hooks.

Details:
- `sy0()` function filters out hooks that have a `pluginRoot` property
- Enables proper plugin unloading without affecting built-in hooks
- Improves plugin lifecycle management

Evidence: `sy0()` at line 2270 (plugin hooks cleanup, filters by `"pluginRoot"`)


### Configurable Timeout Validator
What: New timeout configuration validator with sensible defaults and caps.

Details:
- Default: 30000ms (30 seconds)
- Maximum: 150000ms (2.5 minutes)
- Invalid values fall back to default with a warning
- Values exceeding maximum are capped with a notice

Evidence: `sx0()` at line 1741 (timeout validator, contains `"Invalid value"`, `"Capped from"`)

## Bug Fixes

- Fixed potential crash when OAuth tokens expire and keychain has updated credentials (`C1B()` at line 146443)
- Improved handling of model region prefixes (us, eu, apac, global) for Bedrock deployments (`Ad1()` at line 139167, `MoQ()` at line 139171)

## Internal Changes

The following changes are internal and don't affect user-facing functionality:


### Removed Libraries/Code
- **AJV JSON Schema Validator**: The large AJV library (~5000+ lines) has been removed. Schema validation now uses a different approach (likely Zod which was already present)
- **Terminal Setup Helpers**: Functions for configuring iTerm2, WezTerm, Ghostty, and Kitty Shift+Enter bindings have been removed from the diff (the `/terminal-setup` command still exists but implementation may have changed)
- **Keychain Delete Sync**: The synchronous `UsQ()` keychain delete function was replaced with an async version `J1B()`


### Added Libraries
- **YAML Parser**: A full YAML parsing library has been bundled (likely for reading `.yml`/`.yaml` config files)


### Refactoring
- Zod schema validation error messages now use `.issues` instead of `.errors` property
- Cache invalidation function `fl()` added for OAuth credential cache
- Various dependency updates (google-auth-library version string changes)
