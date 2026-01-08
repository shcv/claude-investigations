# Changelog for version 1.0.49

# Claude Code v1.0.49 Changelog

### Windows Git Bash Integration
- **Automatic Git Bash detection**: Claude Code now automatically detects and configures Git Bash on Windows systems
- **Custom Git Bash path**: Set `CLAUDE_CODE_GIT_BASH_PATH` environment variable to specify a custom Git Bash location
- **Path conversion**: Added automatic Windows-to-Unix path conversion using `cygpath` for Git Bash compatibility

### File System Watching (Chokidar Integration)
- **Real-time file monitoring**: Added comprehensive file watching capabilities powered by Chokidar
- **Watch events**: Support for file/directory add, change, unlink events with configurable options
- **Symlink handling**: Proper symlink resolution and circular symlink detection
- **Performance optimizations**: Binary file detection and optimized polling intervals for different file types

### Enhanced Configuration Validation
- **Improved error messages**: More helpful validation errors with specific suggestions for configuration issues
- **Field-specific tips**: Added contextual help for configuration errors (e.g., apiKeyHelper format)
- **Documentation links**: Automatic documentation links for configuration fields like permissions, env, and hooks

### Path Handling
- **Cross-platform support**: Better handling of Windows paths with proper normalization
- **Absolute path resolution**: New utilities for resolving and joining paths across platforms
- **Path validation**: Enhanced validation for file paths and directory structures

### Stream Processing
- **Readdirp integration**: Advanced recursive directory reading with filtering capabilities
- **Stream optimization**: High-performance file enumeration with configurable water marks
- **Error handling**: Graceful handling of permission errors and inaccessible directories

## Bug Fixes

- Removed duplicate imports and unused functions
- Fixed shell function snapshot generation issues
- Improved error handling for missing directories
- Better handling of special characters in file paths

## Internal Changes

- Added new utility functions: `ls2`, `TfA`, `P29`, `IlA`, `ZlA`, `GlA`, `FlA`, `R79`, `YlA`, `WlA`
- New classes: `HlA` (recursive directory reader), `hy1` (Node.js file system handler), `jlA` (directory watcher), `ylA` (watch helper), `dy1` (main watcher)
- Removed obsolete functions: `M3`, `jQ`, `F9Q`, `hK`, `KuQ`, `jx6`, `sx6`, `Nh2`, `ox6`, `tx6`, `ex6`

### New Environment Variables
- `CLAUDE_CODE_GIT_BASH_PATH`: Specify custom Git Bash location on Windows
- `CHOKIDAR_USEPOLLING`: Force polling mode for file watching (true/false)
- `CHOKIDAR_INTERVAL`: Set polling interval in milliseconds

### Watch Options
```javascript
{
  persistent: true,           // Keep process alive while watching
  ignoreInitial: false,      // Emit events for initial scan
  followSymlinks: true,      // Follow symbolic links
  usePolling: false,         // Use fs.watchFile instead of fs.watch
  interval: 100,             // Polling interval (ms)
  binaryInterval: 300,       // Polling interval for binary files (ms)
  awaitWriteFinish: {        // Wait for writes to finish
    stabilityThreshold: 2000,
    pollInterval: 100
  }
}
```
