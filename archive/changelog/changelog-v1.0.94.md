# Changelog for version 1.0.94

Now I have enough information to create the comprehensive changelog. Let me compile all the verified findings into the final changelog format.

# Changelog for version 1.0.94

## 🎯 Highlights
Version 1.0.94 introduces comprehensive performance monitoring with new warnings for large agent descriptions and MCP tools, significantly improves security with sophisticated sed command validation, and enhances the permission system with dynamic update capabilities.

## 🚀 New Features

### Performance Context Warnings
**What:** New warning system that monitors context consumption from custom agents and MCP tools
**How to use:**
```bash
# Warnings appear automatically when thresholds are exceeded
# Agent descriptions > 15,000 tokens will trigger a warning
# MCP tools > 25,000 tokens will trigger a warning
```
**Details:**
- Monitors cumulative token count of custom agent `whenToUse` descriptions
- Tracks total context consumed by MCP tool definitions
- Shows top contributors by token consumption for optimization
- Integrated with existing CLAUDE.md size warnings into unified system
- **Evidence**: `kY1() at line 399348`, `XV5() at line 399376`, `FV5() at line 399400`, `WSB() at line 399442`

### Advanced sed Command Security
**What:** Complete replacement of sed command validation with sophisticated parsing that blocks dangerous operations
**How to use:**
```bash
# Safe sed commands work normally
claude "Use sed to replace text in file.txt"

# Dangerous operations are now blocked:
# - File writes (s///w, w command)
# - Command execution (s///e, e command)
# - Multiple expression exploits
```
**Details:**
- Prevents sed commands from writing to files or executing shell commands
- Parses actual sed expressions instead of using regex patterns
- Detects and blocks write operations (`w`), execute operations (`e`), and dangerous flags
- **Evidence**: `P1B() at line 379595`, `mS6() at line 379676`, `hS6() at line 379611`, `gS6() at line 379638`

## 🔧 Improvements

### Dynamic Permission Updates
**What:** Tools can now suggest and apply permission changes during execution
**Details:**
- Permission prompts can include tool-suggested rules
- "Yes, and apply suggestions" option for streamlined workflows
- Automatic directory access rule creation when accessing folders
- Context-aware permission suggestions based on access patterns
- **Evidence**: `qW1() at line 430572`, `Cz1() at line 348277`, `CR5() at line 421430`

### Enhanced Error Messages
**What:** Improved error handling for PDF files
**Details:**
- Clear message when PDF exceeds page limits
- Guidance to edit message and retry with smaller PDF
- **Evidence**: `bb6 variable at line 391166` in error handler `B_1()`

### Checkpointing Status Display
**What:** Better visibility into checkpointing errors and status
**Details:**
- Shows checkpointing errors in status display
- Indicates when checkpointing is disabled
- Displays save failures with error messages
- **Evidence**: `KV5() at line 399769`

### Memory File Selection UI
**What:** Redesigned memory file selector interface
**Details:**
- Improved organization of memory file options
- Better visual hierarchy for nested imports
- Clearer descriptions of file locations
- **Evidence**: `sb1() at line 400461` replacing `hb1()`

## 🐛 Bug Fixes

### Git Command Flag Handling
**What:** Fixed handling of numeric flags in git commands
**Details:**
- Git commands with numeric flags like `git log -5` now work correctly
- Improved flag parsing to distinguish between numeric flags and invalid options
- **Evidence**: `lS6() at line 380053`, added check for `/^-\d+$/` pattern at line 1404

## 📚 Internal Changes

### Model Deprecation Updates
**What:** Added deprecation dates for additional Claude models
**Details:**
- Added `claude-3-opus-20240229` with deprecation date January 5th, 2026
- Added `claude-3-5-sonnet-20241022` with deprecation date October 22, 2025
- Added `claude-3-5-sonnet-20240620` with deprecation date October 22, 2025
- **Evidence**: `My2 object at line 366970`, `jy2 object at line 367622`

### Settings Processing
**What:** Enhanced --settings flag processing during initialization
**Details:**
- Settings are now processed earlier in the startup sequence
- Supports both JSON strings and file paths
- Better error messages for invalid settings
- **Evidence**: `wS5() at line 433801`, initialization check at lines 1537-1541

## 🔄 Removed Features

### Local Memory Type Selection
**What:** Simplified memory file selection by removing separate "Local" memory type
**Details:**
- CLAUDE.local.md functionality appears to be consolidated
- Memory selection UI simplified from three types to unified approach
- **Evidence**: Removed functions `cv1()`, `fb1()`, `VyB variable`, `hb1()`, `rz5()`, `AD5()`
