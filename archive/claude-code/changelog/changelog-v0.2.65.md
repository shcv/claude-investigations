# Changelog for version 0.2.65

Based on the comprehensive diff analysis, here's the changelog for Claude Code version 0.2.65:

## Version 0.2.65 Changelog

### New Features

#### 🛡️ Sandbox Mode for Bash Commands
- **New `sandbox` parameter** for the Bash tool that enables sandboxed command execution
- Commands run in sandbox mode are executed with restricted permissions - they can read files but cannot write to the filesystem or access the network
- **Key benefit**: Commands run with `sandbox=true` execute immediately without requiring user permission, providing a smoother user experience
- **Usage example**: `claude --sandbox ls -la` (read-only operations run immediately)

#### 📋 Enhanced Paste Detection
- Added support for bracketed paste mode in the terminal
- When pasting multi-line content, Claude Code now properly detects and handles pasted input
- Prevents accidental command execution when pasting code blocks

#### 🔧 Improved Permission Rules System
- Enhanced permission management UI with better organization
- New "Add permission rule" dialog for creating custom tool permissions
- Permission rules now support more granular control with specifiers (e.g., `Bash(ls:*)`)
- Permission rules can be saved to local project settings or shared project settings

#### 📝 Release Notes Integration
- New `release-notes` command to view changelog directly in the CLI
- Automatically fetches and displays recent version changes
- Falls back to offline changelog if network is unavailable
- **Usage**: `claude release-notes`

### Improvements

#### 🚀 Performance Enhancements
- Better handling of Unicode text in wrapped terminal output
- Improved text wrapping algorithm that correctly handles normalized Unicode characters
- More efficient handling of large output with JSON formatting support

#### 🔄 API Retry Logic
- Enhanced retry mechanism with optional error display control
- New `showErrors` parameter in retry configuration
- Better handling of API rate limits and context overflow errors

#### 💡 User Experience
- Added desktop notifications for idle sessions (triggers after 30 seconds of inactivity)
- New `tipsHistory` setting to track displayed tips
- Improved handling of API errors with clearer messaging

### Technical Improvements

#### 🏗️ Code Architecture
- Introduced `tree-kill` library for better process management
- New `eG0` class for managing macOS sandbox profiles
- Enhanced signal handling with proper cleanup on process termination
- Improved abort controller management for better command cancellation

#### 🔍 Tool Updates
- Bash tool description now dynamically includes sandbox mode instructions
- Better documentation of which commands require write access vs read-only
- Comprehensive lists of commands that should use sandbox mode

### Bug Fixes
- Fixed Unicode normalization issues in text wrapping
- Improved handling of incomplete escape sequences in terminal input
- Better cleanup of temporary sandbox profiles
- Fixed race conditions in process termination

### Developer Notes
- Added `sandbox` parameter to Bash tool schema
- New `hy()` function to check sandbox availability
- `Jr()` function to wrap commands with sandbox execution
- Enhanced process spawning with `detached: true` option for better process group management
