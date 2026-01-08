# Changelog for version 0.2.66

# Claude Code v0.2.66 Changelog

### Todo List Management Tools
Added comprehensive todo list functionality with two new tools:

**TodoWrite** - Update and manage your task list during coding sessions
- Create, update, and track todos with status (pending, in_progress, completed) and priority (high, medium, low)
- Automatic progress tracking with visual indicators
- Use it to organize complex multi-step tasks and maintain focus

**TodoRead** - View your current todo list
- Quickly check pending tasks and current progress
- Shows focused view by default, with verbose option for full list
- Helps maintain context across long coding sessions

Example usage:
```
# Claude will proactively use these tools to track progress
# You can also explicitly ask to see or update the todo list
"Show me my todo list"
"Add a todo to implement dark mode"
```

### Enhanced Permission System
- Improved permission handling for Bash commands with smarter rule suggestions
- Better detection and handling of command injection attempts
- More informative permission debug information display
- Rule suggestions now based on actual command analysis

### Settings Enhancement
- Added `stressTestingFraction` to user settings options
- This appears to be for internal testing/debugging purposes

### User Experience
- Better visual formatting for permission prompts
- Clearer distinction between local and project settings descriptions
- Enhanced permission decision reasoning display

### Architecture Changes
- Improved file handling for external tool integrations
- Better error handling in file save operations
- More robust command prefix detection and validation

### New Dependencies
- Added imports for `execSync`, `execFile`, and `spawn` from child_process
- Added `PassThrough` from stream module
- Added path and filesystem utilities (`extname`, `relative`, `existsSync`, `statSync`)

### Internal Improvements
- Refactored permission checking logic for better maintainability
- Enhanced rule suggestion generation
- Improved handling of workspace and organization roles
- Better support for admin and billing role detection

## Bug Fixes
- Fixed issues with command injection detection
- Improved error handling in file operations
- Better handling of edge cases in permission flows

## Notes
The todo list feature is designed to be used proactively by Claude to track complex tasks and maintain context. It's stored locally in your project's `.claude/todos/` directory and persists across sessions.
