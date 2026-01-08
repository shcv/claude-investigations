# Changelog for version 1.0.14

# Claude Code v1.0.14 Changelog

### Plan Mode
- **New interactive planning mode** - A new mode that allows Claude to plan implementation steps before executing them. When enabled, Claude will outline the approach before making changes.
  - Visual indicator: `⏸ plan mode on` appears in the status bar
  - Toggle between modes using `Shift+Tab`
  - Plan mode can be detected programmatically via the tool permission context

### Terminal Title
- **Automatic terminal title** - The CLI now sets the terminal title to "claude" when launched, making it easier to identify Claude Code sessions in your terminal tabs.

### Enhanced MCP Tool Error Messages
- **Better error reporting for missing MCP tools** - When using `--permission-prompt-tool` with a non-existent tool, the error message now lists available MCP tools or indicates "none" if no MCP tools are available.
  ```bash
  # Before: generic error
  # After: "Error: MCP tool xyz not found. Available MCP tools: tool1, tool2, tool3"
  ```

### Tool Permission Filtering
- **Excluded permission prompt tools from regular tool list** - When a tool is specified via `--permission-prompt-tool`, it's now properly excluded from the regular tool execution list to prevent conflicts.

### Analytics
- Added tool decision tracking for better understanding of tool usage patterns
- New telemetry event: `tool_decision` captures tool selection decisions

### Code Organization
- Switched from direct process import to named import for better modularity
  ```javascript
  // Before: import mS2 from "node:process"
  // After: import { cwd as vI0 } from "node:process"
  ```
- Added PassThrough stream import for improved stream handling

### Removed Features
- Removed unused streaming tool UI components that were displaying waiting messages
- Cleaned up redundant imports and unused variables

## Version Update
- Launcher script version bumped from 0.0.4 to 0.0.6
