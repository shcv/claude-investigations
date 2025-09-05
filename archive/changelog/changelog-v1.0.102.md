# Changelog for version 1.0.102

Based on my analysis of the diff and verification against both versions, here's the changelog for Claude Code v1.0.102:

# Changelog for version 1.0.102

## 🎯 Highlights
Enhanced background task management with improved architecture, better user interface terminology, and new structured input/output parsing for background tasks.

## 🚀 New Features

### Background Task Input/Output Parsing
**What:** Added support for structured input/output in background tasks using XML-like tags
**How to use:**
```bash
# Background tasks can now parse and display structured content
# with <background-task-input> and <background-task-output> tags
claude --some-command &
```
**Details:**
- Enables better formatting and organization of background task communication
- Supports tagged content for clearer task progress tracking
- Improves integration between background processes and the main conversation
- **Evidence**: `GA1() at line 410790` and `bbB() at line 410805` (new functions not present in v1.0.100)

### Task Creation Progress Feedback
**What:** Added visual feedback when creating background tasks
**Details:**
- Shows "Creating background task…" message during task initialization
- Provides better user awareness of task creation process
- **Evidence**: New message at `line 429262` (not found in v1.0.100)

## Improvements

### Enhanced Task Management Architecture
**What:** Improved background task system with better state management and filtering
**Details:**
- Refactored from direct global state access to parameterized app state management
- Added filtering for shell-type tasks with `(G) => G.type === "shell"` logic
- Better separation between running and completed tasks
- More reliable task state tracking and updates
- **Evidence**: `BV5(A) at line 395850` vs `zF5() at line 395605` in v1.0.100

### Refined User Interface Terminology
**What:** Updated terminology from "bash shells" to "tasks" throughout the interface
**Details:**
- Changed "List and manage background bash shells" to "List and manage background tasks"
- Updated "No background shells currently running" to "No tasks currently running"
- More inclusive language supporting different types of background operations
- Consistent terminology across all user-facing messages
- **Evidence**: `line 411750` vs `line 408227` in v1.0.100, `line 411633` vs `line 408178` in v1.0.100

### Improved Task Processing Functions
**What:** Enhanced task processing with new filtering and state management functions
**Details:**
- Replaced `U1B()` and `E1B()` functions with `g1B()` and `u1B()` functions
- Better encapsulation through app state parameter passing
- More robust task state transitions and error handling
- **Evidence**: Functions `g1B() at line 395854` and `u1B() at line 395863` (architecture change from v1.0.100)
