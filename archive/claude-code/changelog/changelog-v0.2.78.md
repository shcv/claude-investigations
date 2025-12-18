# Changelog for version 0.2.78

# Claude Code v0.2.78 Changelog

## New Features

### OAuth Token Refresh Support
- **Added automatic OAuth token refresh functionality** for MCP (Model Context Protocol) connections
  - When an OAuth access token expires, Claude Code will now automatically attempt to refresh it using the refresh token
  - This prevents authentication interruptions during long sessions
  - Usage: This happens automatically in the background when using MCP servers that require OAuth authentication

### Configurable Telemetry Settings
- **New environment variables for controlling telemetry data collection**:
  - `OTEL_METRICS_INCLUDE_SESSION_ID` (default: true) - Controls whether session IDs are included in metrics
  - `OTEL_METRICS_INCLUDE_VERSION` (default: false) - Controls whether the app version is included in metrics
  - `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` (default: true) - Controls whether account UUIDs are included in metrics
  
  Example usage:
  ```bash
  # Disable session ID tracking
  OTEL_METRICS_INCLUDE_SESSION_ID=false claude
  
  # Enable version tracking
  OTEL_METRICS_INCLUDE_VERSION=true claude
  ```

## Improvements

### Enhanced OAuth Infrastructure
- Added OAuth authorization server metadata discovery following the `.well-known/oauth-authorization-server` specification
- Improved error handling for OAuth token refresh failures with detailed error messages
- Added fallback OAuth configuration for servers that don't support metadata discovery

### Code Organization
- Refined import statements to use more specific imports (e.g., `import { PassThrough as ou9 } from "stream"` instead of importing the entire stream module)
- Added proper process imports using the `node:` prefix convention

## Bug Fixes

### OAuth Token Management
- Fixed potential issues with expired OAuth tokens by implementing proper refresh logic
- Added validation to ensure refresh tokens are only used when available
- Improved error recovery when token refresh fails

## Internal Changes

- Added constant `LI3 = 60000` (60 seconds timeout value)
- Updated MCP protocol version to "2024-11-05"
- Version bump to 0.2.78

## Technical Details

The OAuth token refresh implementation includes:
- Automatic detection of expired tokens based on `expiresAt` timestamp
- Support for OAuth 2.0 refresh token grant type
- Proper handling of client credentials (client_id and client_secret)
- Telemetry events for tracking refresh success/failure rates
