# Changelog for version 1.0.19

# Claude Code v1.0.19 Changelog

### MCP Resource Support (@mentions)
- **New @mention syntax for MCP resources**: You can now reference MCP (Model Context Protocol) resources directly in your messages using the `@server:resource` syntax
  - Example: `@myserver:config.json` to reference a config file from an MCP server
  - Resources are automatically fetched and included as context when mentioned
  - Autocomplete support for discovering available MCP resources (up to 15 suggestions)

### Agent-Specific Todo Lists
- **Isolated todo lists per agent**: When using the Task tool to spawn sub-agents, each agent now maintains its own separate todo list
  - Todo lists are stored as `{session-id}-agent-{agent-id}.json` files
  - Prevents todo list conflicts between parent and child agents
  - Each agent can track its own progress independently

### Compact Summary Messages
- **New compact summary display**: A new message type that shows condensed summaries of long responses
  - Displays "Compact summary" header with the summarized content
  - In transcript view, shows the full summary text
  - In other views, shows hint "(ctrl+r to expand)" for accessing full content

### Enhanced Text Editing

#### Logical Line Navigation
- **New logical line movement commands**: Navigate by actual line breaks rather than wrapped lines
  - `upLogicalLine()`: Move cursor up one logical line (to previous newline)
  - `downLogicalLine()`: Move cursor down one logical line (to next newline)
  - `startOfLogicalLine()`: Jump to start of current logical line
  - `endOfLogicalLine()`: Jump to end of current logical line
  - `firstNonBlankInLogicalLine()`: Jump to first non-whitespace character in logical line
  - `deleteToLogicalLineEnd()`: Delete from cursor to end of logical line

These commands are useful when working with long lines that wrap in the terminal, allowing navigation based on actual line breaks in the text rather than visual line wrapping.

### Shell Command Execution
- **Background process management**: Enhanced support for running commands in the background
  - New `moveToBackground()` function for shell commands
  - Returns shell ID when moving a process to background
  - Example output: "Command running in background (shell ID: 123)"

### Command Metadata
- **Read-only command flagging**: Commands can now be marked as `read_only`
  - New `read_only` boolean field in command schemas
  - Helps identify commands that won't modify the filesystem or make network calls
  - Improves command safety and permission handling

### Performance
- **Adaptive connection checking**: Connection status polling interval now adjusts based on environment
  - Default: 1 second polling interval
  - Extended to 30 seconds in certain runtime environments for reduced overhead

## Bug Fixes

- Fixed duplicate comment issue in codebase
- Improved file path handling for agent-specific data storage
- Enhanced error handling for MCP resource fetching

## Technical Changes

- Removed unused stream imports and process-related functions
- Consolidated file storage paths for better organization
- Added UUID generation support for unique identifiers
- Improved sandbox detection (though currently disabled by default)
