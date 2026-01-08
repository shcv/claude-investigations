# Changelog for version 0.2.39

# Claude Code v0.2.39 Changelog

### Administrative Controls
- **Bug Command Control**: Administrators can now disable the `bug` command via the `claude_code_disable_bug_command` configuration setting. When disabled, users will see the message "This command has been disabled by your administrator."

### Tool Management
- **Dynamic Tool Allowlisting**: New functions for managing allowed tools:
  - Tools specified via CLI flags (`--allowed-tools`) are now properly tracked separately from the configuration-based allowed tools
  - Multiple tools can be added to the allowed list in batch operations
  - Improved handling of tool permissions with clearer separation between CLI-specified and configuration-based tools

### OAuth and Role Management  
- **User Role Tracking**: OAuth authentication now fetches and stores user roles from the API:
  - Organization role (e.g., "developer")
  - Workspace role (e.g., "workspace_developer") 
  - Roles are persisted in the configuration for future reference

### Cost Warning Controls
- **Conditional Cost Warnings**: Cost threshold warnings are now only shown to users with appropriate roles (non-developer roles)
- **Environment Variable Override**: Cost warnings can be disabled entirely via the `DISABLE_COST_WARNINGS` environment variable

### Command Prefix Detection
- **Enhanced Command Detection**: New logic to handle multiple subcommand prefixes when detecting available commands
- **Better Error Handling**: Improved detection of command injection attempts with clearer validation

### Shell Management
- **Shell Initialization**: The persistent shell now properly changes to the initial working directory after sourcing shell configuration files
- **Improved Buffer Management**: Removed redundant stdout/stderr buffer tracking in the shell implementation

### Telemetry Controls
- **Telemetry Opt-out**: Telemetry can now be completely disabled via the `DISABLE_TELEMETRY` environment variable

### Auto-updater Controls
- **Auto-updater Opt-out**: Auto-updater functionality can be disabled via the `DISABLE_AUTOUPDATER` environment variable

### New Configuration Storage
- Added storage for auto-compact configuration with customizable token thresholds
- New configuration key: `tengu_auto_compact_config`

### OAuth Endpoints
- Added new endpoint for fetching user roles: `https://api.anthropic.com/api/oauth/claude_cli/roles`

### Performance
- Optimized state management in the main UI component to reduce unnecessary re-renders
- Improved async state handling for write file permissions

### Code Quality
- Better separation of concerns between OAuth authentication and API key generation
- Cleaner error handling with more specific error messages in OAuth flows
- Simplified HTTP request handling by switching from fetch to axios for OAuth operations

## Bug Fixes

- Fixed potential race conditions in state updates for write file allowed directories
- Improved handling of shell exit conditions with better cleanup

## Version
Updated from 0.2.38 to 0.2.39
