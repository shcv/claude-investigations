# Changelog for version 1.0.58


### New Features

#### Agent Color Coding
- Agents now have color-coded identification in the interface
- New color palette: `claude`, `success`, `bashBorder`, `planMode`, `autoAccept`, `warning`, `permission`, `error`
- Color assignments persist per agent type for consistency
- The `general-purpose` agent remains uncolored

#### PDF File Support
- Added native PDF reading capability to the Read tool
- PDF files up to 32MB can now be processed directly
- PDF content is displayed visually as Claude Code is multimodal

#### Enhanced Permission Messages
- New `DETAILED_PERMISSION_MESSAGES` environment variable
- When enabled, provides more context about which specific commands are pre-approved
- Permission prompts now show reminders of allowed commands for each tool type

#### OAuth 2.0 Client Authentication
- Added comprehensive OAuth 2.0 client authentication support
- Supports multiple authentication methods:
  - `client_secret_basic` (HTTP Basic Auth)
  - `client_secret_post` (form-encoded)
  - `none` (public clients)
- New error handling for OAuth flows with specific error types

#### Bash Command Prefix Support
- New `CLAUDE_CODE_BASH_PREFIX` environment variable
- Allows prefixing all bash commands with custom wrapper scripts
- Useful for sandboxing or monitoring command execution


### Improvements

#### Performance
- Added LRU cache support with configurable size limits
- New telemetry for tracking attachment computation duration
- Improved abort signal handling with configurable timeouts (default 50ms)

#### MCP Server Integration
- Better connection status reporting for MCP servers
- New `JyB` function provides clear connection status messages:
  - "✓ Connected"
  - "⚠ Needs authentication"
  - "✗ Failed to connect"
  - "✗ Connection error"

#### Telemetry Enhancements
- Added tracking for non-interactive sessions
- New `print` mode detection in API success metrics
- TTY detection for better usage analytics


### API Changes

#### Tool Permission Context
- New `I1Q` function to get tool-specific permission rules
- Enhanced `G1Q` function for generating contextual permission messages
- Permission rules now support content-specific messaging

#### Agent Management
- Agent color preferences stored in new `agentColorMap`
- Color index rotation for automatic assignment
- `uz0` function for getting agent colors
- `e31` function for setting custom agent colors


### Bug Fixes

- Fixed duplicate code comments in some scenarios
- Improved error handling for OAuth token refresh flows
- Better cleanup of temporary shell execution files


### Removed Features

- Removed several unused internal functions and variables
- Cleaned up deprecated OAuth implementation code
- Removed redundant file reading state management


### Developer Notes

- Version updated from 1.0.57 to 1.0.58
- Structural similarity remains high at 99.0%
- 76 additions, 19 deletions, 11 modifications across the codebase
