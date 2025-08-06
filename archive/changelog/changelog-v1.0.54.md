# Changelog for version 1.0.54

Based on the comprehensive diff analysis, here's the changelog for Claude Code version 1.0.54:

# Claude Code v1.0.54 Changelog

## New Features

### 🚀 Dynamic OAuth Callback Port Configuration
- **Added environment variable support for OAuth callbacks**: You can now set `MCP_OAUTH_CALLBACK_PORT` to specify a custom OAuth callback port
- **Improved port selection for Windows**: OAuth callback port range now adapts based on platform (Windows: 39152-49151, others: 49152-65535)
- **Example usage**: 
  ```bash
  export MCP_OAUTH_CALLBACK_PORT=45000
  claude-code
  ```

### 📁 Enhanced File System Monitoring
- **New file watcher implementation**: Added comprehensive file system monitoring with `chokidar` integration for better detection of external file changes
- **Settings change detection**: Automatically detects when settings files are modified externally and can reload configurations
- **Improved performance**: Better handling of file system events with debouncing and throttling

### 🔧 Settings Configuration Improvements
- **Better validation messages**: Settings file validation now provides more descriptive error messages with specific field names
- **Schema documentation**: All settings fields now include helpful descriptions in the schema
- **New settings options**:
  - `permissions.allow/deny`: Glob patterns for file/directory access control
  - `permissions.defaultMode`: Default permission mode when Claude Code needs access
  - `permissions.disableBypassPermissionsMode`: Option to disable permission bypass
  - `permissions.additionalDirectories`: Additional directories to include in permission scope
  - `hooks`: Custom commands to run before/after tool executions
  - `forceLoginMethod`: Force specific login method ("claudeai" or "console")
  - `otelHeadersHelper`: Path to script for OpenTelemetry headers

### 🐚 Shell Environment Improvements  
- **Simplified shell snapshots**: Shell environment capture now outputs directly to stdout instead of writing temporary files
- **Debug mode support**: When `CLAUDE_CODE_DEBUG` is set, shell snapshots are saved to disk for troubleshooting
- **Removed shell snapshot cleanup**: Eliminated the periodic cleanup of old shell snapshots as they're no longer persisted by default

### ⌨️ Enhanced Keyboard Shortcuts
- **Platform-specific focus shortcut**: 
  - Windows: `Alt+M` to focus on the message input
  - Mac/Linux: `Cmd+M` to focus on the message input

## Improvements

### 🎯 Command System Enhancements
- **Better error handling for commands**: Failed commands now throw proper `CommandError` exceptions with context
- **Improved command validation**: More specific error messages when using unsupported command types
- **New command execution function**: Added `K1B` for executing prompt commands with better error handling

### 🌐 URL Handling
- **Safer URL opening**: Added URL validation before opening in browser to prevent security issues
- **Windows PowerShell support**: Improved browser opening on Windows using PowerShell for better compatibility

### 📊 Data Sharing
- **Async qualification check**: Added `m$1` function for checking data sharing qualification asynchronously

## Technical Changes

### 🏗️ Architecture Updates
- **New imports**: Added various Node.js stream, path, and process utilities for better system integration
- **Constants reorganization**: Moved and consolidated various timeout and configuration constants
- **Improved error tracking**: Better Sentry integration with more context for validation errors

### 🐛 Bug Fixes
- **Removed duplicate imports**: Cleaned up redundant imports of stream and process modules
- **Fixed shell environment issues**: Better handling of shell configuration file detection and sourcing
- **Improved Windows compatibility**: Better path handling and process execution on Windows

## Breaking Changes
- **Shell snapshot behavior**: Shell snapshots are no longer automatically saved to disk unless in debug mode
- **OAuth port ranges**: Changed default OAuth callback port ranges based on platform

## Internal Changes
- **Code refactoring**: Multiple functions renamed and restructured for better maintainability
- **New utility classes**: Added file watching and monitoring classes for better file system integration
- **Improved type safety**: Better TypeScript/schema definitions for settings validation
