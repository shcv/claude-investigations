# Changelog for version 1.0.18


### MCP Server Management UI
- **New interactive MCP server management interface** - Users can now manage MCP (Model Context Protocol) servers through a new interactive UI
  - `claude mcp` - Opens the MCP server management interface
  - View connected servers, their status (connected, pending, needs authentication, failed)
  - Browse and inspect available tools for each MCP server
  - View tool details including parameters, descriptions, and whether they're read-only
  - Authenticate SSE (Server-Sent Events) based MCP servers directly from the UI


### Enhanced Directory Permissions
- **New `--add-dir` flag** - Add additional working directories for the current session
  ```bash
  claude "analyze this project" --add-dir /path/to/project --add-dir ../another/directory
  ```
  - Supports multiple directories
  - Can use relative or absolute paths
  - Validates that paths exist and are directories


### Streaming JSON Input Support
- **New streaming input mode** - Accept streaming JSON input from stdin for continuous interactions
  - Supports the `stream-json` output format for real-time message processing
  - Enables piping structured messages into Claude Code for automated workflows


### Enhanced Permission Modes
- **Improved permission system** with new modes:
  - `default` - Standard permission checking
  - `acceptEdits` - Accept file edits without prompting
  - `plan` - Planning mode for complex tasks
  - `bypassPermissions` - Skip permission checks (requires explicit acceptance)


### Performance Enhancements
- **Async message history loading** - Message transcripts and summaries now load asynchronously for better performance
- **Caching improvements** for MCP client connections with cache invalidation support
- **Optimized file filtering** for MCP tools by server name


### ️ Better Error Handling
- **Improved directory existence checks** - More robust handling when creating directories or files
- **Enhanced rate limit handling** - Better tracking and display of unified rate limit status
- **Clearer error messages** for MCP tool authentication failures


### Logging Improvements
- **New environment variable `OTEL_LOG_USER_PROMPTS`** - Enable logging of user prompts for debugging
- **Simplified log cleanup** - Removed separate message log cleanup, focusing on MCP logs only


### Fixed Issues
- **Permission prompt improvements** - Fixed duplicate permission prompts for file operations
- **Directory path handling** - Better handling of paths with spaces (proper quoting)
- **Streaming mode stability** - Fixed issues with streaming JSON input parsing
- **MCP server reconnection** - Servers now properly reconnect after authentication


### Internal Improvements
- Refactored MCP tool filtering to use consistent naming patterns (`mcp__<server>__<tool>`)
- Improved separation between MCP tools and built-in tools
- Better handling of tool permission contexts for different modes
- Enhanced support for SSE-based MCP authentication flow


### Managing MCP Servers
```bash
# Open MCP server management interface
claude mcp

# The interface allows you to:
# - View all configured MCP servers
# - Check connection status
# - Browse available tools
# - Authenticate servers that need it
# - View detailed tool documentation
```


### Working with Additional Directories
```bash
# Add directories to the working context
claude "refactor this codebase" --add-dir ./src --add-dir ./tests

# Use relative paths
claude "analyze dependencies" --add-dir ../shared-lib

# Multiple projects at once
claude "find common patterns" --add-dir ~/project1 --add-dir ~/project2
```


### Streaming Mode
```bash
# Pipe streaming JSON messages
echo '{"type":"user","message":{"role":"user","content":"Hello"}}' | claude --print --output-format=stream-json --verbose

# Use with other tools that output structured messages
./message-generator | claude --print --output-format=stream-json
```

This update focuses on improving the MCP (Model Context Protocol) integration experience, making it easier to manage external tool servers, authenticate them, and work with multiple directories in your projects. The streaming improvements also enable better integration with automated workflows.
