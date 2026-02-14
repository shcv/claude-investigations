# Changelog for version 0.2.44

# Claude Code v0.2.44 Changelog


### Thinking Mode ("Think Harder")
- **New thinking mode activation**: Simply say "think", "think harder", or even "ultrathink" to have Claude make a plan before executing
- Claude will enter a planning mode where it thinks through the implementation steps before coding
- After presenting the plan, you'll be prompted to exit plan mode and proceed with implementation


### Enhanced Autocomplete System
- **Improved file path autocomplete**: The autocomplete system now provides intelligent file path suggestions as you type
- **Fuzzy file search**: File paths are matched using fuzzy search with relevance scoring
- **Directory navigation**: Autocomplete shows parent directories and supports navigating through the file tree
- **Smart filtering**: Test files are deprioritized in autocomplete results
- **Visual improvements**: Better formatting and scrolling for autocomplete suggestions with a maximum of 10 visible items


### macOS Keychain Security Enhancement
- Added `gd2()` function to delete API keys from macOS Keychain when needed
- Improved security for API key management on macOS


### Autocomplete UI
- **New suggestion types**: Supports both command suggestions (starting with `/`) and file path suggestions
- **Keyboard shortcuts**:
  - `Tab`: Accept the current suggestion
  - `Up/Down arrows`: Navigate through suggestions
  - `Enter`: Accept selected suggestion
  - `Escape`: Clear suggestions
- **Smart completion**: Automatically completes common prefixes when multiple matches exist
- **Visual indicators**: Selected suggestions are highlighted with appropriate colors


### Interactive Features
- **Triple-click detection**: New `F91()` function detects rapid clicks (3 clicks within 1 second) to trigger special actions
- **Auto-accept mode**: New toggle system for automatically accepting certain tool confirmations (can be enabled/disabled per session)

## Performance Improvements

- **Optimized file indexing**: Background file indexing for faster autocomplete responses
- **Caching**: File list caching to reduce filesystem operations
- **Batch operations**: Multiple tool calls can now be batched for better performance

## Technical Improvements

- **Non-interactive session support**: Better handling of non-interactive sessions (e.g., when running from scripts)
- **Improved error handling**: More robust error handling for API authentication failures
- **Code organization**: Refactored autocomplete logic into separate, focused functions for better maintainability

## Bug Fixes

- Fixed issues with permission mode handling
- Improved handling of root/sudo privileges with `--dangerously-skip-permissions` flag
- Better error messages for API key validation failures

## Internal Changes

- Updated internal version tracking and telemetry
- Refactored suggestion system to use a more modular architecture
- Improved TypeScript/JavaScript code analysis for better language detection


**Note**: This version focuses heavily on improving the interactive experience with intelligent autocomplete and the new thinking mode for better planning before implementation.
