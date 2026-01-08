# Changelog for version 1.0.28

### New Features

#### Model Selection Command Menu
- Added new interactive model selection functionality that allows users to switch between different Claude models during a session
- When invoked, users can navigate through available models and select their preferred model
- Includes keyboard shortcuts: ESC key to cancel and keep current model
- The selected model is displayed in bold text for clarity
- Example usage: The menu will show available models and allow selection via arrow keys

#### Enhanced MCP (Model Context Protocol) Support
- Added `MAX_MCP_OUTPUT_TOKENS` environment variable to control the maximum tokens for MCP output
- Default value: 25,000 tokens (configurable via environment variable)
- Example: `export MAX_MCP_OUTPUT_TOKENS=50000` to increase the limit

#### Improved Resume Command
- Refactored the `resume` command to use a more robust component-based architecture
- Better error handling when loading conversations
- Async loading with proper state management
- Shows loading state while fetching conversations
- Filters out sidechain conversations automatically

### Improvements

#### Image Processing Enhancements
- Added new `TG5` function for more robust image file handling
- Improved error recovery when image processing fails
- Better support for empty image files with specific error messages
- Maintains original media type when fallback processing is used

#### Configuration Directory Resolution
- Enhanced config directory resolution to respect XDG Base Directory specification
- Priority order:
  1. `CLAUDE_CONFIG_DIR` environment variable (if set)
  2. `XDG_CONFIG_HOME/claude` (if XDG_CONFIG_HOME is set)
  3. Default: `~/.claude`
- Example: `export XDG_CONFIG_HOME=/custom/config` will use `/custom/config/claude`

#### Multi-Edit Operations
- Added `iK1` function to properly handle edit operations with default values
- Ensures `replace_all` parameter defaults to `false` when not specified
- Improves consistency in batch edit operations

### Technical Improvements

#### Better Environment Variable Handling
- More defensive checks for `CLAUDE_CODE_ENTRYPOINT` to prevent duplicate assignments
- Cleaner initialization in both CLI and MCP modes

#### Error Handling
- Added `AH1` (FallbackTriggeredError) class for better model fallback error reporting
- Includes original and fallback model information in error messages

#### Process Management
- Changed from hardcoded `/bin/bash` paths to more portable process execution
- Better support for different shell environments

#### Metrics and Telemetry
- Added terminal type tracking in metrics (`terminal.type` attribute)
- Helps understand user environments for better support

### Bug Fixes

- Fixed duplicate import issues with stream modules
- Removed redundant process import
- Improved native installation detection logic
- Better handling of thinking tokens with configurable defaults

### Internal Changes

- Updated version number to 1.0.28
- Refined internal function naming and structure
- Improved code organization with better separation of concerns
- Enhanced type safety with new schema definitions for tool responses

Note: This version maintains 99.8% structural similarity with v1.0.27, ensuring stability while adding targeted improvements.
