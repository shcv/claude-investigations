# Changelog for version 0.2.106


### External CLAUDE.md File Security
- **Added security dialog for external file references**: When CLAUDE.md files reference files outside the current working directory, users now see a warning dialog asking for explicit permission. This enhances security by preventing unauthorized access to files outside the project.
  - New settings: `hasClaudeMdExternalIncludesApproved` and `hasClaudeMdExternalIncludesWarningShown` track user preferences
  - Dialog options: "Yes, I trust this repository" or "No, disable external includes"
  - Keyboard shortcuts: Enter to confirm, Escape to disable external includes


### HTTP Headers Support for SSE Connections
- **Custom headers for Server-Sent Events (SSE)**: Added ability to specify custom HTTP headers when configuring SSE transport for MCP servers
  - New `headers` field in MCP server configuration
  - Interactive header input during server setup with format: `Header-Name: value`
  - Examples: `X-Api-Key: abc123`, `Authorization: Bearer token`


### Session History Improvements
- **Migrated from SQLite to JSONL format**: Session history is now stored in lightweight JSONL files instead of SQLite database
  - Sessions stored in `~/.claude/projects/[project-name]/[session-id].jsonl`
  - Improved performance and simpler file-based storage
  - Automatic migration of existing session data


### Enhanced macOS Terminal Detection
- **Better IDE detection on macOS**: Improved detection of Visual Studio Code, Cursor, and Windsurf when launched from their integrated terminals
  - Automatically finds the correct `code`, `cursor`, or `windsurf` command path
  - Works by traversing parent processes to find the IDE application


### Code Quality
- **Trimming improvements**: Added `trimKeepingFinalNewline` function to preserve final newlines while trimming trailing whitespace
- **Debounced operations**: Integrated lodash debounce for better performance in UI operations
- **React hooks**: Added `useOnUnmount` and `useDebouncedCallback` for cleaner component lifecycle management


### Prompt Caching
- **Flexible caching control**: Split `generateSummary` into two functions:
  - `generateSummaryWithCaching`: Enables prompt caching for better performance
  - `generateSummaryWithoutCaching`: Disables caching when needed


### File Editing Validation
- **Stricter validation for file edits**: The edit validation now specifically checks for the presence of file edit tools rather than just any tool use, preventing false positives

## Bug Fixes

- **Fixed parameter order**: Corrected parameter order in `collectIncludedPaths` function
- **Improved error handling**: Better error messages for invalid HTTP headers
- **Session file handling**: More robust session file creation and management

## Technical Changes

- Removed several database-related functions (`saveMessage`, `saveConversationChain`, `getConversationSummaries`, `saveConversationSummary`)
- Replaced SQLite-based history with file-based JSONL storage
- Added new imports for file system operations and stream handling
- Updated version string to "0.2.106"
