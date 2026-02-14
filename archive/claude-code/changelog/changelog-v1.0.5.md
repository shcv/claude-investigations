# Changelog for version 1.0.5

# Claude Code v1.0.5 Changelog


### 🆕 Flexible Configuration Directory
- **New function `b9()`**: Returns the Claude configuration directory, defaulting to `~/.claude` if `CLAUDE_CONFIG_DIR` environment variable is not set
- **New function `vJ()`**: Intelligently determines the configuration file path:
  - First checks for `.config.json` in the Claude config directory
  - Falls back to `.claude.json` in either the custom config directory or home directory
  - Example: If you set `CLAUDE_CONFIG_DIR=/custom/path`, Claude will look for `/custom/path/.config.json` first


### Centralized Configuration Management
- Replaced hardcoded configuration paths throughout the codebase with dynamic path resolution
- All configuration-related functions now use the centralized `b9()` function for consistency


### 🆕 Enhanced Command Execution with `D2()` Function
- **New options parameter** with configurable defaults:
  ```javascript
  {
    timeout: 120000,           // 2 minutes default
    preserveOutputOnError: true,
    useCwd: true              // Use current working directory
  }
  ```
- **Environment variable support**: Pass custom environment variables to executed commands
- **Abort signal support**: Cancel long-running commands programmatically


### Improved `eG()` Function (formerly `AZ`)
- Now accepts flexible parameter formats:
  - Simple abort signal: `eG(command, abortSignal)`
  - Options object: `eG(command, { abortSignal, timeout })`
  - Backward compatible with existing usage


### 🆕 X11 Display Handling
- **New function `lh1()`**: Automatically disables X11 forwarding on Linux systems by setting `DISPLAY=""` in command environment
- Prevents GUI applications from attempting to open windows when running in headless environments


### 🆕 Resource Discovery
- **New `dO8` variable**: Implements automatic resource discovery from connected MCP servers
- Fetches available resources from servers with resource capabilities
- Gracefully handles errors and logs failures for individual servers


### 🆕 Dynamic Fallback Description
- **New function `g31()`**: Generates user-friendly descriptions for model fallback behavior
- Example output: "Use Opus up to 75% of Max usage limits, then Sonnet"
- Adapts description based on configured threshold


### Stream Handling
- Added `PassThrough` stream import for improved data streaming capabilities


### Refactored Changelog Formatting
- Renamed `sU2` to `aU2` for consistent naming conventions
- Maintained identical formatting behavior for version changelogs


### Updated System Prompt
- Version number updated from 1.0.4 to 1.0.5 in user assistance messages
- Added conditional MCP resource information to system prompts


### Process Import Fix
- Added missing `cwd` import from `node:process` module
- Ensures proper working directory handling across the application


### Configuration Path Resolution
- Fixed potential issues with configuration file discovery
- Improved fallback logic for legacy configuration locations
