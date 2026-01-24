# Changelog for version 2.1.14


## Summary

This release renames `MCPSearch` to `ToolSearch` to better reflect its broader tool discovery capabilities, adds support for dynamically discovered skills from `.claude/skills` directories, introduces a new `CLAUDE_CODE_GLOB_TIMEOUT_SECONDS` environment variable for controlling glob timeouts, and simplifies the ExitPlanMode tool documentation. Additionally, Claude.ai MCP server integration has been expanded with improved telemetry and eligibility checking.

### ToolSearch (renamed from MCPSearch)

**What**: The `MCPSearch` tool has been renamed to `ToolSearch` to better reflect its ability to search for and load both MCP tools and deferred built-in tools.

**Usage**: The tool works the same way but with the new name:
```
ToolSearch with query: "select:NotebookEdit"
ToolSearch with query: "slack"
```

**Details**:
- Direct selection mode: Use `select:<tool_name>` for exact tool loading
- Keyword search: Use natural language to find relevant tools
- Now supports loading deferred built-in tools in addition to MCP tools
- Documentation updated throughout to reference the new name

**Evidence**: `aj` at line 280183 (tool name constant, contains `"ToolSearch"`)

### Configurable Glob Timeout

**What**: A new environment variable `CLAUDE_CODE_GLOB_TIMEOUT_SECONDS` allows customizing the timeout for glob/ripgrep operations.

**Usage**:
```bash
export CLAUDE_CODE_GLOB_TIMEOUT_SECONDS=30
claude
```

**Details**:
- Default timeout remains 20 seconds (60 seconds on WSL)
- Set a custom value in seconds to override the default
- Useful for large codebases where glob operations may take longer

**Evidence**: `r0Q()` at line 30721 (ripgrep executor, contains `"CLAUDE_CODE_GLOB_TIMEOUT_SECONDS"`)

### Dynamic Skill Discovery

**What**: Skills can now be discovered dynamically from `.claude/skills` directories at any level of the project hierarchy.

**Details**:
- Scans for `SKILL.md` files in subdirectories of `.claude/skills`
- Skills are discovered based on directory triggers during operation
- Enables projects to define reusable skills that Claude can invoke
- Skills defined in parent directories are also discovered

**Evidence**: `vl5()` at line 373896 (dynamic skill discovery, references `"SKILL.md"` and `"dynamic_skill"`)

### Skills with Required MCP Server Dependencies

**What**: Skills can now specify required MCP servers and will only be available when those servers are connected.

**Details**:
- Skills can declare `requiredMcpServers` as dependencies
- Skill availability is filtered based on connected MCP servers
- Enables context-aware skill loading

**Evidence**: `UV0()` at line 313441 (MCP server requirement check, contains `"requiredMcpServers"`)

### WebFetch GitHub URL Guidance

**What**: WebFetch tool documentation now recommends using the `gh` CLI for GitHub URLs.

**Details**:
- New guidance: "For GitHub URLs, prefer using the gh CLI via Bash instead (e.g., gh pr view, gh issue view, gh api)"
- Reduces reliance on web scraping for GitHub content
- Leverages the more reliable `gh` CLI for GitHub operations

**Evidence**: `AwQ` at line 96805 (WebFetch tool description, contains `"gh pr view, gh issue view, gh api"`)

### Simplified ExitPlanMode Tool Description

**What**: The ExitPlanMode tool documentation has been simplified by removing the `allowedPrompts` permission request section.

**Details**:
- Removed detailed instructions about requesting Bash permissions during plan approval
- Streamlines the plan mode workflow
- Documentation now focuses on core functionality

**Evidence**: `Zn2` at line 416019 (ExitPlanMode description, no longer contains `"allowedPrompts"`)

### Claude.ai MCP Server Integration Improvements

**What**: Enhanced Claude.ai MCP server integration with better eligibility checking and telemetry.

**Details**:
- New eligibility states tracked: `disabled_gate`, `disabled_env_var`, `no_oauth_token`, `missing_scope`, `eligible`
- Requires `user:mcp_servers` OAuth scope
- Can be disabled via `ENABLE_CLAUDEAI_MCP_SERVERS` environment variable
- Improved logging for debugging MCP server connectivity

**Evidence**: `Q_0` at line 458270 (Claude.ai MCP initialization, contains `"tengu_claudeai_mcp_eligibility"`)

### Prompt Suggestion Mode Improvements

**What**: The prompt suggestion system now supports a new "stated intent" mode in addition to the existing "user intent" mode.

**Details**:
- New `stated_intent` mode focuses on finding explicitly stated next steps from user messages
- Looks for multi-part requests ("do X and Y"), stated intent ("then I'll Z"), and answers to Claude's questions
- Controlled by `tengu_plank_river_frost` feature flag
- Provides more conservative suggestions based on user's explicit plans

**Evidence**: `ls5` at line 395184 (stated intent prompt, contains `"stated_intent"` and `"SEARCH FOR"`)

### Git Clone with SHA Support

**What**: Git clone operations now support checking out specific commit SHAs in addition to branches.

**Details**:
- Uses `--no-checkout` flag followed by SHA fetch and checkout
- Falls back to `--unshallow` fetch if shallow fetch of SHA fails
- Enables working with specific commit references

**Evidence**: `FU7()` at line 497957 (git clone function, contains `"--no-checkout"` and `"checkout"`)

### Debug Log Cleanup

**What**: Added automatic cleanup of old debug log files.

**Details**:
- Cleans up `.txt` files from the debug directory
- Removes files older than a threshold date
- Helps manage disk space from accumulated debug logs

**Evidence**: `Tj7()` at line 530506 (debug cleanup function, accesses `"debug"` directory)

### Tool Usage Tracking for Deferred Tools

**What**: Added tracking infrastructure for deferred tool usage patterns.

**Details**:
- Tracks `usageCount` and `lastUsedAt` for tools
- Enables smarter tool deferral decisions based on usage frequency
- Similar tracking added for skill usage with time-decay weighting

**Evidence**: `R22()` at line 280135 (tool usage tracker, contains `"toolUsage"`, `"usageCount"`, `"lastUsedAt"`)

### Proxy Configuration Improvements

**What**: Added support for `no_proxy` and `NO_PROXY` environment variables.

**Details**:
- New function to read proxy bypass configuration
- Improves compatibility with corporate network environments

**Evidence**: `kx3()` at line 155303 (proxy config reader, contains `"no_proxy"` and `"NO_PROXY"`)

## Internal Changes

- Refactored ripgrep execution to use spawn with better timeout handling
- Added `REPL` tool type constant for future use
- Improved border style handling in UI components
- Various code organization and cleanup changes
