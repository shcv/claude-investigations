# Changelog for version 0.2.46

# Claude Code v0.2.46 Changelog

## New Features

### Local Installation Support
- **New `/migrate-installer` command**: Install Claude CLI locally to your home directory (`~/.claude/local`) to avoid npm permission issues
- Automatically detects if you're running from a local installation
- Provides setup instructions for creating shell aliases when using local installation
- Local installations update differently - use `cd ~/.claude/local && npm update @anthropic-ai/claude-code`

### API Key Helper
- **New `apiKeyHelper` configuration option**: Specify a command in `~/.claude.json` that returns your API key
- Useful for retrieving API keys from password managers or other secure storage
- Example: `"apiKeyHelper": "op item get 'Anthropic API Key' --fields password"`

### iTerm2 Integration Improvements
- Enhanced iTerm2 Shift+Enter key binding installation with automatic backup/restore
- Creates a backup of iTerm2 preferences before making changes
- Automatically restores settings if installation fails
- New recovery functions: `vV0()` (backup), `SV0()` (restore), `X79()` (install with safety)

### Enhanced Tool Confirmations
- Write/Edit file confirmations now include "Yes, and don't ask again this session" option with Shift+Tab shortcut
- More contextual scope descriptions in MCP server confirmations (e.g., "private to you in this project" vs "shared via .mcp.json")

## Improvements

### Token Usage Monitoring
- New token threshold system with warning levels:
  - 60% usage: Warning threshold
  - 80% usage: Error threshold  
  - 100% usage: Auto-compact threshold
- `cE1()` function provides detailed usage statistics including percentage remaining

### File Operations
- Read tool now explicitly mentions it can display images: "For image files, the tool will display the image for you"
- Added reminder to use `ReadNotebook` for Jupyter notebook files (.ipynb)

### MCP (Model Context Protocol)
- Updated server configuration messages to be clearer about scope visibility
- Better formatting of scope descriptions in success messages

## Under the Hood

### Configuration
- Added `env` field to configuration defaults for environment variable management
- Expanded allowed configuration keys to include `apiKeyHelper` and `env`

### Code Organization
- New utility functions for local installation management: `yO2()`, `OO2()`, `bb()`, `YN()`, `Kv3()`, `l$1()`
- Improved shell detection and configuration file handling
- Added robust error handling for API key retrieval

### Dependencies
- Updated various import statements for better module organization
- Added new imports for file system operations and process management

## Bug Fixes

- Fixed duplicate permission checking logic in auto-updater
- Improved error messages when API key helper fails
- Better handling of escape key in MCP wizard (now only works in non-welcome/success screens)

## Migration Notes

If you're experiencing npm permission issues with auto-updates, you can now use the local installation method:

1. Run `/migrate-installer` in Claude Code
2. Follow the instructions to set up a shell alias
3. Future updates can be done with `cd ~/.claude/local && npm update @anthropic-ai/claude-code`
