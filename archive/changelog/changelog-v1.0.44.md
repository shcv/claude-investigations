# Changelog for version 1.0.44

Based on my analysis of the diff file, here's the detailed changelog for Claude Code version 1.0.44:

## Claude Code v1.0.44 Changelog

### New Features

#### 1. **Export Conversation Command** 🆕
- Added new `/export` command to save conversation history
- Usage: `/export [filename]` or just `/export`
- Export methods:
  - **Copy to clipboard** - Copies the entire conversation to system clipboard
  - **Save to file** - Saves conversation as a text file in the current directory
- Automatically generates filename based on conversation content and timestamp if not specified
- Example: `conversation-2024-12-16-implement-dark-mode.txt`

#### 2. **Process Suspension Support (Ctrl+Z)** 🆕
- Added ability to suspend Claude Code using `Ctrl+Z` (like traditional Unix applications)
- When suspended, displays: "Claude Code has been suspended. Run `fg` to bring Claude Code back."
- Resume with `fg` command to return to Claude Code
- Note: `Ctrl+U` now handles undo operations (previously `Ctrl+Z`)

#### 3. **GitHub Actions OAuth Authentication** 🆕
- Added OAuth token support for GitHub Actions setup
- New authentication flow creates long-lived tokens (1 year expiry)
- Stores OAuth tokens as `CLAUDE_CODE_OAUTH_TOKEN` secret
- Environment variable support: `CLAUDE_CODE_OAUTH_TOKEN`
- Improved security for GitHub Actions integration

#### 4. **MCP Resource Management Improvements**
- Enhanced MCP (Model Context Protocol) resource handling
- New resource listing and reading capabilities
- Better integration with MCP servers and resources
- Support for `strictMcpConfig` parameter for stricter configuration validation

### Enhancements

#### GitHub Actions Integration
- Added `actions: read` permission to workflow templates
  - Enables Claude to read CI/CD results on pull requests
  - Improved visibility into build and test status
- Updated GitHub Actions setup flow with better error handling
- New OAuth token option in setup wizard for users without API keys

#### Tool Improvements
- **Removed TodoRead tool** - Todo functionality streamlined
- Better handling of tool permissions and validation
- Improved MCP tool discovery and execution
- Enhanced structured output formats for various tools

#### UI/UX Improvements
- Better handling of long input with automatic text truncation
- Improved clipboard integration across platforms
- Enhanced error messages with platform-specific instructions
- Smoother OAuth authentication flow with visual feedback

### Technical Changes

#### Authentication
- New OAuth flow implementation with:
  - Browser-based authentication
  - Automatic token storage
  - Refresh token support
  - 1-year token expiry option
- Support for inference-only OAuth tokens
- Better token validation and error handling

#### Platform Support
- Improved clipboard commands for different platforms:
  - macOS: `pbcopy`
  - Windows: `clip`
  - Linux: `xclip` or `wl-copy`
  - WSL: `clip.exe`

#### Error Handling
- Better error messages for:
  - Failed clipboard operations
  - OAuth authentication issues
  - GitHub Actions setup problems
- Platform-specific troubleshooting instructions

### Bug Fixes
- Fixed issues with stream handling in various tools
- Improved stability of GitHub Actions setup process
- Better handling of suspended/resumed state
- Fixed edge cases in conversation export

### Internal Improvements
- Cleaner separation of OAuth and API key authentication paths
- Better state management for complex workflows
- Improved error tracking and telemetry
- Enhanced TypeScript type definitions

### Breaking Changes
- `TodoRead` tool has been removed - todo functionality integrated differently
- `Ctrl+Z` now suspends the application instead of undo (use `Ctrl+U` for undo)

### Notes for Users

1. **Exporting Conversations**: Use `/export` to save important conversations or share them with others. The export includes all messages, tool uses, and responses in a readable format.

2. **GitHub Actions Setup**: When setting up GitHub Actions, you can now choose between:
   - Using an existing Anthropic API key
   - Creating a new API key
   - Using OAuth authentication (recommended for better security)

3. **Process Control**: The new suspend/resume feature works like traditional Unix applications, making Claude Code more familiar for terminal users.
