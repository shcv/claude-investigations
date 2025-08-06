# Changelog for version 1.0.63

# Claude Code v1.0.63 Changelog

## New Features

### Output Mode Selection
A new output mode system has been introduced that changes how Claude Code communicates with users. Users can now choose between different interaction styles:

- **Default Mode**: Concise, direct responses focused on completing tasks efficiently. Best for straightforward coding help.
- **Insights Mode**: Provides educational insights along the way to help understand implementation choices and codebase patterns.
- **Learn by Doing Mode**: Collaborative mode where users are asked to contribute small, strategic pieces of code for hands-on learning.

To change the output mode, users can access the new mode selection interface which allows saving preferences either globally or per-project.

### Enhanced Debug Output
New debug flag `--debug-to-stderr` has been added. When enabled, debug output will be written to stderr instead of stdout, allowing better separation of debug information from regular output.

```bash
claude --debug-to-stderr [command]
```

### Workspace Restoration in Message Selector
The message selector (jump to previous message feature) now includes an option to restore the workspace state associated with a previous message when checkpointing is enabled. This allows users to not only jump to a previous conversation point but also restore the file system state from that moment.

When selecting a previous message, users will see indicators showing whether workspace restoration is available for that checkpoint. Messages without restorable workspace states are marked with `[ ✗ Restore Workspace ]`.

### MCP Server Status Indicators
New visual indicators for MCP (Model Context Protocol) server status have been added. The interface now shows:
- Failed MCP servers with error indicators
- MCP servers that need authentication with warning indicators
- Helpful hint to use `/mcp` command for more information

These indicators automatically disappear after 5 seconds to avoid cluttering the interface.

## Improvements

### Better Error Handling in Print Mode
The `--print` mode now has improved error handling and exit codes. The exit code properly reflects whether an error occurred during execution, making it more reliable for scripting and automation.

### Enhanced Command Response Handling
Local commands now include checkpoint information in their responses, ensuring that the conversation state is properly tracked even when using local slash commands.

### Cleaner Message Filtering
The message selector now has improved filtering logic to exclude command output messages (stdout/stderr from local commands and bash commands) from the selectable message list, providing a cleaner interface for jumping between actual user messages.

## Bug Fixes

### Removed Duplicate Imports
Fixed issues with duplicate stream imports that were causing potential conflicts.

### Fixed Parallelization Configuration
Removed the `parallelTasksCount` configuration option which was causing issues with task execution.

### IDE Auto-connection Improvements
Enhanced the IDE auto-connection logic to better handle WebSocket and Server-Sent Events connections, with improved authentication token handling and Windows compatibility detection.

## Technical Changes

### Stream Processing Updates
- Replaced direct stream imports with more specific imports from `node:stream`
- Added `PassThrough` stream handling for better data flow control

### Debugging Infrastructure
- Added lazy evaluation for debug flags using memoization
- Introduced `qo0` function for writing debug output to stderr in chunks

### Message Processing
- New `w$B` function for extracting control sequences from user messages
- Added `B68` function for handling output mode metadata
- Implemented `$Z1` for finding checkpoint IDs in message sequences

## API Changes

### Control Response Handling
New `tH8` function handles initialization requests with improved error handling and command discovery for external integrations.

### Checkpoint Management
- `Wx1`: Retrieves checkpoint attachments for a conversation
- `$Z1`: Finds checkpoint IDs associated with messages

These changes improve the overall stability and user experience of Claude Code, with particular focus on making the tool more educational and collaborative through the new output modes, while also enhancing the debugging and state management capabilities.
