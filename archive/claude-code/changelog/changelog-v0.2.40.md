# Changelog for version 0.2.40

### New Features

#### Interactive Confirmation Prompts
- Added a new `ConfirmInput` component that provides Y/n prompts for user confirmations
- Supports customizable default choices and keyboard shortcuts (Y/n or y/N)
- Automatically submits on Enter key based on the default choice

#### Enhanced Shell Prompt Integration (OSC 133)
- Added support for OSC 133 terminal sequences for better shell integration
- New prompt markers automatically inserted to track command execution:
  - `OSC 133;A` - marks prompt start
  - `OSC 133;B` - marks prompt end  
  - `OSC 133;C` - marks command start
  - `OSC 133;D` - marks command end
- Includes bracketed paste mode support (`OSC ?2026h/l`)
- Improves terminal experience with better command boundary detection

#### Improved Allowed Tools Management
- Redesigned the `/approved-tools` interface with better visual feedback
- Added confirmation dialogs when deleting allowed tools
- Shows "Press [key] again to exit" hints for better UX
- Improved escape key handling throughout the permission flows

### Security Enhancements

#### URL Validation for WebFetch
- WebFetch tool now requires URLs to be "provided directly by the user in the current or a previous message"
- Added URL extraction from user messages to maintain a whitelist of allowed URLs
- Prevents potential security issues from arbitrary URL fetching

#### Custom HTTP Headers Support
- New environment variable `ANTHROPIC_CUSTOM_HEADERS` for adding custom headers to API requests
- Supports multi-line header definitions with `name: value` format
- Useful for proxy authentication or custom API configurations

### UI/UX Improvements

#### Better Mode Indicators
- Reorganized status bar to show mode indicators more clearly
- Added `# to memorize` indicator for memory mode
- Improved layout of bash mode and command hints
- Vim INSERT mode indicator now properly hides other hints when active

#### Enhanced File Writing
- Added tab-to-spaces conversion for better cross-editor compatibility
- Improved file writing with proper encoding handling

### Bug Fixes

- Fixed release notes history (removed duplicate entries for v0.2.27)
- Improved terminal output handling with better escape sequence filtering
- Enhanced error handling in file operations
- Better support for environments without terminal resize events

### Technical Improvements

- Added `PassThrough` stream support for better data handling
- Improved MCP (Model Context Protocol) configuration parsing
- Enhanced terminal rendering with proper OSC sequence support
- Better memory management for long-running sessions

### Developer Notes

The codebase shows significant refactoring in several areas:
- Terminal rendering engine now supports prompt markers
- Permission management UI components have been modularized
- Stream handling has been improved with proper Node.js stream imports
- Configuration parsing is more robust with better error handling
