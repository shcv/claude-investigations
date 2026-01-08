# Changelog for version 1.0.65

Based on my analysis of the diff file, here's the changelog for Claude Code version 1.0.65:

# Claude Code v1.0.65 Changelog

### Settings Schema Support
- Added JSON Schema support for Claude Code settings files
- Settings files can now include `$schema: "https://json.schemastore.org/claude-code-settings.json"` for validation and autocompletion in supported editors
- Improved settings validation with clearer error messages

### Enhanced Bash Tool Shell Integration
- **Improved shell startup behavior**: The Bash tool now better captures and preserves your shell environment including:
  - User-defined functions (filtered to exclude system functions)
  - Shell aliases (with special handling for Windows Git Bash winpty aliases)
  - Shell options and settings
  - PATH environment variable
- **Better cross-platform support**: Special handling for Windows environments (MSYS/Cygwin) to avoid "stdin is not a tty" errors with winpty aliases
- **Snapshot file generation**: Creates a comprehensive snapshot of your shell environment for more reliable command execution

### Settings File Watcher Improvements
- Refactored settings file monitoring system for better performance
- More efficient file watching with improved change detection
- Better handling of file creation and deletion events

### Performance Optimizations
- Removed unnecessary diagnostic event handlers that could impact performance
- Streamlined the caching system with a more efficient implementation
- Reduced memory usage in the message compaction system

### Code Quality
- Removed several unused imports and variables
- Simplified the diagnostic management system
- Cleaned up deprecated conversation mode configurations ("Default", "Insights", "Learn by Doing")

### IDE Integration
- Enhanced selected lines tracking in IDE integration
- Now tracks line start and end positions for better context preservation
- Improved handling of truncated content in IDE selections

## Bug Fixes

- Fixed shell function capture in Bash and Zsh environments
- Resolved issues with base64 encoding of shell functions containing special characters
- Fixed handling of shell aliases on Windows Git Bash

## Technical Changes

- Removed unused ripgrep wrapper functions
- Consolidated child process execution imports
- Simplified the LRU cache implementation
- Removed redundant diagnostic notification handlers

## Removed Features

- Removed the built-in conversation modes (Default, Insights, Learn by Doing)
- These modes previously offered different interaction styles but have been deprecated in favor of a unified experience
