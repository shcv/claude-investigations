# Changelog for version 0.2.117

# Claude Code v0.2.117 Changelog

## New Features

### Background Task Management 🚀
A new `tasks` command has been added to list and manage background tasks. This allows you to:
- View all running background tasks
- Monitor task status (running, completed, or failed)
- View stdout/stderr output from tasks in real-time
- Kill running tasks

**Usage:**
```bash
claude tasks
```

The interface shows:
- Task ID, status, runtime, and command
- Live stdout output (last 5 lines)
- Live stderr output (last line)
- Exit codes for completed tasks

### Long-Running Command Handling ⏱️
When executing commands that take a long time, Claude Code now presents three options:
1. **Continue waiting** - Keep waiting for the command to complete
2. **Run in the background** - Move the command to a background task
3. **Kill command** - Terminate the command

This prevents the CLI from being blocked by long-running processes.

### Enhanced Print Mode (`--print`) 📄
The print mode has been significantly improved with new options:

**Session Management:**
- `--continue` - Continue the most recent conversation
- `--resume <session-id>` - Resume a specific conversation by UUID

**System Prompts:**
- `--system-prompt <prompt>` - Replace the default system prompt
- `--append-system-prompt <prompt>` - Append to the existing system prompt

**Examples:**
```bash
# Continue last conversation
claude --print --continue "What were we discussing?"

# Resume specific session
claude --print --resume 550e8400-e29b-41d4-a716-446655440000 "Let's continue"

# Custom system prompt
claude --print --system-prompt "You are a Python expert" "Write a sorting algorithm"
```

## Improvements

### Output Truncation
Large command outputs are now intelligently truncated to prevent overwhelming the display:
- Shows the first and last portions of output
- Displays line count for truncated sections
- Format: `[X lines truncated]` in the middle

### Stream Processing
Added `PassThrough` stream support for better handling of streaming data in background tasks.

## Bug Fixes

### Import Path Corrections
- Fixed Node.js process import to use named imports (`import { cwd } from "node:process"`)
- Properly scoped crypto imports for UUID generation

## Internal Changes

### Code Organization
- Removed obsolete functions (`A50`, `FZ6`) related to model override handling
- Consolidated message formatting utilities (`MR5`, `$Z6`)
- Improved task output management with dedicated truncation logic

### Performance
- More efficient handling of long-running processes
- Better memory management for large command outputs
- Streamlined background task monitoring
