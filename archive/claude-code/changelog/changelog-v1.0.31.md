# Changelog for version 1.0.31

Based on my analysis of the diff for Claude Code version 1.0.31, here's the detailed changelog:

# Claude Code v1.0.31 Changelog


### Native Installation Command
- **New `claude install` command**: Install Claude Code's native build directly from the CLI
  - Usage: `claude install [options]`
  - Supports `--force` flag to override installation checks
  - Automatically cleans up old npm installations before installing the native build
  - Provides visual feedback during installation process with status updates
  - Shows shell integration setup notes after successful installation


### Enhanced Conversation Analytics
- Added token usage tracking for conversations with detailed breakdowns:
  - Human vs assistant message tokens
  - Tool request and response tokens by tool type
  - Duplicate file read detection and optimization metrics
  - Attachment token counts by type
  - Local command output token tracking
  - Percentage breakdowns for all token categories


### Security Enhancements
- New security-focused system prompt that emphasizes defensive security practices
- Enhanced malicious code detection in file reading operations
- Updated security instructions to refuse creating, modifying, or improving potentially malicious code


### ️ Shell Integration
- Improved shell alias management with better conflict resolution
- Enhanced detection and cleanup of existing claude aliases
- Support for ZDOTDIR environment variable for zsh configurations
- Automatic removal of old/conflicting claude aliases during setup


### Documentation Updates
- Updated documentation URL structure with new sub-pages:
  - `quickstart`, `common-workflows`, `ide-integrations`
  - `mcp`, `github-actions`, `sdk`, `third-party-integrations`
  - `amazon-bedrock`, `google-vertex-ai`, `corporate-proxy`
  - `llm-gateway`, `devcontainer`, `iam`, `monitoring-usage`
  - Expanded coverage for Extended thinking, image pasting, and `--resume` flag


### ️ Session Management
- Improved transcript loading with better summary handling
- Enhanced session file organization by working directory
- More efficient duplicate message detection
- Better handling of sidechain conversations


### Auto-updater Improvements
- Native installer now sets `autoUpdaterStatus` to "installed" after successful installation
- Better error handling and retry logic for version locks
- Enhanced cleanup of stale npm installations and symlinks
- More robust directory creation for lock files


### Stop Signal Support
- Added "Stop" to the list of supported signal types for MCP (Message Control Protocol)
- Enables better control flow for long-running operations


### Theme Support
- Added dark theme configuration option for error dialogs
- Better visual consistency across the application

## Bug Fixes

- Fixed issues with transcript summary generation for conversations without summaries
- Improved error handling in configuration file parsing with proper async/await flow
- Fixed race conditions in session file writes
- Better handling of missing or corrupt session files

## Internal Changes

- Refactored main entry point to use proper async initialization
- Improved process cleanup with dedicated launcher symlink removal
- Enhanced token counting algorithms for more accurate usage metrics
- Better separation of concerns for installation and setup logic


### Installing Claude Code
```bash
# Install the latest native build
claude install

# Force reinstall even if already installed
claude install --force
```


### Shell Integration
After installation, the tool will automatically:
1. Clean up any old npm global installations
2. Remove conflicting aliases from shell config files
3. Add the new `claude` alias pointing to `~/.claude/bin/claude`
4. Provide instructions for sourcing your shell config

The installation process provides clear visual feedback:
```
✓ Claude Code successfully installed!
Version: 1.0.31
Location: ~/.claude/bin/claude
Next: Run claude --help to get started
```
