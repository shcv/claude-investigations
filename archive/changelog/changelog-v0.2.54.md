# Changelog for version 0.2.54

Based on my analysis of the diff, here is the changelog for version 0.2.54:

# Claude Code v0.2.54 Changelog

## New Features

### Memory System
- **New `/memory` command**: Edit and manage Claude's memory files
  - Access three types of memory:
    - **Project memory** - Stored in `./CLAUDE.md` (checked into your repository)
    - **User memory** - Stored in `~/.claude/memory` (global to your user account)
    - **Local memory** - Project-specific memory (not checked in)
  - Quick access with `#` prefix in input (e.g., `# Always use descriptive variable names`)
  - Visual indicator shows loaded memory types (e.g., "project + user memory")
  - Memory files are created automatically when accessed for the first time

### API Response Streaming
- **SSE (Server-Sent Events) support**: New streaming mode for API responses
  - Configuration option to choose between `stdio` (default) and `sse` modes
  - Enables real-time streaming of Claude's responses for better interactivity

### Terminal Enhancements
- **Option as Meta key support**: Automatic configuration for macOS Terminal.app
  - Enables Option+Enter for newline input
  - Automatically configures Terminal preferences on first run
  - Shows helpful status message when enabled

### WebFetch Improvements
- **15-minute response cache**: Faster repeated access to the same URLs
  - Automatic cache cleanup for entries older than 15 minutes
  - Improves performance when working with web documentation

### Enhanced Domain Detection
- **Improved URL parsing**: Better detection of domains mentioned in conversations
  - Supports multiple URL formats including bare domains
  - More intelligent domain extraction from user messages

## UI/UX Improvements

### Visual Indicators
- **Memory mode indicator**: Shows `# to memorize` hint when in memory mode
- **Auto-accept mode indicator**: Shows `⏵⏵ auto-accept edits on` when file edits are auto-accepted
- **Spinner customization**: New spinner styles and messages for different operation types
  - Separate configurations for thinking, responding, and tool use states

### Project Analysis
- **File count estimation**: Shows rounded project file count in telemetry
  - Provides better context about project size
- **Context size tracking**: Improved tracking of memory and context usage

## Performance Improvements

- **Lodash integration**: Added Lodash (v4.17.21) for optimized utility functions
- **Better resource cleanup**: Improved handling of memory and cache resources
- **Streaming optimizations**: More efficient handling of large responses

## Developer Experience

### Configuration
- **MCP server configuration**: Support for both `stdio` and `sse` type servers
  ```javascript
  {
    "mcpServers": {
      "example": {
        "type": "sse",
        "url": "https://example.com/mcp"
      }
    }
  }
  ```

### Error Handling
- **Permission error tracking**: Better telemetry for file access issues
- **Improved error messages**: More descriptive error feedback for common issues

## Bug Fixes

- **Removed duplicate dependencies**: Cleaned up dotenv and related packages
- **Fixed command parsing**: Better handling of command input modes
- **Improved file path handling**: More robust path resolution for memory files

## Internal Changes

- **Code reorganization**: Significant refactoring of internal modules
- **Updated telemetry**: New events for memory usage, Option+Meta configuration, and cache hits
- **Dependency updates**: Updated internal dependencies and build process

This release focuses on improving the development workflow with the new memory system, better streaming capabilities, and enhanced terminal integration, while also providing performance improvements and bug fixes.
