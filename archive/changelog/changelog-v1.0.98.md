# Changelog for version 1.0.98

## 🎯 Highlights
This release focuses on architectural improvements to session persistence, removes the LS tool in favor of existing alternatives, and enhances UI component organization with better todo list management.

## 🚀 New Features

### Enhanced Session Persistence
**What:** Complete rewrite of session persistence system to support remote server synchronization
**How to use:**
```bash
# Session data now automatically syncs with remote servers when available
# Uses CLAUDE_CODE_WEBSOCKET_AUTH_FILE_DESCRIPTOR for authentication
export CLAUDE_CODE_WEBSOCKET_AUTH_FILE_DESCRIPTOR=3
claude --session-id my-session
```
**Details:**
- Sessions can now be persisted to and restored from remote servers
- Cross-platform file descriptor support (Darwin/FreeBSD use `/dev/fd/`, Linux uses `/proc/self/fd/`)
- Automatic conflict detection and resolution for concurrent session modifications
- Improved error handling with detailed logging for session operations
- **Evidence**: `VVA() at line 352480`, `KVA() at line 352534`, `$VA() at line 352860`, `MI9() at line 352437`

### Todo List UI Improvements
**What:** Dedicated todo rendering component with expanded view capability
**How to use:**
```bash
# Todo lists now have enhanced visual presentation
# Use Ctrl+T to toggle expanded todo view (when available)
claude
/todos "Implement feature X" "Test feature Y"
```
**Details:**
- New dedicated `Pb1` component for consistent todo list rendering
- Enhanced checkbox visualization with proper status indicators
- Expandable todo view for better task management
- Improved integration across different UI contexts
- **Evidence**: `Pb1() at line 399903`, expanded todos feature at `line 400288`

### SlashCommand Tool Framework (Experimental)
**What:** New tool that enables executing slash commands from within the conversation context
**How to use:**
```bash
# Note: Currently disabled by default - experimental feature
# When enabled, allows tools to execute slash commands
```
**Details:**
- Complete command parsing infrastructure with `PS()` function
- Permission checking system for cross-execution security
- Designed for future tool-to-command bridging capabilities
- Currently disabled (`isEnabled() returns false`) pending further development
- **Evidence**: `ZA1 tool definition at line 414675`, `VuB() at line 414597`, `AL5() at line 414466`

## 🔄 Improvements

### Enhanced Command Execution
**What:** All slash command executions now include autocheckpoint support
**Details:**
- Commands automatically create checkpoints when executed
- Improved session state management across command boundaries
- Better integration with conversation flow tracking
- **Evidence**: `AL5() at line 414466` with autocheckpoint parameter

### Cross-Platform File Descriptor Support
**What:** WebSocket authentication now works correctly on Darwin, FreeBSD, and Linux
**Details:**
- Darwin/FreeBSD systems use `/dev/fd/` path format
- Linux systems continue using `/proc/self/fd/` path format
- Improved error messages for invalid file descriptor configurations
- **Evidence**: `MI9() at line 352437` with platform detection

### Atomic File Operations
**What:** New secure file copying utility for configuration management
**Details:**
- Temporary file creation with process ID and timestamp
- Atomic rename operations to prevent corruption
- Proper cleanup on failure scenarios
- **Evidence**: `qvB() at line 407217`

## 🗑️ Removed Features

### LS Tool Removal
**What:** The LS (directory listing) tool has been completely removed
**Migration:**
```bash
# Old way (no longer available):
# LS tool for directory listing

# New alternatives:
# Use Bash tool for directory operations
Bash("ls -la /path/to/directory")
Bash("find /path -name '*.js'")

# Use Glob tool for pattern matching
Glob("**/*.py")

# Use Read tool for individual files when paths are known
Read("/path/to/specific/file.txt")
```
**Details:**
- Removed to streamline tool set and reduce redundancy
- Bash tool provides more flexible directory listing capabilities
- Glob tool offers superior pattern-matching for file discovery
- **Evidence**: Removed `nU tool definition at line 391316`, `eb6() at line 391425`, related functions

### Removed Internal Functions
**What:** Various internal functions removed as part of codebase cleanup
**Details:**
- Removed unused checkpointing UI components
- Cleaned up obsolete session management utilities
- Eliminated redundant path processing functions
- **Evidence**: Removed `TPB() at line 395476`, `RY1() at line 395486`, `gmB() at line 420941`

## ⚠️ Breaking Changes

### Directory Listing Workflow
**Impact:** Users who relied on the LS tool for directory exploration must adapt their workflow
**Solution:** Use Bash tool with standard shell commands (`ls`, `find`, `tree`) or Glob tool for pattern matching

### Session Persistence Format
**Impact:** Session data format may have changed due to remote persistence capabilities
**Solution:** Existing local sessions should migrate automatically, but backup important session data before upgrading
