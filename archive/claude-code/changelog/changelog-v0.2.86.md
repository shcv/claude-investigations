# Changelog for version 0.2.86

### New Features

#### Managed Settings Support
- Added support for managed settings configuration file at:
  - macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
  - Other systems: `/etc/claude-code/managed-settings.json`
- This allows system administrators to configure Claude Code settings centrally

#### Enhanced Error Handling
- Improved error message rendering with new `DIFF_REJECTED` status detection
- Better handling of tool use errors with dedicated error message rendering
- Error messages now properly distinguish between different error types and provide clearer feedback

### API Changes

#### New Functions for Session Tracking
- `WN0(cwd)`: Set the current working directory for the session
- `YN0(cost, duration, durationWithoutRetries, inputTokens, outputTokens, cacheReadTokens, cacheCreationTokens)`: Track API usage metrics including:
  - Total cost in USD
  - API call durations (with and without retries)
  - Token usage breakdown (input, output, cache read, cache creation)

#### Improved Current Directory Detection
- New `d0()` function provides more robust current working directory detection with fallback handling

### Bug Fixes

- Fixed duplicate import issues (removed redundant stream imports)
- Removed obsolete error handling classes and functions
- Cleaned up unused variables and functions related to session management

### Internal Changes

- Refactored non-interactive session handling with new `propagateErrors: false` option
- Simplified message persistence by removing complex database transaction logic
- Streamlined error content formatting for better consistency
- Updated version string from "0.2.85" to "0.2.86"

### Removed Features

- Removed database-backed message history storage functions (`Kl9`, `uT1`, `eu0`, `Zm0`)
- Removed progress message filtering (`s91`)
- Removed custom error class `hp` in favor of standardized error handling
- Removed system policies configuration (previously at `/etc/claude-code/policies.json`)

This update focuses on improving error handling, adding managed settings support, and cleaning up deprecated functionality while maintaining backward compatibility for core features.
