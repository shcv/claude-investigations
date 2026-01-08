# Changelog for version 1.0.6

Based on my analysis of the diff file, here's the changelog for Claude Code version 1.0.6:

### New Features

#### Web Search Tool Enhancement
- **Improved web search parameter handling**: The web search tool now uses a more streamlined parameter structure. Instead of separate objects, domain filters are now passed directly through the tool configuration:
  ```javascript
  // New usage
  claude web-search "your query" --allowed-domains example.com --blocked-domains spam.com
  ```

### Bug Fixes

#### Screenshot File Path Resolution
- **Fixed screenshot file handling with AM/PM timestamps**: Improved the file path resolution for screenshots that contain AM/PM timestamps. The tool now:
  - Uses a more robust regex pattern to detect timestamp formats
  - Checks for file existence before applying transformations
  - Handles both regular spaces and non-breaking spaces (Unicode 8239) in filenames
  - Falls back gracefully if the expected file doesn't exist

  This fixes issues where screenshots taken at specific times (like "Screenshot 2:30 PM.png") might not be found due to space character encoding differences.

#### Graceful Shutdown Handling
- **Added explicit error handling for shutdown failures**: A new graceful shutdown wrapper ensures that if the shutdown process fails, the error is logged and the process exits cleanly with the appropriate exit code.

### Technical Improvements

#### Import Optimizations
- Added explicit imports for `cwd` from `node:process` and `PassThrough` from `stream` modules
- Improved module loading efficiency

#### Configuration Changes
- **Removed `enableAllProjectMcpServers` flag**: This configuration option has been removed from the project settings structure, simplifying MCP server management

### Removed Features

#### Easter Egg Removal
- **Removed "The Way of Code" easter egg**: The hidden `vibe` command that displayed ASCII art and philosophical coding quotes has been removed. This feature previously showed:
  - ASCII art of the Claude logo
  - Quotes inspired by Lao Tzu and adapted by Rick Rubin
  - Could be accessed via the `vibe` command

### Summary

Version 1.0.6 focuses on stability improvements and bug fixes, particularly around file handling for screenshots with special characters in their names. The removal of the easter egg and configuration simplification suggests a move toward a more streamlined, production-ready codebase.
