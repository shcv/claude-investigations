# Changelog for version 1.0.11

# Claude Code v1.0.11 Changelog


### Enhanced MCP OAuth Authentication
- **Interactive MCP authentication flow**: The `/mcp` command now provides an interactive interface for authenticating with MCP servers that support OAuth
  - Navigate through MCP servers using arrow keys
  - Press Enter to manage authentication for SSE-type servers
  - Options to authenticate, re-authenticate, or clear existing authentication
  - Example: Run `/mcp`, use arrow keys to select a server, press Enter to authenticate


### New `/upgrade` Command
- Added `/upgrade` command for Max subscription enrollment
  - Automatically opens the upgrade page in your browser
  - Streamlines the login process after upgrading
  - Example: `/upgrade` - Opens claude.ai/upgrade/max and prompts for login


### Improved Authentication Handling
- **Multi-source authentication detection**: Better handling of authentication conflicts
  - Detects when multiple authentication methods are configured (e.g., ANTHROPIC_AUTH_TOKEN vs claude.ai login)
  - Shows clear warnings about which authentication source is being used
  - Provides instructions for resolving conflicts


### Subscription Recommendations
- **Personalized subscription suggestions**: Claude Code now shows targeted subscription recommendations based on your organization's settings
  - Recommendations for Pro, Max 5x ($100/mo), and Max 20x ($200/mo) plans
  - Smart display logic that limits how often recommendations are shown
  - Example output:
    ```
    With the $100/mo Max plan, use Sonnet 4 as your daily driver with predictable pricing. • /upgrade to sign up
    ```


### Performance Enhancements
- **File reading cache**: Implemented a smart caching system for file reads
  - Caches up to 1000 files with automatic eviction
  - Tracks file modification times to ensure cache validity
  - Significantly improves performance when repeatedly accessing the same files


### WSL Networking Support
- **Improved WSL host detection**: Better support for Windows Subsystem for Linux environments
  - Automatically detects the correct host IP in WSL environments
  - Falls back gracefully when detection fails
  - Respects `CLAUDE_CODE_IDE_HOST_OVERRIDE` environment variable


### OAuth Port Management
- **Dynamic port allocation**: OAuth authentication now uses dynamic port allocation
  - Tries random ports in the 45000-45999 range
  - Falls back to port 45123 if needed
  - Prevents port conflicts during authentication


### Opus 4 Limitation for Claude Pro Users
- Claude Pro users are now restricted from using Opus 4 models in Claude Code
- Attempting to set model to Opus 4 will show:
  ```
  Invalid model. Claude Pro users are not currently able to use Opus 4 in Claude Code. The current model is now Sonnet 4.
  ```
- This encourages Pro users to upgrade to Max plans for Opus 4 access


### Enhanced Error Messages
- More specific error messages for API key issues
  - Differentiates between external API key errors and managed API key errors
  - Example: "Invalid API key · Fix external API key" vs "Invalid API key · Fix managed API key"


### Better Visual Feedback
- New system message formatting for better visibility
- Improved notebook cell editing rejection messages with syntax highlighting
- Enhanced MCP server status display with color-coded connection states

## Bug Fixes

- Fixed duplicate imports and variable declarations
- Removed obsolete telemetry functions
- Cleaned up unused authentication state management code
- Improved error handling in OAuth token revocation

## Technical Changes

- Migrated from synchronous to asynchronous file reading patterns
- Improved module organization with better separation of concerns
- Enhanced TypeScript/JavaScript interoperability
- Better handling of Node.js stream APIs
