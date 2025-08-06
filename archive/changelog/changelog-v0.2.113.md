# Changelog for version 0.2.113

Based on my analysis of the diff, here's the changelog for Claude Code version 0.2.113:

## Claude Code v0.2.113 Changelog

### Token Usage Tracking Enhancements
- **Per-Model Token Tracking**: Improved token usage tracking with breakdown by model instead of aggregated totals
  - New display format shows token usage for each model separately
  - Format: `Model Name: X input, Y output, Z cache read, W cache write`
- **Enhanced Cache Metrics**: Better tracking of cache read and cache creation tokens
  - Added functions to separately track cache read input tokens and cache creation input tokens
  - More accurate cache usage reporting in API responses

### Command Execution Improvements
- **JSX Command Support**: Enhanced support for `local-jsx` command type
  - Commands can now return JSX components that hide the prompt input (`shouldHidePromptInput`)
  - Better handling of interactive command responses

### Performance Metrics
- **Time to First Token (TTFT)**: Added tracking for time to first token in streaming responses
  - Measures the time from request start to when the first token is received
  - Helps monitor API response latency

### Code Cleanup
- **Removed Drizzle ORM Dependencies**: Removed 343 functions related to Drizzle ORM
  - Removed database-related modules including table definitions, column builders, and SQL utilities
  - Simplified codebase by removing unused database abstraction layers

### Bug Fixes
- **Message Filtering**: Added filter to exclude progress and attachment messages from certain operations
  - Prevents UI clutter from non-content messages
  - Improves message handling reliability

### Developer Experience
- **Version Check**: Added function to detect when the configured model differs from the default
  - Helps identify configuration mismatches
- **VS Code Detection**: Added utility to detect if VS Code is installed on the system
  - Enables better IDE integration features

### Internal Improvements
- **Async Version Retrieval**: Version information is now fetched asynchronously
- **Better Error Handling**: Improved error handling in command execution flow
- **Stream Processing**: Enhanced stream handling with PassThrough support for better data flow

The update focuses on improving observability with detailed token tracking, enhancing command execution capabilities, and cleaning up the codebase by removing unused database-related code.
