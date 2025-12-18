# Changelog for version 0.2.62

# Changelog for v0.2.62

## New Features

### IDE Integration Enhancement
- **Enhanced IDE selection awareness**: Claude Code now detects and displays when text is selected in your IDE (when connected via MCP)
  - Shows the number of lines selected in the status bar (e.g., "5 lines selected")
  - Automatically clears the indicator when selection is removed
  - Supports selection notifications from IDE extensions that implement the `selection_changed` MCP notification

### Improved Changelog Management
- **Dynamic changelog fetching**: Claude Code now fetches the latest changelog from GitHub
  - Automatically caches changelog updates for better performance
  - Fetches from: `https://raw.githubusercontent.com/anthropics/claude-code/refs/heads/main/CHANGELOG.md`
  - Shows relevant release notes on startup when updates are available

### Model Configuration Updates
- **New Sonnet model**: Added support for `claude-3-7-sonnet-20250219`
- **Improved model selection**: Better handling of environment-specific model configurations
  - Automatically selects appropriate model variant based on your provider (Bedrock, Vertex, or First-party)
  - Respects `ANTHROPIC_SMALL_FAST_MODEL` environment variable for custom model selection

## Improvements

### User Interface
- **Queue command hint tracking**: Added `queuedCommandUpHintCount` to user preferences for better hint management
- **Enhanced streaming status**: Claude now shows more specific status indicators during response streaming:
  - "responding" for regular text responses
  - "tool-use" when executing tools
  - "thinking" when in thinking mode

### Performance
- **Optimized output handling**: Large outputs are now written in chunks to prevent buffer overflow
  - Processes output in 2000-character chunks for better terminal performance

## Technical Changes

- Removed unused stream import and process import redundancies
- Consolidated MCP server connection handling
- Improved notification processing for IDE integrations
- Better separation of concerns for changelog and release notes display

## Bug Fixes

- Fixed potential issues with undefined IDE selection states
- Improved error handling for selection change notifications
- Better handling of edge cases in streaming responses
