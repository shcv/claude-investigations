# Changelog for version 2.0.5

## Highlights

Version 2.0.5 adds extended thinking support for Claude Sonnet 4.5, allowing users to enable transparent reasoning via environment variables or configuration settings. This release also improves session persistence with deduplication and refines internal error handling.


### Extended Thinking Support for Sonnet 4.5

**What:** Claude Code now supports extended thinking mode when using Claude Sonnet 4.5, enabling more transparent reasoning for complex tasks.

**How to use:**
```bash
# Enable thinking via environment variable
MAX_THINKING_TOKENS=10000 claude

# Or configure in your settings file
# Set alwaysThinkingEnabled: true in your Claude Code settings
```

**Details:**
- Only available when using Claude Sonnet 4.5 model
- Can be controlled via `MAX_THINKING_TOKENS` environment variable (set to any positive integer to enable)
- Can be configured permanently via `alwaysThinkingEnabled` in settings
- Subject to Statsig feature gate `thinking_on_default` for gradual rollout
- Provides visible reasoning steps during Claude's problem-solving process
- **Evidence**: `hL1() at line 364041` in v2.0.5


### Session Persistence Deduplication

**What:** Session entries are now deduplicated before persistence, preventing redundant API calls when the same conversation entry is encountered multiple times.

**Details:**
- Uses UUID tracking to identify already-persisted entries
- Reduces unnecessary backend calls and potential conflicts
- Improves overall session handling performance
- **Evidence**: `K8B() at line 397234` in v2.0.5, modified from `QPB()` at line 23491 in v2.0.3


### Refined Tool Execution Messaging

**What:** Internal tool descriptions now emphasize "batch" execution rather than "parallel" execution, providing more accurate guidance for Claude's behavior.

**Details:**
- Updated Glob tool description from "in parallel" to "as a batch"
- Better reflects the actual execution model of tool calls
- Improves Claude's understanding of how multiple tool calls are processed
- **Evidence**: Glob tool description at line 12298 in v2.0.5


### Removed Obsolete Tool Concurrency Error

**What:** Eliminated the "tool use concurrency issues" error message that instructed users to run `/rewind` to recover conversations.

**Details:**
- The underlying API error condition (400 status for tool_use without tool_result blocks) is no longer expected
- Suggests server-side fix has been implemented
- Users will no longer encounter this specific error message
- **Evidence**: Error handling removed from `fk1()` at lines 23711-23720 in v2.0.3


### AWS Credential Handling Simplified

Removed workspace trust validation checks from AWS credential export and refresh functions, suggesting the security model has evolved to handle trust validation elsewhere in the codebase.

Evidence: `gH5() at line 23918` in v2.0.5, modified from `oH5()` at lines 23868-23876 in v2.0.3


### MCP Tool Token Instrumentation

Added telemetry for Model Context Protocol (MCP) tool usage, tracking both tool count and token consumption for optimization purposes.

Evidence: Token counting instrumentation at lines 446832-446838, new error code `Dn0 = 278` at line 339997 in v2.0.5


### OAuth Profile Fetching Streamlined

Removed extraction of `billingType` field from OAuth profile responses, as this field is no longer needed.

Evidence: `QN0()` at line 23631 in v2.0.3, field extraction removed in v2.0.5


### Code Modernization

- Removed unused `stream` module import
- Updated to use ES6 import for `cwd()` from `node:process`

Evidence: Stream import removed from line 338164 in v2.0.3; `cwd` import added at line 12278 in v2.0.5
