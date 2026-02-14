# Changelog for version 0.2.42

# Claude Code v0.2.42 Changelog


### Batch Tool Execution (Call Tool)
A powerful new tool that allows executing multiple tools in a single request for improved performance:

- **Tool Name**: `BatchTool` (displayed as "Call" to users)
- **Purpose**: Run multiple independent tool operations at once to reduce context usage and latency
- **Execution**: Tools are executed in parallel when possible, otherwise serially
- **Usage Example**:
  ```
  claude> /call
  {
    "invocations": [
      {
        "tool_name": "Bash",
        "input": {
          "command": "git blame src/foo.ts"
        }
      },
      {
        "tool_name": "Glob", 
        "input": {
          "pattern": "**/*.ts"
        }
      },
      {
        "tool_name": "Grep",
        "input": {
          "pattern": "function",
          "include": "*.ts"
        }
      }
    ]
  }
  ```


### MCP Server Timeout Configuration
- **New Environment Variable**: `MCP_TIMEOUT` 
- **Default**: 5000ms (5 seconds)
- **Usage**: Set custom timeout for MCP server operations
  ```bash
  MCP_TIMEOUT=10000 claude  # Set 10 second timeout
  ```
- **Benefit**: Allows users to adjust timeout for slower MCP servers


### Non-Blocking MCP Server Startup
- MCP server initialization no longer blocks the application from starting
- Improves startup time when MCP servers are slow to initialize
- Application becomes responsive immediately while MCP servers load in background


### Enhanced Help Mode
- New help display showing keyboard shortcuts when help is open
- Displays:
  - `! for bash mode` - Quick access to bash command mode
  - `/ for commands` - Access slash commands
  - Platform-specific newline instructions:
    - Mac with Karabiner: `shift + ⏎ for newline`
    - Terminal supporting backslash: `\⏎ for newline`
    - Default: `Backslash (\) + Return (⏎) for newline`


### WebFetch Security Enhancement
- Updated security requirement: URLs must be provided directly by the user (removed "in the current or a previous message" qualifier)
- Strengthens security by requiring explicit user-provided URLs


### HTTP Request Handling
- Switched from native `fetch` to axios for better control
- Added proper redirect handling with `maxRedirects: 0`
- Improved error messages with HTTP status codes
- Better content length limiting with `maxContentLength`


### Release Notes Update
- Added v0.2.41 release notes documenting:
  - MCP server startup timeout configuration via MCP_TIMEOUT
  - Non-blocking MCP server startup behavior


### Code Organization
- Renamed internal functions and variables for consistency
- Improved stream handling using named imports
- Better error handling in HTTP requests
- Enhanced batch tool execution with proper progress tracking and error aggregation
