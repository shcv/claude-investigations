# Changelog for version 1.0.62


### 🆕 Enhanced `/add-dir` Command
The `/add-dir` command has been completely redesigned with an interactive UI and persistent storage options:

**Usage:** `/add-dir <directory-path>`

- **Interactive Selection**: When adding a directory, you now get three options:
  - `Yes, for this session` - Adds the directory only for the current session
  - `Yes, remember` - Adds the directory and saves it to local settings for future sessions
  - `No` - Cancels the operation

- **Visual Feedback**: The command now displays:
  - The directory path being added in cyan
  - A clear explanation that Claude will be able to read files and make edits in this directory
  - Better error messages if the path is invalid

- **Persistent Storage**: When choosing "Yes, remember", the directory is saved to your local settings and will be available in future sessions


### 🆕 Agent Mentions with @-syntax
You can now mention agents directly in your prompts using the `@agent-` syntax:

**Usage:** `@agent-<agent-type>`

Example:
```
Please help me refactor this code @agent-refactoring-specialist
```

The system will automatically detect and process agent mentions in your messages.


### 🆕 Session Start Hooks
A new hook system that runs when starting a new session, allowing for automatic context injection and initialization tasks. This runs automatically on startup unless using `--continue`, `--resume`, or `--teleport` flags.


### 🆕 Directory Path Autocomplete (Internal Enhancement)
Added intelligent directory path completion that:
- Supports `~` for home directory expansion
- Provides up to 10 directory suggestions
- Filters hidden directories (starting with `.`)
- Caches results for 5 minutes for better performance


### Tool Selection UI Enhancements
The tool selection interface has been significantly improved:

- **MCP Server Grouping**: MCP tools are now grouped by server for easier management
- **New Categories**: Tools are now organized into:
  - Read-only tools
  - Edit tools
  - Execution tools
  - MCP tools (new dedicated category)
  - Other tools (new category for miscellaneous tools)
- **Advanced Options**: Replaced "Show individual tools" with "Show advanced options" that reveals:
  - MCP servers with tool counts
  - Individual tool selection
- **Better Navigation**: Header sections are now non-interactive and properly skipped during keyboard navigation
- **Escape to Cancel**: Press `Esc` to cancel tool selection and use initial tools


### Ripgrep Integration Improvements
- Centralized ripgrep path resolution with better quoting for paths containing spaces
- More robust handling of bundled vs system ripgrep
- Improved alias generation in shell snapshots with proper escaping


### Settings Watcher Optimization
The settings file watcher has been streamlined:
- Removed redundant state tracking
- Simplified change detection logic
- More efficient memory usage
- Better event handling for file changes


### Performance Enhancements
- Connection check interval increased to 30 seconds (from 1 second on non-Mac platforms)
- Added caching for directory listing operations (5-minute TTL)
- Optimized settings watcher to reduce memory footprint


### Code Quality
- Better error handling for agent mentions
- Improved type safety with centralized MCP tool detection
- More consistent path resolution across the codebase
- Enhanced stream handling with proper PassThrough imports


### Fixed
- Proper handling of spaces in ripgrep paths on all platforms
- Correct escaping of quotes in shell snapshot generation
- Better error messages for invalid session IDs in `--print` mode


### ️ Architecture
- New `SessionStart` hook type added to the hook system
- Centralized MCP tool identification with `Is1()` function
- Improved modularity for agent mention processing
- Better separation of concerns in the `/add-dir` command implementation
