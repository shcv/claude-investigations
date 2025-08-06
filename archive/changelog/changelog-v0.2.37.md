# Changelog for version 0.2.37

## Claude Code v0.2.37 Changelog

### New Features

#### 🎉 `/release-notes` Command
A new slash command that displays release notes for all versions of Claude Code.

**Usage:**
```bash
/release-notes
```

This command shows the complete release history with version numbers and their corresponding changes. The release notes are now always available and enabled by default (`isEnabled: !0`), replacing the previous version-specific implementation.

#### 🔧 Enhanced `config add/remove` Commands
The `claude config add` and `claude config remove` commands now support adding or removing multiple values at once.

**New capabilities:**
- Add multiple values to array-based configuration options in a single command
- Values can be separated by commas or spaces
- The command now tracks the count of items being added/removed
- Items are automatically deduplicated using Set operations
- Lists are sorted alphabetically after modifications

**Examples:**
```bash
# Add multiple tools to allowed tools
claude config add allowedTools Read,Write,Edit

# Remove multiple patterns from ignore patterns  
claude config remove ignorePatterns "*.log" "*.tmp" "build/"

# Works with both global and project configs
claude config add --global mcpServers server1,server2,server3
```

### Improvements

#### 🔔 Kitty Terminal Notification Support
Added native notification support for Kitty terminal emulator using the OSC 99 protocol.

**How it works:**
- When using Kitty terminal, Claude Code can now send desktop notifications
- Notifications include both title and body text
- Automatically detected when `preferredNotifChannel` is set to "auto"
- Can be explicitly enabled with `claude config set preferredNotifChannel kitty`

#### 🎯 Better Terminal Detection
Improved terminal detection for Kitty:
- Now checks `TERM` environment variable for "kitty" string earlier in the detection chain
- More reliable Kitty terminal identification

### Technical Improvements

#### Error Message Enhancement
- New `IM3` function provides more detailed and user-friendly error messages for validation failures
- Better formatting for parameter type mismatches, missing required parameters, and unexpected parameters

#### Architecture Tool Removal
- Removed the experimental "Architect" tool that was disabled in the previous version
- Cleaned up related code and dependencies

### Bug Fixes

- Fixed duplicate notification method tracking
- Improved error handling for array-based configuration operations
- Better validation for configuration keys

### Internal Changes

- Updated release notes data structure from `Gn` to `yW1`
- Refactored notification system from `Y01` to `H01` with improved telemetry
- Removed unused functions related to word-level diff display
- Code cleanup: removed 23 deprecated functions and added 19 new implementations
