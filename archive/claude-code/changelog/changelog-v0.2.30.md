# Changelog for version 0.2.30

# Claude Code v0.2.30 Changelog

### New File Management System
- **Introduced `AM` class** for temporary file management with automatic cleanup
  - Provides methods for writing, reading, checking existence, and getting file size
  - Files are stored in system temp directory with pattern `/tmp/claude-{id}-{type}`
  - Includes automatic size checking and deletion capabilities

### Enhanced Color System
- **Added 256-color terminal support** with new `s6()` function that converts RGB colors to ANSI 256-color codes
  - Provides better color accuracy for terminals supporting extended color palettes
  - Automatically maps RGB values to nearest 256-color equivalent
  - Handles grayscale colors separately for better accuracy

### Improved Environment Detection
- **Enhanced IDE and terminal detection** in `mX4()` function
  - Now detects Cursor, Windsurf, and all JetBrains IDEs (PyCharm, IntelliJ, WebStorm, etc.)
  - Checks `__CFBundleIdentifier` environment variable for more accurate IDE detection
  - Better support for development environments beyond traditional terminals

### Package Manager Detection
- **New automatic package manager discovery**
  - `OX4`: Detects available Node.js package managers (npm, yarn, pnpm)
  - `TX4`: Detects JavaScript runtimes (bun, deno, node)
  - `uX4`: Specifically checks if running under Bun runtime
  - Enables smarter dependency installation based on available tools

### API Key Management Improvements
- **Enhanced API key storage with macOS Keychain integration**
  - New `Jc()` function retrieves API keys from macOS Keychain when available
  - `Y30()` function stores API keys securely in Keychain on macOS
  - Falls back to configuration file storage on other platforms
  - Improved security for API key handling

### New Tracking Functions
- **`XM()`**: Tracks API usage costs and duration metrics
- **`Dj()`**: Returns total lines removed during operations
- **`al1()`**: Returns timestamp of last user interaction
- **`Hj()`**: Executes commands with timeout and proper error handling

### Message Filtering
- **New `Oz()` function** filters out progress messages from conversation history
  - Improves performance by removing non-essential messages
  - Keeps conversation focused on actual content

### Token Efficiency
- Updated internal flag from `token-efficient-tools-2024-12-11` to `token-efficient-tools-2025-02-19`
- Indicates optimizations for reduced token usage in tool operations

### File Size Limits
- New `Xj` variable defines maximum file size based on `vX4` configuration
- Better handling of large file operations

## Removed Features

Several internal functions and variables were removed, likely replaced by the new implementations:
- Removed standalone terminal detection function (replaced by enhanced `mX4()`)
- Removed various UI components related to sticker requests and animations
- Cleaned up deprecated color theme definitions
- Removed unused import statements and helper functions

## Developer Notes

The update focuses on improving the foundation of Claude Code with better environment detection, secure API key management, and enhanced performance tracking. The new color system provides better visual consistency across different terminal types, while the package manager detection enables smarter dependency handling.
