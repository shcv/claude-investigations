# Changelog for version 1.0.4

# Claude Code v1.0.4 Changelog

### Enhanced Model Support
- **New Model Recognition**: Added support for recognizing additional Claude models including:
  - Claude Sonnet 4
  - Claude Opus 4
  - Claude 3.7 Sonnet
  - Claude 3.5 Sonnet
  - Claude 3.5 Haiku

### Improved Working Directory Management
- **PWD Environment Support**: The CLI now recognizes the `PWD` environment variable as an additional working directory, expanding file operation permissions beyond just the current working directory
- **Multiple Working Directories**: Files can now be accessed from both the current working directory and the PWD location

### Sandbox Mode for Bash Commands
- **New `sandbox` parameter**: Execute bash commands in a restricted environment without requiring user approval
  - When `sandbox=true`: Commands run immediately without approval dialogs but with restricted filesystem write and network access
  - Automatically retries with `sandbox=false` if permission or network errors occur
  - Optimized for read-only operations like `ls`, `cat`, `git status`, `pwd`, etc.

Example usage scenarios:
```bash
# These commands can run with sandbox=true (no approval needed)
ls -la
git status
cat file.txt
pwd
echo $HOME

# These require sandbox=false (user approval required)
npm install
git commit
touch newfile.txt
curl https://api.example.com
```

### Streaming Tool Use Display
- **Enhanced streaming feedback**: When Claude is preparing to use a tool, the interface now shows animated status messages that cycle through states like "Streaming input", "Still streaming input", "Megastreaming", etc.
- **Improved tool preview**: Shows the tool name and partial parameters while the tool use is being streamed

### Telemetry and Metrics System
- **Centralized metrics**: New unified system for tracking CLI usage metrics including:
  - Session counts
  - Lines of code modified (additions/removals)
  - Pull requests created
  - Git commits created
  - Cost tracking
  - Token usage
  - Code editing tool decisions (accept/reject)

### Custom Command Title Detection
- **Smart command titles**: Custom slash commands now extract titles from markdown headers in the command content, limiting to 100 characters for better display

### File Operations
- **Symlink resolution**: The `cd` command now resolves symlinks using `realpath`, ensuring you navigate to the actual directory location
- **Enhanced WSL support**: Improved detection of Windows Subsystem for Linux (WSL) environments with better path handling for `.claude/ide` directories
- **Notebook cell handling**: Better support for reading and editing individual cells in Jupyter notebooks

### Configuration and Environment
- **API Provider display**: New configuration info panel showing:
  - Current API provider (AWS Bedrock, Google Vertex AI)
  - Custom base URLs if configured
  - AWS/GCP regions
  - Proxy settings
  - Authentication status

### Tool Validation
- **Stricter input parsing**: Tool inputs now use proper schema validation with partial parsing support for streaming scenarios
- **Better error handling**: Improved error messages when tool rendering fails during streaming

### Version Management
- **Concurrent version cleanup**: Old CLI versions are now cleaned up more efficiently with proper locking
- **Protected versions**: The system protects currently running versions and symbolic links (latest, known-good) from deletion
- **Configurable retention**: Keeps only the 2 most recent versions by default

## Technical Improvements

- **Modular telemetry**: Metrics system is now initialized separately and can be disabled
- **Better proxy support**: Consolidated proxy configuration using `HTTPS_PROXY` or `HTTP_PROXY` environment variables
- **Enhanced MCP approval**: Improved migration of MCP (Model Context Protocol) server approval settings
- **React context for feature flags**: New context system for managing feature availability

## Bug Fixes

- Fixed issues with file permission checks in additional working directories
- Improved handling of malformed tool inputs during streaming
- Better error recovery during version installation and cleanup
- Fixed duplicate imports and unused variables

## Breaking Changes

None - This release maintains backward compatibility with existing workflows and configurations.
