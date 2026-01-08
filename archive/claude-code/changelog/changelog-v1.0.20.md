# Changelog for version 1.0.20

Based on my analysis of the diff, here is the changelog for version 1.0.20:

### New Features

#### Plan Mode
- **New planning mode for complex tasks**: Claude can now work in "Plan Mode" where it will research and present a plan before making any changes to your codebase
- **Exit plan mode tool**: When in plan mode, Claude will use the `ExitPlanMode` tool to present the completed plan and prompt you to confirm before proceeding with implementation
- **Visual indicators**: Plan mode has its own color scheme in the UI (cyan/teal colors) to clearly indicate when this mode is active
- **Usage**: Plan mode is automatically triggered for tasks that require planning and research before implementation. Claude will not make any file edits or run any commands that modify system state while in plan mode

#### Improved Task Management
- **Enhanced todo list guidance**: Claude now has better heuristics for when to use the todo list tool:
  - Complex multi-step tasks (3 or more distinct steps)
  - Non-trivial tasks requiring careful planning
  - When users explicitly request a todo list
  - When users provide multiple tasks (numbered or comma-separated)
- **Better task tracking**: Claude is now instructed to mark tasks as completed immediately after finishing them, not batching completions

### Removed Features
- **File structure snapshot removed**: The automatic project file structure snapshot that was shown at the start of conversations has been removed. This snapshot previously displayed the project's directory structure while skipping .gitignore patterns.

### UI/UX Improvements
- **Mode selection UI**: Added visual mode indicators with distinct color schemes:
  - Default mode
  - Plan mode (cyan/teal)
  - Accept Edits mode
  - Bypass Permissions mode
- **Development Partner Program notice**: Users in the Development Partner Program will see a notice that their sessions are being shared with Anthropic for service improvement

### Tool Improvements
- **MultiEdit tool enhancement**: Added clarification that `old_string` and `new_string` must be different, preventing accidental no-op edits
- **Better error messages**: More specific error messages for various edge cases in tools

### Documentation Updates
- Updated references to Claude Code documentation with specific sub-pages:
  - `overview`
  - `cli-usage` (CLI commands, flags, SDK, slash commands, and modes)
  - `memory` (Memory management and CLAUDE.md)
  - `settings`
  - `security` (Permissions and tools)
  - `costs`
  - `bedrock-vertex-proxies` (Model configuration)
  - `tutorials` (Extended thinking, pasting images, workflows)
  - `troubleshooting`

### Bug Fixes
- Various minor fixes and improvements to tool execution and error handling
- Better handling of edge cases in file operations
