# Changelog for version 0.2.36

Based on my analysis of the diff between v0.2.35 and v0.2.36, here's the detailed changelog focusing on user-facing features:


### New Features

#### Import MCP Servers from Claude Desktop
A new command has been added to seamlessly import MCP server configurations from Claude Desktop:

```bash
claude mcp add-from-claude-desktop
```

This command:
- Automatically detects Claude Desktop installations on macOS and WSL
- Presents an interactive multi-select interface to choose which servers to import
- Handles naming conflicts by adding numbered suffixes when servers with the same name already exist
- Shows visual indicators for servers that already exist in your configuration

**Example interaction:**
```
┌─ Import MCP Servers from Claude Desktop ─────────────────────┐
│ Import MCP Servers from Claude Desktop                       │
│ Found 3 MCP servers in Claude Desktop.                       │
│ Note: Some servers already exist with the same name.         │
│ Please select the servers you want to import:                │
│                                                               │
│ > [✓] filesystem-server                                       │
│   [ ] github-server (already exists)                          │
│   [✓] postgres-server                                         │
└───────────────────────────────────────────────────────────────┘
  Space to select · Enter to confirm · Esc to cancel
```

#### Add MCP Servers as JSON Strings
You can now add MCP servers directly using JSON configuration:

```bash
claude mcp add-json <name> <json>
```

This allows you to quickly configure servers by passing their JSON configuration directly on the command line.


### Improvements

#### Auto-Compact Enhancement
The `/compact` command has been significantly improved:
- Better conversation summarization using a more sophisticated prompt template
- Improved error handling with clearer user messages
- The summary now includes structured sections:
  1. Primary Request and Intent
  2. Key Technical Concepts
  3. Files and Code Sections
  4. Problem Solving
  5. Pending Tasks
  6. Current Work
  7. Next Step Recommendation

**Error messages are now more helpful:**
- "Not enough messages to compact." - when conversation is too short
- "Conversation too long. Press esc to go up a few messages and try again." - when hitting API limits
- "API Error: Request was aborted." - for network issues

#### Diff Display Improvements
The code diff display now supports:
- Option to hide line numbers with the `hideLineNumbers` parameter
- Option to skip unchanged lines with the `skipUnchanged` parameter
- Enhanced word-level diff highlighting for better readability

#### File Reading Enhancements
- New token counting for file content to prevent API overload
- Better error messages when files exceed size limits:
  - Size-based: "File content (XKB) exceeds maximum allowed size (YKB)"
  - Token-based: "File content (X tokens) exceeds maximum allowed tokens (Y)"
- Improved handling of large file reads with streaming support

#### Shell Improvements
The persistent shell has been optimized:
- Better tracking of working directory changes with a "dirty" flag
- Reduced unnecessary `pwd` calls for better performance
- Enhanced logging for debugging shell operations
- Fixed initialization timeout for shell configuration loading

#### Platform Detection
New environment detection capabilities:
- `isWslEnvironment`: Detects if running in WSL
- `isNpmFromWindowsPath`: Detects if npm is being run from Windows path in WSL

#### Configuration
New configuration option added:
- `autoCompactEnabled`: Control automatic conversation compacting (default: true)


### Bug Fixes

- Fixed WebFetch tool to properly handle response body streaming and size limits
- Improved error handling for aborted fetch requests
- Better support for safe command execution with enhanced command validation


### Technical Improvements

- Added new utility class `Ch` for structured tool errors
- Enhanced multi-select component for better user interaction
- Improved token counting accuracy for API request management
- Better handling of WSL environments for cross-platform compatibility
