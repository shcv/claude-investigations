# Changelog for version 0.2.56

Looking at this diff between Claude Code v0.2.55 and v0.2.56, here's the changelog:

## Claude Code v0.2.56 Changelog

### New Features

#### Enhanced Permission System
- **New granular permission rules**: The permission system now supports more specific rule configurations with the ability to grant permissions for specific command patterns
  - Example: You can now allow `bash` commands that start with specific prefixes like `npm:*` or `git:*`
  - Rules can be configured through both CLI arguments and local settings
  
#### Supervisor Mode
- Added a new "supervisorMode" setting to the configuration options
- This appears to be a new operational mode for Claude Code (specific functionality details would need further investigation)

#### Environment Variable Overrides Display
- The welcome screen now displays active environment variable overrides when present, including:
  - Custom API keys (shown as `sk-ant-…` with partial masking)
  - Prompt caching status (shows "off" when disabled via `DISABLE_PROMPT_CACHING`)
  - API timeout settings (from `API_TIMEOUT_MS`)
  - Maximum thinking tokens (from `MAX_THINKING_TOKENS`)
  - Custom API base URL (from `ANTHROPIC_BASE_URL`)

#### WebSearch Tool Enhancement
- WebSearch tool now supports domain filtering:
  - `allowed_domains`: Restrict search results to specific domains
  - `blocked_domains`: Exclude results from specific domains
  - Example usage: Search only within documentation sites or exclude certain sources

#### Project-wide MCP Server Settings
- New `enableAllProjectMcpServers` configuration option
- Allows enabling all MCP (Model Context Protocol) servers for a project at once

### Performance Improvements

#### Intelligent Retry Backoff
- Retry delays now include a random jitter (up to 25% of base delay) to prevent thundering herd problems
- This helps distribute retry attempts when multiple operations fail simultaneously

#### Host Validation Optimization
- Added caching for CLAUDE.md host validation to reduce repeated lookups
- Improves performance when checking URLs referenced in project documentation

### Technical Improvements

#### Enhanced Spinner Animation System
- Refactored the progress indicator system with new `Ov5` function
- Supports different spinner styles, colors, and update intervals based on context
- More flexible configuration for tool-use, responding, and thinking states

#### Stream Processing
- Updated stream handling to use proper Node.js stream imports
- Added new `gk` function for consuming async iterators completely

### Bug Fixes

- Fixed duplicate comment issue (as mentioned in recent commits)
- Improved error handling in permission checking system
- Better handling of aborted operations with proper cleanup

### Internal Changes

- Refactored permission checking logic to use a rule-based system
- Updated tool configuration with new tools array structure
- Constants for line limits now properly defined (`m91` and `j91` both set to 2000)
- Better separation of concerns in the permission validation flow

### Breaking Changes

None identified - the update maintains backward compatibility while adding new optional features.
