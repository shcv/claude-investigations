# Changelog for version 0.2.55

# Claude Code v0.2.55 Changelog

## New Features

### Enhanced Tool Permission System
- **New permission checking functions** for file operations:
  - `d_()` - Validates read permissions before file access, providing clear error messages when permissions haven't been granted
  - `Vg()` - Validates write permissions before file modifications, ensuring proper access control
  
  These functions improve security by checking if Claude has been granted the necessary permissions before attempting file operations. Users will see messages like:
  - "Claude requested permissions to read from [path], but you haven't granted it yet."
  - "Claude requested permissions to write to [path], but you haven't granted it yet."

### Improved Memory Update Notifications
- **Simplified memory update display** with the new `Xk2()` component
  - Shows concise memory update notifications without diff details
  - Displays: "[MemoryType] updated in [path] · /memory to edit"
  - Cleaner UI that reduces visual clutter while maintaining essential information

### Better Error Handling for Context Limits
- **New `Tl2()` function** parses context limit errors to extract token information
  - Automatically detects when input length + max_tokens exceed the context limit
  - Extracts and returns structured data: `{ inputTokens, maxTokens, contextLimit }`
  - Helps users understand token usage and adjust their requests accordingly

## Configuration Changes

### MCP Tool Timeout
- **New environment variable**: `MCP_TOOL_TIMEOUT`
  - Default: 100,000,000ms (increased from standard timeout)
  - Allows longer-running MCP tool operations
  - Set via: `export MCP_TOOL_TIMEOUT=100000000`

### MCP Connection Timeout
- **Modified environment variable handling**: `MCP_TIMEOUT`
  - Default: 30,000ms (30 seconds)
  - Now properly handles empty string values with fallback

## UI Improvements

### Refactored Status Indicator System
- **Centralized status theme logic** with `EL1()` function
  - Cleaner code for determining UI themes based on operation status
  - Supports states: "tool-use", "responding", "thinking", and "normal"
  
- **New helper functions** for consistent UI rendering:
  - `im5()` - Returns appropriate spinner style for current status
  - `nm5()` - Returns color theme for current status
  - `am5()` - Returns message style for current status

## Technical Improvements

### Stream Handling
- Changed from default import to named import for Node.js streams
  - Before: `import pg4 from "stream"`
  - After: `import { Readable as ug4 } from "stream"`

### Process Management
- Relocated process.cwd import for better module organization
  - Now imported as: `import { cwd as NX0 } from "node:process"`

### Error Retry Logic
- Enhanced `Ak5()` function (formerly `Bb5()`) now checks for context limit errors
  - Automatically retries requests that fail due to context limits
  - Provides better handling of token-related errors

## Bug Fixes

- Fixed memory update notification display to be more concise and user-friendly
- Improved error message clarity for permission-related failures
- Better handling of empty MCP timeout environment variables

## Internal Changes

- Removed unused variables: `RG9`, `zi2`, `xZ`
- Removed redundant import: `Rn2` from "node:process"
- Added new utility function `Yf()` for internal operations
- Significant code refactoring with ~4254 function renames for better code organization
