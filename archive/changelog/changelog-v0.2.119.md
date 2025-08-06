# Changelog for version 0.2.119

# Claude Code v0.2.119 Changelog

## New Features

### IDE Onboarding Experience
A comprehensive onboarding screen has been added for first-time users installing Claude Code in their IDE. This feature:

- **Automatic Display**: Shows automatically when Claude Code is installed in an IDE for the first time
- **Per-Terminal Tracking**: Tracks whether onboarding has been shown for each terminal type (VSCode, IntelliJ, etc.)
- **Quick Start Guide**: Displays essential keyboard shortcuts and usage tips:
  - `Cmd+Esc` to launch Claude Code
  - `Cmd+Option+K` (Mac) or `Ctrl+Alt+K` (Windows/Linux) to insert @File references
  - View and apply file diffs directly in your editor
- **Version Display**: Shows the installed version of Claude Code
- **Restart Reminder**: For plugin installations, reminds users to restart their IDE (may require multiple restarts)
- **Exit Options**: Press the designated key again to exit the onboarding screen

### Enhanced IDE Detection
The IDE detection functionality has been improved with an optional parameter:

```javascript
// Previously: dn() - only returned valid IDEs for current workspace
// Now: pn(includeAll) - can optionally return all detected IDEs
```

When `includeAll` is `true`, the function returns all detected IDE instances, not just those valid for the current workspace. This enables better IDE discovery and selection.

## Improvements

### Better Error Handling
- **Tool Result Mapping**: The tool result mapping function now includes try-catch error handling, preventing crashes when tool results cannot be properly mapped
- **Async Error Wrapper**: New `ZT` function provides a standardized way to handle async errors, returning empty arrays on failure instead of throwing

### Message Content Merging
New functionality for intelligently merging message content:

- **Smart Tool Result Merging**: When merging assistant messages, tool results with string content are now intelligently combined with subsequent text blocks
- **Content Preservation**: Maintains proper formatting with double newlines between merged content sections
- **Array Content Support**: Properly handles both string and array-based message content formats

## Technical Changes

### Import Updates
- **Process Module**: Changed from default import to named import for better tree-shaking: `import { cwd as Rj0 } from "node:process"`
- **Stream Module**: Added `PassThrough` import from the stream module for enhanced streaming capabilities
- **URL Module**: Added `fileURLToPath` import for better file path handling

### Code Organization
- **Memoization**: The MCP client initialization function `cs2` has been converted to a memoized variable `ss2` using the `k2` wrapper for better performance
- **Permission Handling**: Simplified the permission mode function by removing intermediate parsing, now directly passes CLI arguments

## Bug Fixes

### Tool Permission Configuration
The permission configuration for allowed/disallowed tools has been simplified, removing unnecessary parsing that could cause issues with complex tool patterns.

### IDE Detection Reliability
Fixed potential issues with IDE detection when multiple IDEs are running by improving the workspace folder matching logic and process ID validation.

## Notes for Users

This update focuses on improving the first-run experience for IDE users and enhancing the reliability of tool operations. The new onboarding screen provides essential information for getting started with Claude Code in your IDE, while the improved error handling ensures more stable operation when working with tools and external resources.
