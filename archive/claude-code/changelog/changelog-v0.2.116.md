# Changelog for version 0.2.116

### New Features

#### Enhanced IDE Integration
- **New WebSocket IDE Transport**: Added support for WebSocket-based IDE connections, enabling more robust communication with IDEs like JetBrains
- **Improved IDE Connection Management**: Better handling of IDE connections with automatic reconnection and timeout management
- **IDE Extension Installation**: Enhanced automatic installation of IDE extensions with version checking and compatibility validation

#### Configuration & Management
- **Cleanup Period Configuration**: New `cleanupPeriodDays` setting in managed settings to control how long logs and project data are retained (default: 30 days)
  ```json
  {
    "cleanupPeriodDays": 30
  }
  ```
- **Automatic Log Cleanup**: Claude Code now automatically cleans up old log files and project data based on the configured cleanup period
- **Enhanced Environment Control**: New `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` environment variable to disable telemetry, auto-updates, and error reporting

#### API Key Management
- **API Key Helper TTL**: New `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` environment variable to control API key caching duration
- **Better Authentication Handling**: Improved handling of 401 authentication errors with automatic cache clearing

### Improvements

#### Tool Enhancements
- **Better Tool Descriptions**: Enhanced descriptions for Glob and Grep tools with clearer guidance on when to use each tool
- **Multi-Edit Tool**: Improved documentation emphasizing preference for MultiEdit over single Edit operations
- **Thinking Display**: Enhanced visual presentation of Claude's thinking process with better formatting and borders

#### Error Handling & Reliability
- **Retry Logic**: Improved retry mechanism that handles authentication failures by refreshing credentials
- **Error Reporting**: Added protection against recursive error reporting with a flag to prevent infinite loops
- **Better Error Messages**: More descriptive error messages for IDE integration failures

#### ️ Project Management
- **Project Directory Structure**: New project storage location at `/projects` for better organization
- **Environment Detection**: Added functions to detect production vs development environments
- **External vs Internal Classification**: New system to classify whether code is running externally or internally

### Bug Fixes

- **Fixed GitHub Actions Workflow**: Updated workflow to properly handle issue titles containing @claude mentions
- **Fixed IDE Connection Status**: More accurate reporting of IDE connection status in the UI
- **Fixed Cleanup Logic**: Proper handling of empty directories during cleanup operations

### Technical Changes

- **Removed Legacy Functions**: Cleaned up unused functions related to sandbox execution and old configuration paths
- **Streamlined Imports**: Consolidated and optimized module imports
- **Code Organization**: Better separation of concerns with dedicated functions for environment detection and configuration management

### Breaking Changes

None - This release maintains backward compatibility with existing configurations and workflows.

### Notes for Users

- If you're using IDE integration, you may need to restart your IDE after updating to ensure proper connection
- The new cleanup feature will automatically remove logs older than 30 days by default. Adjust `cleanupPeriodDays` in managed settings if you need different retention
- For environments with restricted network access, use `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` to disable all non-essential network requests
