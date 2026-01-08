# Changelog for version 1.0.23

### New Features

#### 🆕 Add Directory Command (`/add-dir`)
A new command has been added to dynamically add working directories during your session:

```bash
/add-dir <path>
```

**Usage Examples:**
- `/add-dir ../my-project` - Adds a relative path as a working directory
- `/add-dir /home/user/projects` - Adds an absolute path as a working directory

**Features:**
- Validates that the path exists and is a directory
- Prevents adding directories that are already accessible within existing working directories
- Provides helpful error messages if you accidentally specify a file instead of a directory

#### Enhanced MCP Server Management UI
The MCP (Model Context Protocol) server management interface has been completely redesigned with improved visual indicators:

- **Connection Status Icons**: 
  - ✓ Connected (green checkmark)
  - ○ Connecting... (gray radio button)
  - ▲ Disconnected/Needs authentication (yellow warning triangle)
  - ✗ Failed (red cross)

- **Server Capabilities Display**: Shows available capabilities (tools, resources, prompts) for each server

- **Streamlined Authentication Flow**: 
  - Automatic authentication prompts when needed
  - Re-authentication and clear authentication options
  - Better error handling and status feedback

### Improvements

#### Native Binary Installation
- Switched from npm-based installation to direct binary downloads from Google Cloud Storage
- Improved platform detection supporting Windows (x64), macOS (x64/arm64), and Linux (x64/arm64)
- Added checksum verification for downloaded binaries
- More reliable update mechanism with atomic symlink updates

#### File Reading Enhancements
- New token-based limits for file reading with clearer error messages
- `MaxFileReadTokenExceededError` class provides specific token count information
- Better handling of large files with more informative error messages suggesting use of offset/limit parameters

#### Hook System Extensions
- Added new hook types: `PreToolUse`, `PostToolUse`, and `Notification`
- Improved hook matching and filtering capabilities
- Better integration with MCP tool filtering

### Technical Changes

- Added `fine-grained-tool-streaming-2025-05-14` feature flag
- Improved stream handling with `PassThrough` streams
- Enhanced caching mechanisms for MCP client connections
- Better error handling for architecture-specific installations
- Removed legacy migration code for home directory configurations

### Bug Fixes

- Fixed symlink creation issues with atomic operations to prevent corruption
- Improved error handling for unsupported architectures
- Better cleanup of temporary files during installation
- Enhanced validation for directory operations

### Breaking Changes

- The native installer no longer uses npm packages (`@anthropic-ai/claude-cli-native-*`)
- Direct binary downloads are now used instead, which may affect custom installation scripts
