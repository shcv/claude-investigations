# Changelog for version 1.0.46

### New Features

#### Environment Variable Expansion in MCP Server Configuration
- Added support for environment variable expansion in MCP server configurations using `${VAR}` syntax
- Supports default values with `${VAR:-default}` notation
- Validates that all required environment variables are set before starting servers
- Example usage in MCP config:
  ```json
  {
    "mcpServers": {
      "myServer": {
        "command": "${HOME}/bin/server",
        "args": ["--port", "${PORT:-8080}"],
        "env": {
          "API_KEY": "${MY_API_KEY}"
        }
      }
    }
  }
  ```

#### Background Command Execution Shortcut
- Added keyboard shortcut `Ctrl+B` to run long-running commands in the background
- Displays helpful hint "Ctrl+B to run in background" when commands are executing
- Allows users to quickly background tasks without waiting for the command selection dialog

#### Enhanced Long-Running Command Display
- Improved the display of long-running commands to show the last 2 lines of output
- Shows line count indicator (e.g., "+15 more lines") for truncated output
- More compact and informative display during command execution

#### WSL Path Translation Support
- Added automatic path translation between Windows and WSL environments
- New `ie` class handles bidirectional path conversion:
  - `toLocalPath()`: Converts Windows paths to WSL paths
  - `toIDEPath()`: Converts WSL paths to Windows paths
- Automatically detects and handles WSL distribution names in paths

### Performance Improvements

#### Circular Buffer for Command Output
- Implemented `qu1` circular buffer class for efficient handling of streaming command output
- Maintains only the most recent output lines in memory
- Reduces memory usage for long-running commands with extensive output

#### Tool Result Compaction
- Added intelligent compaction for frequently-used tool outputs to reduce token usage
- Compacts results for: Read, Edit, MultiEdit, Write, Bash, Grep, Glob, LS, WebSearch, WebFetch
- Preserves essential information while reducing verbosity
- Example: `[Read /path/to/file.js, details compacted]` instead of full file contents

### Bug Fixes

#### Installation Health Check Improvements
- Fixed auto-update detection for global npm installations
- Removed check for global installations being unable to auto-update (no longer applicable)
- Improved permission checking for update capabilities

#### Shell Execution Error Handling
- Added try-catch block around shell command spawning to handle execution failures gracefully
- Returns proper error response with exit code 126 when shell command fails to start
- Provides clear error messages in stderr when execution fails

### Technical Changes

#### Updated Dependencies
- Removed redundant stream imports (`stream` and `node:stream`)
- Added new imports for child process operations from specific modules
- Updated to use `PassThrough` from `node:stream` consistently

#### Code Organization
- Removed 39 unused functions and variables, including:
  - String trimming utilities (`um2`, `dm2`)
  - Number parsing functions (`am2`, `sm2`, `om2`)
  - Array shuffling functions (`na2`, `aa2`, `ra2`)
  - Unused configuration functions
- Added 30 new functions focused on MCP support and improved command handling

#### Configuration Constants
- Added `lw6 = 2000` for command output line limits
- Added `WS6 = 2000` for WebSearch result limits
- Added `F$6 = 80000` for maximum tool output size
- Added `zQA = 3` for retry attempts

### Developer Notes

- The codebase now includes better support for development environments with proper `__dirname` handling
- Git status information is now truncated at 40,000 characters to prevent overwhelming the context
- Improved modularity with separate concerns for path translation, environment expansion, and output buffering
