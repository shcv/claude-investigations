# Changelog for version 1.0.52


### New Features

#### Metrics Opt-Out Detection
- Added automatic detection of organization-level metrics opt-out preferences
- Claude Code now checks if your organization has disabled metrics logging and respects that setting
- The check is cached for 1 hour to minimize API calls
- If the check fails, metrics are disabled by default for privacy

#### Enhanced Shell Snapshot Management
- **Improved shell snapshot creation** with better error handling and file locking
- **Automatic cleanup** of old shell snapshots (older than configured threshold)
- Shell snapshots are now timestamped with random suffixes to avoid conflicts
- Added file locking to prevent concurrent access issues
- Shell snapshot files are automatically cleaned up on shutdown

#### Todo List Reminders
- **Automatic todo reminders** to help you stay on track with your tasks
- Claude will remind you about your todo list after 20 turns without using TodoWrite
- Reminders appear at most every 10 turns to avoid being intrusive
- Example: After extended conversations, Claude will prompt: "You have X pending tasks in your todo list"

#### System Reminders
- New `system-reminder` functionality for injecting context-aware guidance
- Allows Claude to provide system-level hints and reminders during conversations


### Improvements

#### Terminal Title Management
- Added `CLAUDE_CODE_DISABLE_TERMINAL_TITLE` environment variable
- Set this to disable automatic terminal title updates if they interfere with your workflow
- Usage: `export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=1`

#### Performance Enhancements
- Implemented caching mechanism with configurable TTL for frequently accessed data
- Reduced redundant API calls through intelligent caching
- Cache automatically refreshes stale data in the background

#### Security & Stability
- Enhanced error handling for shell operations
- Better cleanup of temporary resources
- Improved file locking mechanisms to prevent race conditions


### Technical Changes

#### API Updates
- New endpoint for checking organization metrics preferences: `/api/claude_code/organizations/metrics_enabled`
- Added proper error handling and fallback behavior for API failures

#### Code Refactoring
- Removed legacy date/time formatting utilities (replaced with more efficient implementations)
- Cleaned up unused imports and dependencies
- Streamlined tool permission decision logic


### Bug Fixes
- Fixed potential race conditions in shell snapshot creation
- Improved cleanup of locked files on process termination
- Better handling of missing or corrupted shell configuration files


### Configuration
- New timeout configurations:
  - Shell snapshot creation: 10 seconds (configurable)
  - Metrics API check: 5 seconds
  - Cache refresh: 1 hour for metrics status


### Usage Examples

**Disabling terminal title updates:**
```bash
# Add to your shell configuration
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=1
claude chat
```

**Todo reminders in action:**
```
User: Help me refactor this codebase
Claude: I'll help you refactor the codebase. Let me create a todo list to track our progress.
[... 20+ turns of conversation without using TodoWrite ...]
Claude: [Reminder: You have 5 pending tasks in your todo list. Use /todos to view them.]
```

**Shell snapshot behavior:**
- Snapshots are created automatically when needed
- Old snapshots (>60 minutes by default) are cleaned up automatically
- Each snapshot is locked to prevent conflicts with concurrent Claude sessions

This update focuses on improving the developer experience with better task management, respecting privacy preferences, and ensuring stable shell environment handling.
