# Changelog for version 0.2.108

# Claude Code v0.2.108 Changelog


### Attachment System Enhancement
- **New attachment types support**: The update introduces a comprehensive attachment handling system that supports multiple types:
  - **Queued commands**: Execute commands passed as attachments with `type: "queued_command"`
  - **Nested memory**: Access nested memory content with proper path resolution
  - **TODO lists**: Automatic reminders when TODO list is empty or hasn't been used recently
  - **Ultramemory**: New attachment type for enhanced memory handling
  - **File attachments**: Improved handling for edited files, with automatic notifications when files are modified by user or linter


### Enhanced Memory Management
- **New memory export functionality**: Added `Jq1` function for exporting conversation history to JSONL format
- **Session-based memory organization**: Memory is now organized by session ID and stored in structured JSONL files
- **Automatic memory cleanup**: Added `C41` function for automatic database cleanup and memory migration


### Improved Command-Line Experience
- **Dynamic timeout configuration**: 
  - Set default timeout with `BASH_DEFAULT_TIMEOUT_MS` environment variable
  - Set maximum timeout with `BASH_MAX_TIMEOUT_MS` environment variable
  - Default timeout: 2 minutes (configurable)
  - Maximum timeout: 10 minutes (configurable)


### New Assistant Features
- **Refusal handling**: When Claude refuses a request, users now get a helpful message: "This request was refused by the model. Please double-press esc to go back in history and try again with a different prompt."
- **Queue serialization**: New `xJ6` function ensures async operations are properly serialized to prevent race conditions


### File Editing
- **Enhanced edit validation**: The `ph` function now checks if `old_string` is a substring of any previous `new_string` to prevent conflicting edits
- **Better whitespace handling**: Added note in Write tool description: "Do not add trailing whitespace to lines (a newline at the end of a file is fine)"


### Documentation Updates
- Updated documentation URL to point to simplified path: `https://docs.anthropic.com/en/docs/claude-code`
- Improved tool descriptions with clearer formatting and examples


### Performance Optimizations
- **Serialized memory operations**: Memory save operations are now queued and processed sequentially using `bJ6`
- **Better attachment rendering**: New `LJ6` function provides cleaner rendering of different attachment types


### Process Management
- Added `_p0` function to track first start time for analytics
- Improved process working directory handling with `Ot0` import


### Model Configuration
- Updated model configuration structure in `t09` with dynamic feature flags
- Added `PW` function for extracting API keys from configuration

## Bug Fixes
- Fixed potential race conditions in memory save operations
- Improved error handling for attachment processing
- Better validation for file edit operations to prevent data loss

## Removed Features
- Removed several deprecated functions including wizard-related UI components (`MN6`, `CN6`, etc.)
- Removed old memory handling functions in favor of new attachment-based system
- Removed deprecated streaming imports and variables
