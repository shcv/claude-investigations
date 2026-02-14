# Changelog for version 0.2.114

# Claude Code v0.2.114 Changelog


### Debug Mode
- Added `--debug` / `-d` command line flag for enhanced debugging capabilities
- When enabled, provides detailed debug output with dimmed formatting
- Debug messages include MCP server errors and other diagnostic information
- Example usage: `claude --debug` or `claude -d`


### Enhanced Text Truncation for Large Inputs
- Automatically truncates text inputs exceeding 10,000 characters to prevent UI issues
- Smart truncation preserves beginning and end of text while removing middle content
- Truncated content is stored separately and marked with placeholder text showing line count
- Prevents performance degradation when pasting very large text blocks


### Improved Git Ignore Management
- Now uses global git ignore file at `~/.config/git/ignore` instead of modifying project `.gitignore` files
- Checks if files are already ignored before attempting to add ignore rules
- Creates `.config/git/` directory structure if it doesn't exist
- More respectful of existing project configurations


### Tool Execution Enhancements
- New `renderToolUseQueuedMessage` support for tools to display custom queued state messages
- Improved error handling for tool progress rendering
- Better separation of debug and verbose logging in tool contexts


### Memory Management
- Fixed issue where extremely large text inputs could cause UI freezing
- Automatic text truncation now triggers for inputs over 10,000 characters
- Prevents memory issues when pasting large code files or logs


### MCP Server Integration
- Added `debug` and `verbose` parameters to MCP tool execution context
- Improved error logging for MCP server failures
- Better diagnostic information when MCP servers encounter errors


### Code Organization
- Removed unused functions related to permission prompts and decision rendering
- Cleaned up OAuth redirect handler code
- Removed duplicate imports and variables
- Better path handling with explicit `posix` and `win32` path imports


### Performance
- Reduced maximum response delay from unlimited to 1000ms for better responsiveness
- Optimized text truncation to maintain UI performance with large inputs

## Version Update
- Updated from v0.2.113 to v0.2.114
- Auto-updater now references the new version for update checks
