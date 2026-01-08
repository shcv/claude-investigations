# Changelog for version 0.2.41

### New Features

#### MCP (Model Context Protocol) Status Command
- **New command**: `/mcp` - Shows the connection status of all configured MCP servers
- Displays a formatted list of MCP servers with their connection states:
  - **connected** (green) - Successfully connected to the server
  - **connecting…** (yellow) - Connection in progress
  - **failed** (red) - Connection failed
- Includes debug mode support with `--mcp-debug` flag for inline error logs
- Shows log file location for troubleshooting failed connections

Example output:
```
MCP Server Status

• server1: connected
• server2: connecting…
• server3: failed

Run claude with --mcp-debug to see error logs inline, or view log files in: /path/to/logs
```

### Improvements

#### Enhanced MCP Integration
- Improved MCP server connection handling with better error reporting
- Added connection timeout configuration (5 seconds default)
- MCP tools and prompts now have an `isMcp: true` property for better identification
- Better separation of MCP client state management

#### Logging Infrastructure
- New `baseLogs()` function added to the logging system for accessing the base log directory
- Enhanced MCP-specific logging with dedicated log files per server

#### Memory Management
- Added telemetry events for memory undo operations:
  - `tengu_memory_undo_attempt` - Tracks when undo is attempted
  - `tengu_memory_undo_success` - Tracks successful undo operations
  - `tengu_memory_undo_failure` - Tracks failed undo operations

### Technical Changes

#### Refactored MCP Architecture
- Replaced monolithic MCP initialization with a more modular approach:
  - New `cS1()` function for parallel MCP server connections
  - New `zx2()` function for aggregating MCP resources
  - New `Qx2()` React hook for managing MCP state in the UI
- Improved error handling with per-server error isolation
- Better separation of concerns between connection, tool discovery, and prompt discovery

#### Performance Optimizations
- Changed from SHA-256 web crypto API to Node.js native crypto module for hash operations
- More efficient stream handling with direct `Readable` imports
- Improved memoization for tool and command lists with new `gl2()` and `Ul2()` utility functions

#### Code Quality
- Better TypeScript/Zod schema validation for MCP server configurations
- Cleaner import organization and dependency management
- More consistent error messaging and logging patterns

### Bug Fixes
- Fixed potential race conditions in MCP server connection initialization
- Improved error handling for failed MCP server connections
- Better cleanup of timeouts in connection handling

### Breaking Changes
None - This release maintains backward compatibility with existing configurations and APIs.
