# Changelog for version 2.0.50

## Highlights

This release introduces cross-project conversation resume, a new MCP CLI endpoint for external tool integration, mandatory source citations for web search results, and human-friendly session naming using memorable word combinations like "fluffy-bouncing-bunny".

### Cross-Project Conversation Resume
**What:** View and resume conversations from any project directory, not just the current one.
**How to use:**
```bash
# Use /resume command and toggle "Show all projects" 
claude
> /resume
# Press the toggle key to switch between current project and all projects
```
**Details:**
- When enabled, scans `~/.claude/projects/` for all project directories
- Shows project path in conversation list for cross-project items
- For conversations from different directories, copies the resume command to clipboard
- Provides clear instructions: `cd /path/to/project && claude --resume <session-id>`
- **Evidence**: `FZ1()` at line 487757, `VZ1()` at line 504532 in v2.0.50

### MCP CLI Endpoint
**What:** HTTP REST API server for external tools to interact with Claude Code's MCP servers programmatically.
**How to use:**
```bash
# Enable the endpoint (enabled by default when Claude Code is running)
# External tools can make requests to localhost with bearer token auth

# Example: List available MCP servers
curl -X POST http://127.0.0.1:<port>/mcp \
  -H "Authorization: Bearer <secret>" \
  -H "Content-Type: application/json" \
  -d '{"command": "servers"}'

# Example: Call an MCP tool
curl -X POST http://127.0.0.1:<port>/mcp \
  -H "Authorization: Bearer <secret>" \
  -d '{"command": "call", "params": {"server": "myserver", "tool": "mytool", "args": {}}}'
```
**Details:**
- Supports commands: `servers`, `tools`, `info`, `call`, `grep`, `resources`, `read`
- Bearer token authentication with 32-byte random secret
- Localhost-only binding for security
- Endpoint info stored in `~/.claude/<workspace>.endpoint`
- Can be disabled via `ENABLE_MCP_CLI_ENDPOINT=false` environment variable
- **Evidence**: `class hX0` at line 515880 in v2.0.50

### Friendly Session Slug Names
**What:** Plan files now use memorable, human-readable names instead of UUIDs.
**How to use:**
```bash
# Session plans are now named with friendly slugs like:
# ~/.claude/plans/fluffy-bouncing-bunny.md
# ~/.claude/plans/golden-dancing-butterfly.md
```
**Details:**
- 146 adjectives × 112 verbs × 300 nouns = 4.9 million unique combinations
- Word categories include nature terms, animals, and whimsical objects
- Names like "sparkly-juggling-penguin" or "cozy-dreaming-unicorn"
- **Evidence**: `$A2()` at line 300930, word arrays at lines 300938-301497 in v2.0.50

### Code Change Indicator
**What:** Real-time display of file modifications during a conversation showing files changed and lines added/removed.
**Details:**
- Shows: `2 files +15 -8` format with color-coded counts
- Green for additions, red for deletions
- Tracks changes from tool use results
- Updates as files are modified during the session
- **Evidence**: `Fo2()` component at line 451329 in v2.0.50

### JSON Schema Support in SDK Initialization
**What:** Pass JSON schemas at SDK initialization time for automatic structured output validation.
**How to use:**
```python
# Python SDK example
from claude_code import ClaudeCode

client = ClaudeCode()
response = client.run(
    prompt="Generate user data",
    json_schema={
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"}
        },
        "required": ["name", "age"]
    }
)
```
**Details:**
- Schema is validated using Ajv validator
- Automatically creates a StructuredOutput validation tool
- Validates all outputs against the schema throughout the session
- Works via both SDK initialization and CLI `--json-schema` flag
- **Evidence**: `$D0()` at line 2327, `$G1()` at line 470974 in v2.0.50

### WebSearch Tool Now Requires Source Citations
**What:** Claude must now include a "Sources:" section with hyperlinked references when using web search.
**Details:**
- Mandatory "Sources:" section at end of responses using web search
- Links formatted as markdown hyperlinks: `[Title](URL)`
- Returns now include "links as markdown hyperlinks" in results
- **Evidence**: `k9B` variable at line 187201 in v2.0.50, adds "CRITICAL REQUIREMENT" section

### Enhanced LSP Client Robustness
**What:** Significant improvements to Language Server Protocol client reliability and error handling.
**Details:**
- New spawn event handling ensures process fully started before using stdio
- Added stdin error handler for write failures
- Added connection-level error and close handlers
- New cleanup flag prevents spurious errors during intentional shutdown
- Enhanced listener cleanup removes stdin/stderr handlers on stop
- Trace setup now has error handling
- **Evidence**: `w02()` function at line 304885 in v2.0.50

### Session Memory Template Enhancement
**What:** Added "Key results" section to session memory template for capturing concrete outputs.
**Details:**
- New section between "Learnings" and "Worklog"
- Purpose: Store specific answers, tables, or documents user requested
- Template prompt: "_If the user asked a specific output such as an answer to a question, a table, or other document, repeat the exact result here_"
- **Evidence**: `hP3` template at line 508626 in v2.0.50

### Remote Session Persistence Retry Logic
**What:** Added retry mechanism for remote session log persistence.
**Details:**
- Retries failed persistence attempts with exponential backoff
- Base delay of 1 second, max 8 seconds between attempts
- Better error messages including entry UUID in conflict errors
- **Evidence**: `JS5()` function at line 393547 in v2.0.50

### IDE Name Resolution Enhancement  
**What:** Improved detection and display of IDE names from various formats.
**Details:**
- Better handling of lowercase and trimmed IDE identifiers
- Fallback lookup for IDE display names
- Handles space-separated IDE names (uses first word)
- **Evidence**: `CE()` function at line 318709 in v2.0.50

### Large MCP Tool Result Handling
**What:** Improved handling of oversized MCP tool results with structured output support.
**Details:**
- Detects when results exceed maximum token limits
- Saves large outputs to temporary files
- Reports output format (plain text, JSON, JSON array with schema)
- Provides clear instructions for reading chunked content
- **Evidence**: `HZ5()` function at line 333257 in v2.0.50

### Startup Performance Telemetry
**What:** Added detailed startup performance tracking for diagnostics.
**Details:**
- Tracks import time, init time, settings load time, and total startup time
- Reports checkpoint counts and timing intervals
- Sampled at 0.1% of sessions for telemetry
- **Evidence**: `wT3()` function at line 506078, `UT3` timings at line 506093 in v2.0.50
