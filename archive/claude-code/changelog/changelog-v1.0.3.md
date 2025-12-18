# Changelog for version 1.0.3

# Changelog v1.0.3

## New Features

### Enhanced Image Type Detection
- Added automatic image format detection from base64 data (`JQ0` function)
- Supports detection of PNG, JPEG, GIF, and WebP formats based on file signatures
- Provides fallback to PNG format when detection fails

### GhostTTY Terminal Integration
- New support for GhostTTY terminal configuration (`eL4` function)
- Automatically installs Shift+Enter key binding for multi-line input
- Cross-platform support with proper config paths for macOS and Linux
- Creates automatic backups of existing configurations before modification
- Warns users about existing Shift+Enter bindings to prevent conflicts

### Improved Unicode Handling
- Added robust Unicode sanitization (`Ff1` and `IL` functions)
- Normalizes text using NFKC normalization
- Removes invisible control characters, direction markers, and private use characters
- Prevents potential security issues from malformed Unicode input
- Applies sanitization recursively to all string inputs in nested data structures

### Enhanced Shell Command Safety
- Improved handling of file descriptor redirections (`>&0`, `>&1`, `>&2`)
- Better parsing and validation of shell commands with output redirection
- Prevents unsafe command patterns while allowing legitimate redirections

## Technical Improvements

### Process Information
- Enhanced user agent string now includes the entrypoint information via `CLAUDE_CODE_ENTRYPOINT` environment variable
- Provides better debugging context for different execution environments

### Code Organization
- Removed unused imports and variables for cleaner codebase
- Consolidated stream handling with PassThrough import
- Removed deprecated batch operation functionality

## Bug Fixes

- Fixed potential issues with shell command parsing that could lead to unexpected behavior
- Improved error handling in configuration file operations
- Better validation of command-line arguments containing special characters

## Breaking Changes

- Removed the experimental Batch tool functionality (was using `pF1` variable)
- This feature was likely not widely used and has been replaced with more reliable alternatives

## Notes for Users

- If you use GhostTTY terminal, you'll now have better multi-line input support with Shift+Enter
- Unicode handling is more robust, preventing potential display issues with special characters
- Shell commands with output redirection are now safer and more predictable
