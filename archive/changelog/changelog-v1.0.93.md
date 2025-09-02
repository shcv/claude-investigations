# Changelog for version 1.0.93

Now I have comprehensive information about all changes. Let me create the final changelog:

# Changelog for version 1.0.93

## 🎯 Highlights
Version 1.0.93 introduces cross-platform network sandboxing with Linux support, MCP SDK server integration, and Git checkpointing for preserving work-in-progress. Security is enhanced with command validation to prevent shell injection attacks.

## 🚀 New Features

### Linux Network Sandboxing
**What:** Network isolation now available on Linux using bubblewrap (bwrap)
**How to use:**
```bash
# Network sandboxing automatically activates when network restrictions are configured
# Works transparently with your existing network permission settings
```
**Details:**
- Uses bubblewrap for containerization on Linux systems
- Implements Unix domain socket proxy with socat for network isolation
- TCP-to-Unix forwarding maintains connectivity while enforcing restrictions
- **Evidence**: `zr2() at line 370283`, `Mq6() at line 370273`

### MCP SDK Server Support
**What:** Claude Code can now connect to MCP servers via SDK transport
**How to use:**
```bash
# Configure SDK-based MCP servers in your settings
# SDK transport complements existing HTTP and WebSocket options
```
**Details:**
- New "sdk" type for MCP server configurations
- Built-in transport class for SDK-based communication
- Seamless integration with existing MCP infrastructure
- **Evidence**: `class _D0 at line 387347`, `uBB() at line 388121`, `sendMcpMessage() at line 430038`

### Git Checkpointing (Experimental)
**What:** Automatically save work-in-progress to shadow Git repositories
**How to use:**
```bash
# Enable in settings when available (feature flag controlled)
# Shadow repos are automatically managed and cleaned up after 30 days
```
**Details:**
- Creates shadow repositories to preserve uncommitted changes
- Automatic cleanup of old shadow repos after one month
- Tracks last access time for efficient storage management
- **Evidence**: `ZmB() at line 419608`, `GmB() at line 419705`, `checkpointingShadowRepos at line 355280`

### Enhanced Command Security
**What:** Protection against IFS-based shell injection attacks
**How to use:**
```bash
# Automatic - Claude Code now validates commands for dangerous patterns
# Commands with IFS manipulation will require explicit approval
```
**Details:**
- Detects IFS variable usage that could bypass security validation
- Comprehensive safe flags validation for common shell commands
- Covers git, xargs, sed, sort, file, and other commands
- **Evidence**: `gN6() at line 374933`, `F1B variable at line 379461`

### Image Paste Keybinding for Windows/Linux
**What:** New keyboard shortcut for pasting images from clipboard
**How to use:**
```bash
# Press Alt+V to paste images directly from your clipboard
# Works in all contexts where image input is supported
```
**Details:**
- Platform-specific keybinding (Alt+V on Windows/Linux, Shift+Tab on macOS)
- Consistent with system clipboard conventions
- **Evidence**: `Eu variable at line 363750`

## 🔧 Improvements

### Enhanced NO_PROXY Support
**What:** Better proxy bypass logic for excluded hosts
**Details:**
- New dedicated functions for checking NO_PROXY environment variable
- Intelligent URL matching against proxy bypass patterns
- Supports wildcards, domain suffixes, and port-specific rules
- **Evidence**: `VJ4() at line 354027`, `KJ4() at line 354030`

### Network Sandboxing Refactoring
**What:** Unified cross-platform network isolation
**Details:**
- Single entry point for both macOS and Linux sandboxing
- Better error messages for uninitialized proxy states
- Improved proxy port management with parameterized functions
- **Evidence**: `Er2() at line 370309` replaces platform-specific `Bs2()`

## 🐛 Bug Fixes

### Permission Mode Persistence
**What:** Fixed permission mode settings not persisting across sessions
**Details:**
- Corrected property name mismatch (saved as "mode" but read as "defaultMode")
- Permission modes now correctly persist when changed
- Added helper function for cleaner source validation
- **Evidence**: `setMode case at line 344856` now uses `defaultMode` consistently

## 🔄 Other Changes

### Simplified Timeout Messages
Error messages for request timeouts no longer include technical hints about API_TIMEOUT_MS, providing cleaner user experience.

### Internal Refactoring
- Feature flag checking system enhanced with dedicated function
- MCP-related constants added for token management
- Various function renamings for better code organization
