# Changelog for version 1.0.8

# Claude Code v1.0.8 Changelog


### MCP OAuth Authentication
- Added support for OAuth authentication with MCP (Model Context Protocol) servers
- New `mcp-auth` command for authenticating with servers that require OAuth
- Interactive authentication flow with browser-based login
- Automatic token refresh when tokens expire
- Secure credential storage in the configuration directory


### Enhanced Thinking Mode
- Expanded multi-language support for thinking mode triggers
- Now supports thinking phrases in 8 languages:
  - English: "think", "think harder", "ultrathink", etc.
  - Japanese: "考えて", "熟考", "深く考えて"
  - Chinese: "思考", "深思", "仔细思考"
  - Spanish: "piensa", "piensa más", "piensa profundamente"
  - French: "réfléchis", "réfléchis plus", "pense"
  - German: "denk", "denk mehr", "denk gründlich"
  - Korean: "생각", "심사숙고", "깊이 생각"
  - Italian: "pensa", "rifletti", "pensa profondamente"
- Three thinking levels with different token allocations:
  - HIGHEST: 31,999 tokens (phrases like "think harder", "ultrathink")
  - MIDDLE: 10,000 tokens (phrases like "think deeply", "megathink")
  - BASIC: 4,000 tokens (simple "think")


### Model Selection Improvements
- Better support for Claude Max users with automatic model selection
- Simplified model detection for Pro vs Max subscriptions
- Improved fallback model descriptions based on usage limits


### Keyboard Shortcuts
- New `Ctrl+E` shortcut in transcript mode to toggle a feature (context-dependent)
- Updated newline hints:
  - Apple Terminal with Option as Meta: "option + ⏎ for newline"
  - Other terminals: "shift + ⏎ for newline" or "\\⏎ for newline"


### Edit Tool Improvements
- Added `replace_all` parameter to the Edit tool
- When `replace_all` is true, all occurrences of the old string are replaced
- Default behavior remains single replacement for backwards compatibility

**Example usage:**
```bash
# Replace all occurrences of a variable name
claude "Rename all instances of 'oldVariable' to 'newVariable' in my code"
# Claude will use replace_all: true when appropriate
```


### Signal Handling
- Improved process signal handling for SIGINT and SIGTERM
- More graceful shutdown when interrupted


### Timeout Configuration
- Configurable MCP timeouts via environment variables:
  - `MCP_TIMEOUT`: General MCP operation timeout (default: 30 seconds)
  - `MCP_TOOL_TIMEOUT`: MCP tool execution timeout (default: 100 seconds)


### Debug Logging
- Enhanced MCP debug logging with `--mcp-debug` flag
- Logs are written to structured JSON files for easier debugging
- Each log entry includes timestamp, session ID, and working directory

## Bug Fixes

- Fixed issues with file editing when strings end with newlines
- Improved handling of partial JSON parsing for better error recovery
- Better OAuth token refresh logic with proper error handling
- Fixed race conditions in authentication flows

## Internal Changes

- Removed several unused functions and variables for cleaner codebase
- Updated prompt caching logic to use function-based configuration
- Improved configuration directory handling with hashing support
- Better separation of Pro/Max user detection logic

## Breaking Changes

None - this release maintains full backwards compatibility with v1.0.7.
