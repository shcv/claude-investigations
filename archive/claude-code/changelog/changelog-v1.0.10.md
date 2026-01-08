# Changelog for version 1.0.10

Based on my analysis of the diff file, here is the changelog for Claude Code version 1.0.10:

### New Features

#### Configurable Output Token Limit
- **New environment variable**: `CLAUDE_CODE_MAX_OUTPUT_TOKENS`
  - Allows customization of the maximum output tokens for Claude's responses
  - Default remains 32,000 tokens for most models
  - Automatically set to 8,192 for Claude 3.5 and Haiku models
  - Example usage: `export CLAUDE_CODE_MAX_OUTPUT_TOKENS=50000`

#### Enhanced Telemetry and Debugging
- **New environment variable**: `OTEL_LOG_USER_PROMPTS`
  - Enables logging of user prompts for debugging purposes
  - Example usage: `export OTEL_LOG_USER_PROMPTS=1`

### Improvements

#### Better Web Search Tracking
- Added comprehensive tracking for server-side tool usage
- New `server_tool_use` metrics include `web_search_requests` counter
- Improved usage statistics collection for web searches

#### Enhanced Markdown Rendering
- Added support for **strikethrough** text formatting in markdown
- Improved table rendering with proper alignment support (left, center, right)
- Better handling of complex table structures with dynamic column width calculation
- Enhanced image rendering in markdown (now shows the URL directly)

#### Performance Optimizations
- Added UUID v1, v3, v4, and v5 generation utilities for better request tracking
- Improved streaming response handling with better fallback detection
- Added `didFallBackToNonStreaming` tracking for API responses

#### Security and Error Handling
- Simplified refusal response handling for policy violations
- Removed OAuth authentication flow for MCP servers (streamlined authentication)
- Better error recovery for streaming tool use

### Technical Improvements

#### Code Organization
- Consolidated JSON parsing into a reusable utility function (`j5`)
- Improved message content merging with the new `eQ5` function
- Enhanced tool input validation and parsing with the `Ce` function
- Better separation of concerns for API response processing

#### ️ Developer Experience
- Added debug logging function `ikA` for better troubleshooting
- Improved process working directory access with `e70` import
- Enhanced date/time formatting utilities with comprehensive locale support

### Removed Features

#### Simplified Authentication
- Removed the complex OAuth authentication dialog for MCP servers
- Removed the `mcp-auth` command and its associated UI components
- Streamlined MCP server connection process

### Bug Fixes

- Fixed empty model response handling to provide meaningful fallback messages
- Improved tool use input validation to ensure proper string or object format
- Better handling of streaming responses that fall back to non-streaming mode

### Internal Changes

- Added comprehensive date manipulation utilities from date-fns library
- Improved telemetry data collection with more granular usage metrics
- Enhanced streaming infrastructure with PassThrough stream support
- Better modularization of utility functions


This version focuses on developer experience improvements, better configurability, and enhanced markdown rendering capabilities while streamlining the authentication process for MCP servers.
