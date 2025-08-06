# Changelog for version 1.0.48

Based on my analysis of the diff, here is the changelog for Claude Code version 1.0.48:

## Claude Code v1.0.48 Changelog

### New Features

#### Tool Permission Modes
Added new permission modes for tool execution, giving users more control over how Claude interacts with their system:

- **`default`** - Standard mode with confirmation prompts for potentially sensitive operations
- **`plan`** - Plan mode where Claude outlines steps before executing
- **`acceptEdits`** - Automatically accepts file edits without confirmation  
- **`bypassPermissions`** - Bypasses permission prompts for all tool operations

You can switch between modes during a conversation to control the level of interaction required.

#### PreCompact Hook
A new `PreCompact` hook event that runs before conversation compaction occurs. This allows custom scripts to:
- Modify custom instructions before compaction
- Block compaction by returning exit code 2
- Provide feedback to users about the compaction process

Example usage:
```bash
# In your hooks configuration
# Exit code 0: stdout becomes custom compact instructions
# Exit code 2: blocks compaction
# Other codes: shows stderr to user but continues
```

#### Enhanced Spinner Messages
Added support for custom spinner words/phrases that display during long-running operations, providing more engaging feedback while waiting for tasks to complete.

### Installation Improvements

#### Removed Launcher Script System
- Removed the complex bash launcher script (`claude-v0.0.8.sh`) that previously managed version selection
- Simplified to direct symlink approach at `~/.local/bin/claude`
- Cleaner installation with fewer moving parts

#### Better Installation Diagnostics
The installation process now provides more detailed diagnostics:
- Checks if the claude binary is a valid executable
- Verifies symlink targets exist and are valid
- Provides clearer error messages when PATH configuration is needed
- More helpful instructions for fixing installation issues

### Internal Improvements

- Added utility functions for number operations (clamp, shuffle arrays, etc.)
- Improved hook execution with better error handling and cancellation support
- Enhanced process management for subprocess execution
- Better signal handling for cancelled operations

### Bug Fixes

- Fixed issue with duplicate imports (`stream` and `node:stream`)
- Removed unused metrics opt-out checking functionality
- Cleaned up obsolete code paths related to organization metrics
- Improved error messages for hook execution failures

### Breaking Changes

- The launcher script system has been removed. If you relied on the version management features of the launcher script, you'll need to manage versions manually or use the built-in update mechanism.
