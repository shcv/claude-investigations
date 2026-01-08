# Changelog for version 2.0.34

## Highlights
Version 2.0.34 introduces experimental MCP CLI tooling for direct interaction with Model Context Protocol servers, adds a Skills API for skill management, implements passive LSP diagnostics collection, and enhances sandbox configuration with granular override controls.

### MCP CLI Command Interface
**What:** A new command-line interface for interacting with MCP (Model Context Protocol) servers directly from bash commands within Claude Code sessions.

**How to use:**
```bash
# Discover available MCP servers and tools
mcp-cli servers                        # List all connected MCP servers
mcp-cli tools [server]                 # List available tools
mcp-cli grep "weather"                 # Search tools by keyword

# Get tool schema (REQUIRED before calling any tool)
mcp-cli info slack/search_private      # View JSON schema for parameters

# Invoke MCP tools
mcp-cli call slack/search_private '{"query": "mentions", "max_results": 10}'

# Use stdin for complex JSON
mcp-cli call api/send_request - <<'EOF'
{
  "endpoint": "/data",
  "headers": {"Authorization": "Bearer token"}
}
EOF
```

**Details:**
- Enabled via `ENABLE_EXPERIMENTAL_MCP_CLI` environment variable
- Claude must call `mcp-cli info` before any `mcp-cli call` to check parameter schemas
- Includes full Commander.js CLI with multiple subcommands
- Automatically tracked with telemetry event `tengu_mcp_cli_command_executed`
- **Evidence**: Command parser `Re()` at line 3935, handler `so2()` at line 493008, entry point check at line 493024 in `pretty-v2.0.34.js`

### Skills API Client
**What:** New API client for managing Claude skills through the beta API.

**How to use:**
```javascript
// Skills are managed through the beta client
const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

// Create a skill
await client.beta.skills.create({
  name: "my-skill",
  // ... skill configuration
}, { betas: ["skills-2025-10-02"] });

// Create a skill version
await client.beta.skills.versions.create(skillId, {
  // ... version configuration
}, { betas: ["skills-2025-10-02"] });

// List, retrieve, delete skills and versions
await client.beta.skills.list();
await client.beta.skills.retrieve(skillId);
await client.beta.skills.delete(skillId);
```

**Details:**
- Requires `skills-2025-10-02` beta header
- Full CRUD operations for skills and skill versions
- Accessed via `client.beta.skills` property
- API endpoints: `/v1/skills` and `/v1/skills/{id}/versions`
- **Evidence**: Class `BFA` at line 146202, class `Q2A` at line 146272, beta client integration at line 146346 in `pretty-v2.0.34.js`

### Passive LSP Diagnostics Collection
**What:** Automatic collection of diagnostics (errors, warnings, hints) from LSP servers and delivery as message attachments.

**Details:**
- LSP servers now send `textDocument/publishDiagnostics` notifications automatically
- Diagnostics are queued and attached to the next API request as `lsp_diagnostics` attachments
- Includes file URI, line ranges, severity levels (Error/Warning/Info/Hint), and diagnostic messages
- Handles multiple LSP servers with individual error tracking and retry logic
- New `saveFile` method added to LSP manager for `textDocument/didSave` notifications
- **Evidence**: Handler registration `lUQ()` at line 276542, diagnostic registration `dUQ()` at line 276467, severity mapper `WR6()` at line 276504, transformer `FR6()` at line 276518 in `pretty-v2.0.34.js`

### Sandbox Override Configuration
**What:** New settings UI to control whether commands can fall back to running outside the sandbox when sandbox restrictions prevent execution.

**How to use:**
```bash
# Access via /sandbox command in interactive mode
# Choose from:
# 1. "Allow unsandboxed fallback" - Commands retry outside sandbox if blocked
# 2. "Strict sandbox mode" - All commands must run in sandbox or be excluded
```

**Details:**
- Separate from the main sandbox enable/disable setting
- Can be locked by policy settings from higher-priority configuration sources
- Status displayed in `/sandbox` command output (e.g., "sandbox enabled, fallback allowed")
- New API methods: `areUnsandboxedCommandsAllowed()`, `areSandboxSettingsLockedByPolicy()`, `setSandboxSettings()`
- Documentation link: docs.claude.com/en/docs/claude-code/sandboxing#configure-sandboxing
- **Evidence**: Component `bn2()` at line 465885, policy check `Fs2()` at line 472000 in `pretty-v2.0.34.js`

### Enhanced Wide Character Rendering
**What:** Improved handling of emoji and CJK characters in terminal output through explicit width tracking in the screen buffer.

**Details:**
- Cell objects now include explicit `width` property (0 for normal, 1 for wide, 2/3 for placeholder)
- Automatic insertion of placeholder cells when writing wide characters
- Renderer skips placeholder cells to prevent double-rendering artifacts
- Width-aware cursor movement (advances 2 positions for wide characters)
- Fixes rendering bugs where placeholder cells were processed incorrectly
- **Evidence**: Enhanced cell type `pf9` at line 67236, width-aware write function `$P0()` at line 67208, placeholder skipping logic at lines 67852-67853 in `pretty-v2.0.34.js`

### Dual Telemetry System
**What:** Telemetry events now log to both Statsig and Segment (when enabled by feature gate).

**Details:**
- New feature gate `tengu_log_segment_events` controls Segment logging
- Synchronous logging via `ZA()` function, async via `uw()` function
- Separate formatters for each system: `sc2()` for Statsig (flattened strings), `rc2()` for Segment (structured objects)
- Parallel execution when both systems enabled for optimal performance
- Shared context builder `t01()` gathers environment, model, and session data
- Gate value cached to avoid repeated lookups
- **Evidence**: Dual logger `ZA()` at line 477386, async logger `uw()` at line 477389, context builder `t01()` at line 451726, gate checker `Lr2()` at line 477375 in `pretty-v2.0.34.js`

### Refactored Rendering Engine
**What:** Terminal rendering code reorganized for better maintainability and to support ink2 mode.

**Details:**
- Split `render()` into `render_v1()` and `render_v2()` methods
- Cleaner separation between legacy and new rendering paths
- Improved parameter passing (prevFrame explicitly passed instead of using instance state)
- Better handling of non-TTY output modes
- **Evidence**: Class `RG1` with split rendering methods at line 67663 in `pretty-v2.0.34.js`

### Process Metrics Collection
**What:** Enhanced telemetry with optional process-level metrics.

**Details:**
- New `processMetrics` field in telemetry context
- Included in both Statsig and Segment events when available
- Retrieved via `Lt5()` function
- Adds visibility into resource usage patterns
- **Evidence**: Process metrics in `t01()` at line 451726, formatter handling in `sc2()` at line 451751 and `rc2()` at line 451762 in `pretty-v2.0.34.js`

### MCP Bash Permission Handling
**What:** Improved permission checking for MCP tools invoked via bash commands.

**Details:**
- New command parser `Re()` detects `mcp-cli call` syntax in bash commands
- Permission check function `Bg8()` validates MCP tool access before execution
- Prevents bash command splitting from bypassing MCP permissions
- Returns appropriate deny/ask/allow behavior with suggestions
- **Evidence**: Parser `Re()` at line 3935, permission check `Bg8()` at line 212208 in `pretty-v2.0.34.js`

### Environment Context Refactoring
**What:** Telemetry environment context gathering extracted into reusable function.

**Details:**
- New `Nt5()` async function collects platform, runtime, and environment data
- Includes: platform, arch, Node version, terminal type, package managers, runtimes, deployment environment, CI detection, WSL version
- Shared between Statsig and Segment telemetry
- Eliminates code duplication from previous inline implementation
- **Evidence**: Function `Nt5()` at line 451680 in `pretty-v2.0.34.js`

### Session ID Handling
**What:** Session ID now uses environment variable when available for better tracking across processes.

**Details:**
- New `SQI()` function checks `CLAUDE_CODE_SESSION_ID` environment variable
- Falls back to generated session ID if not set
- Enables correlation of events across related processes
- **Evidence**: Function `SQI()` at line 483098 in `pretty-v2.0.34.js`

### Branch Tracking Analytics
**What:** New telemetry event to track forked conversation branches in chat history.

**Details:**
- Event `tengu_session_forked_branches_fetched` tracks branch statistics
- Metrics: total sessions, sessions with branches, max branches per session, average branches
- Only fires when at least one session has multiple branches (max > 1)
- Helps understand user exploration patterns
- **Evidence**: Function `f1I()` at line 474125 in `pretty-v2.0.34.js`

### Telemetry Architecture Refactoring
- Old `j1()` function replaced with `ZA()` (sync) and `uw()` (async)
- Old `Rs2()` Statsig logger replaced with `f00()` 
- Old `Os2()` Segment logger renamed to `sA0()` with updated helpers
- Context gathering, formatting, and logging now properly separated
- Feature gate system for conditional Segment logging

### LSP Manager Enhancement
- Added `saveFile` method to LSP manager for `textDocument/didSave` notifications
- Improved server initialization with automatic startup on first LSP manager initialization
- Better error handling and logging throughout diagnostic flow

### Version Bump
- Updated from v2.0.33 to v2.0.34
- **Evidence**: Version string at line 451680 in `pretty-v2.0.34.js`
