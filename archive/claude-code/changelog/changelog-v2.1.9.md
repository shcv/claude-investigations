# Changelog for version 2.1.9


## Summary

This release adds Opus 4.5 upgrade nudges for users on older Opus models, introduces a new `plansDirectory` setting to customize where plan files are stored, enhances MCP tool search with better scoring for server and action names, and includes new telemetry for SSL/TLS certificate configurations. Internal improvements include a new HybridTransport for remote sessions with retry logic.

### Plans Directory Configuration
**What**: You can now specify a custom directory for plan files via the `plansDirectory` setting.

**Usage**:
```json
{
  "plansDirectory": "./plans"
}
```

**Details**:
- The directory must be within the project root
- If not specified, plans are stored in the default session directory
- Useful for keeping plan files in version control alongside your project

**Evidence**: `jN()` at line 300782 (plans directory resolution, contains `"plansDirectory must be within project root"`)

### Opus 4.5 Upgrade Nudge
**What**: Users on older Opus 4.x models (Opus 4.0, 4.1) now see a notification suggesting they upgrade to Opus 4.5.

**Details**:
- Only shows for first-party users (claude.ai)
- Displays: "Opus 4.5 is available and is our best model for coding"
- Includes a hint to use `/model` command to upgrade
- Nudge appears for ~10 seconds then dismisses

**Evidence**: `vN9()` at line 535826 (opus upgrade nudge, contains `"opus-45-upgrade-nudge"`, `"Opus 4.5 is available and is our best model for coding"`)

### ENABLE_TOOL_SEARCH Percentage Control
**What**: The `ENABLE_TOOL_SEARCH` environment variable now supports percentage-based control with the `auto:N` syntax.

**Usage**:
```bash
ENABLE_TOOL_SEARCH=auto:50  # 50% tool search probability
ENABLE_TOOL_SEARCH=auto:0   # Equivalent to "tst" (always tool search)
ENABLE_TOOL_SEARCH=auto:100 # Equivalent to standard/mcp-cli modes
```

**Details**:
- Values are clamped between 0-100
- Invalid values log a warning and fall back to defaults
- Provides fine-grained control over tool search behavior

**Evidence**: `DX0()` at line 292496 (auto percentage parser, contains `"Invalid ENABLE_TOOL_SEARCH value"`, `"expected auto:N where N is a number"`)

### Enhanced MCP Tool Search Scoring
Tool search now provides better relevance scoring for MCP tools by parsing server and action names from the tool name format (`mcp__server__action_name`).

**Details**:
- Server name exact matches: +12 points
- Server name partial matches: +6 points
- Action name exact matches: +8 points
- Action name partial matches: +4 points
- Full name matches: +3 points
- Description word boundary matches: +2 points

**Evidence**: `EQ7()` at line 428976 (MCP tool name parser, uses regex `mcp__`)

### HybridTransport for Remote Sessions
Remote sessions now use a hybrid transport that sends messages via HTTP POST with WebSocket fallback, improving reliability.

**Details**:
- Implements retry logic with exponential backoff (up to 10 attempts)
- Converts WebSocket URLs to HTTP POST endpoints for `events` API
- Client errors (4xx except 429) are not retried
- Maximum backoff delay of 8 seconds

**Evidence**: `Yv0` class at line 542866 (HybridTransport, contains `"HybridTransport: POST URL"`, `"cli_hybrid_transport_initialized"`)

### Staging Environment Detection
Sessions can now properly detect and connect to staging environments (staging.claude.ai) for internal testing.

**Evidence**: `Q65()` at line 298312 (staging detection, contains `"_staging_"`, `"https://staging.claude.ai"`)

### SSL/TLS Certificate Telemetry
New telemetry tracks SSL/TLS certificate configuration for debugging connectivity issues.

**Details**:
- Detects `NODE_EXTRA_CA_CERTS` environment variable
- Detects `CLAUDE_CODE_CLIENT_CERT` for mTLS
- Detects `--use-system-ca` and `--use-openssl-ca` Node.js options

**Evidence**: `wT7()` at line 545895 (certificate telemetry, contains `"has_node_extra_ca_certs"`, `"has_use_system_ca"`)

### Session Phase Status Tracking
Internal support for tracking session phases: planning, implementing, reviewing, verifying.

**Evidence**: `Vd5()` at line 373496 (phase status mapper, contains `"planning"`, `"implementing"`, `"reviewing"`, `"verifying"`)

### Improved Screen Buffer Reuse
The terminal rendering system now reuses screen buffers for better memory efficiency, reducing allocations during rendering.

**Evidence**: `C3B()` at line 187260 (resetScreen function, screen buffer management)

## Bug Fixes

- Fixed MCP client cleanup to properly handle timeouts during disconnect (`bd()` at line 296688, 5-second timeout for cleanup)
- Improved screen array handling to prevent resizing issues in edge cases

### /btw Side Questions [In Development]

**What**: Infrastructure for asking quick side questions without interrupting the main conversation.

**Status**: Stubbed - `isEnabled: () => !1` (always returns false)

**Details**:
- Command exists: `/btw <question>`
- Full UI component exists with loading spinner
- Error handling for failed responses
- Dismiss with Enter or Escape
- The command type changed from `"local"` to `"local-jsx"` (JSX component rendering)

**Evidence**: `eB7` at line 437798 (btw command, `isEnabled: () => !1`, contains `"/btw"`, `"Answering..."`)
