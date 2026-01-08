# Changelog for version 0.2.53

# Claude Code v0.2.53 Changelog

### Web Fetch Tool
- **New capability**: Claude can now view URLs that you paste into the conversation
- Simply paste a URL and Claude will fetch and analyze the content
- Improved handling of URL redirects with better host validation

### Background Task Management
- **New `/tasks` command**: View and manage long-running background tasks
- Press `↓` key to quickly view running tasks from the main prompt
- Tasks show real-time status updates and unread output indicators
- Kill background tasks with `/tasks kill <task_id>`
- Retrieve task output with `/tasks output <task_id>`

### Terminal.app Integration (macOS)
- Automatic setup for Option as Meta key in Terminal.app
- Creates backup of Terminal preferences before making changes
- Restores settings automatically if setup is interrupted
- New setup process similar to existing iTerm2 integration

### MCP Server Setup
- Simplified command input: Now accepts full command with arguments and environment variables in a single step
- Smart parsing of commands like `API_KEY=abc123 NODE_ENV=dev node server.js`
- Reduced setup steps from 6 to 4 for faster configuration
- Better examples and guidance for complex commands with quotes

### User Experience
- Added visual indicator for number of running background tasks in the prompt
- New `hasSeenTasksHint` preference to track if user has been shown task shortcuts
- Improved handling of backslash+return key combination tracking

### Image Detection
- Fixed JPEG file extension detection
- Changed from checking `.jpg` to properly checking both `jpg` and `jpeg` extensions (without dots)
- Ensures proper handling of all JPEG image files

## Technical Changes

- Updated to version 0.2.53
- Added comprehensive changelog parsing functionality
- Improved URL validation to prevent redirect attacks
- Better error handling for Terminal.app preference modifications
