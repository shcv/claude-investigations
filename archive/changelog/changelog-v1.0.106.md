# Changelog for version 1.0.106

## 🎯 Highlights
Version 1.0.106 introduces conversation compacting for better performance and readability, reduces terminal flickering with synchronized updates, and enhances Windows path handling with improved Cygwin integration.

## 🚀 New Features

### Conversation Compacting
**What:** Automatically compact conversation history to improve performance and maintain context
**How to use:**
```bash
# Compacting happens automatically during long conversations
# Visual boundary shows: "Conversation compacted · ctrl+r for history"
```
**Details:**
- Creates compact boundary markers in conversation flow
- Filters messages from last compact point for better performance
- Shows visual dividers with "Conversation compacted" messaging
- Accessible via ctrl+r to view full history
- **Evidence**: `Z9B() at line 391737`, `EG1() at line 391749`, `Lf6() at line 391752`, `c_1() at line 391759`

### Terminal Synchronized Updates
**What:** Reduces terminal flickering during output rendering using ANSI escape sequences
**How to use:**
```bash
# Automatic - no user action required
# Terminal output now renders more smoothly
```
**Details:**
- Implements synchronized update protocol (`\x1B[?2026h` and `\x1B[?2026l`)
- Wraps terminal clearing and writing operations
- Eliminates visual artifacts during screen updates
- **Evidence**: `beginSynchronizedUpdate at line 557`, `endSynchronizedUpdate at line 558`

### Enhanced Windows Path Support
**What:** Improved Windows drive letter path handling and bidirectional Cygwin integration
**How to use:**
```bash
# Windows paths like /c/Users/name now work correctly
# Automatic conversion between Windows and Unix paths
```
**Details:**
- Added Windows drive letter pattern matching (`/^\/[a-z]\//i`)
- New `SXA()` function for `cygpath -w` conversion
- Bidirectional path conversion support
- Better compatibility in Cygwin environments
- **Evidence**: `L9B() at line 392483`, `SXA() at line 344435`

### Message Processing Enhancement
**What:** New assistant message processing function for improved filtering
**How to use:**
```bash
# Automatic - improves message handling internally
# Better conversation flow and response processing
```
**Details:**
- New `CQB()` function handles assistant message processing
- Enhanced message filtering capabilities
- Improved conversation state management
- **Evidence**: `CQB() at line 388855`

## Other changes

### Security Improvements
**What:** Tightened command execution security by removing pattern-matching tools from safe command list
**Details:** Removed `"grep"` and `"rg"` from the safe commands array to prevent potential security issues with pattern matching operations

### Terminal Rendering Optimization
**What:** Enhanced compact boundary UI component for better visual representation
**Details:** Converted `ibB()` function from text processing to React component for displaying conversation compact boundaries with proper styling and user feedback
