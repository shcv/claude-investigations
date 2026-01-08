# Changelog for version 0.2.126

# Claude Code v0.2.126 Changelog

### Enhanced GitHub App Installation Workflow
The GitHub app installation process has been significantly improved with better error handling and user guidance:

- **Prerequisite Checks**: The CLI now performs comprehensive checks before attempting GitHub app installation:
  - Verifies GitHub CLI (`gh`) is installed
  - Checks authentication status
  - Validates required permissions (specifically the "workflow" scope)
  
- **Detailed Error Messages**: When issues are encountered, users now receive specific instructions:
  ```
  # If GitHub CLI is not installed:
  - macOS: brew install gh
  - Windows: winget install --id GitHub.cli
  - Linux: See installation instructions at https://github.com/cli/cli#installation
  
  # If not authenticated:
  - Run: gh auth login
  
  # If missing workflow permissions:
  - Run: gh auth refresh -h github.com -s workflow
  ```

- **Workflow Update Dialog**: When an existing Claude workflow is detected, users are presented with three options:
  1. Update workflow file with latest version
  2. Skip workflow update (configure secrets only)
  3. Exit without making changes

### Improved Exit Handling
- **Graceful Shutdown**: A new cleanup mechanism ensures all pending operations complete before exit
  - Cleanup functions are registered and executed on exit
  - 2-second timeout prevents hanging on shutdown
  - Handles `process.exitCode` properly for clean exits

### OpenTelemetry Enhancements
- **Configurable Timeout**: New environment variable `CLAUDE_CODE_OTEL_SHUTDOWN_TIMEOUT_MS` allows customizing the OpenTelemetry shutdown timeout (default: 1000ms)
- **Better Error Messages**: When metrics flush times out, users receive helpful guidance:
  ```
  OpenTelemetry metrics flush timed out after [X]ms
  
  To resolve this issue, you can:
  1. Increase the timeout by setting CLAUDE_CODE_OTEL_SHUTDOWN_TIMEOUT_MS env var
  2. Check if your OpenTelemetry backend is experiencing scalability issues
  3. Disable OpenTelemetry by unsetting CLAUDE_CODE_ENABLE_TELEMETRY env var
  ```

### Code Editing Metrics
- **New Telemetry**: Added metrics tracking for code editing tool permission decisions (accept/reject) for Edit, MultiEdit, Write, and NotebookEdit tools

### Sonnet Model Handling
- Improved support for the "sonnet" model identifier
- Better model selection logic that properly handles custom models and built-in model aliases

### Diff Generation Enhancement
- The diff generation function now supports a `singleHunk` parameter for better control over diff output format

### Import Path Updates
- Updated Node.js imports to use the `node:` prefix convention (e.g., `import { cwd } from "node:process"`)

### Error Code Expansion
The GitHub app installation error codes have been expanded with new specific error types:
- `GH_CLI_NOT_INSTALLED` (7)
- `GH_CLI_NOT_AUTHENTICATED` (8) 
- `GH_CLI_MISSING_SCOPES` (9)
- `REPO_NOT_FOUND` (10)
- `WORKFLOW_FILE_EXISTS` (11)
- `APP_NOT_INSTALLED` (12)

## Bug Fixes

- Fixed potential issues with process exit handling in error scenarios
- Improved error handling for GitHub API calls with better 404 detection
- Enhanced workflow file detection to check for existing `.github/workflows/claude.yml`

## Version Update
- Version bumped from 0.2.125 to 0.2.126
