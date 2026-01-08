# Changelog for version 1.0.17

# Claude Code v1.0.17 Changelog

### Enhanced Status Command
The `claude status` command has been refactored to use React hooks for better performance and reliability. The status display now loads asynchronously and updates dynamically as information becomes available.

### Simplified Update Process
The automatic update and fallback mechanism has been streamlined. The launcher script (claude.sh) has been updated to version 0.0.7 with cleaner logic for managing Claude installations.

### State Management Improvements
The application now uses a centralized state management hook (`k3()`) instead of separate state calls, providing more consistent behavior across the interface.

### MCP (Model Context Protocol) Integration
- MCP clients, tools, commands, and resources are now managed through a centralized state object
- Better integration with the global state management system
- More efficient handling of MCP client connections

### Performance Optimizations
- Replaced synchronous status section generation with asynchronous loading
- Status sections now render progressively as data becomes available
- Reduced unnecessary file system operations during launcher setup

### Code Quality
- Removed redundant symlink management code (`dH5` function and related logic)
- Simplified the launcher installation process by removing the "known-good" and "latest" symlink complexity
- Better separation of concerns in the main UI component

### Import Changes
- Added focused import for `cwd` from `node:process` instead of importing the entire module
- Changed stream import to use named import `PassThrough` for better tree-shaking

## Bug Fixes
- Fixed potential race conditions in status display updates
- Improved error handling in the launcher setup process
- Better cleanup of temporary files and symlinks

## Version Updates
- Claude CLI launcher script updated from v0.0.6 to v0.0.7
- Application version bumped to 1.0.17
