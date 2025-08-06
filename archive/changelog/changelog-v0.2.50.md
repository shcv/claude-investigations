# Changelog for version 0.2.50

# Changelog for Claude Code v0.2.50

## New Features

### MCP Server Project Scope
- **New "project" scope for MCP servers**: You can now add MCP servers to `.mcp.json` files and commit them to your repository. This allows teams to share MCP server configurations as part of their project.
  
  Example usage:
  ```bash
  claude mcp add --scope project
  ```
  
  This creates or updates a `.mcp.json` file in your project root that can be committed to version control.

### Memory System Enhancements
- **Memory type selector**: When creating memories, you can now choose between three types:
  - **Project Memory**: Shared in the project repository (stored in `CLAUDE.md`)
    - Example: "Run lint with the following command after major edits: npm run lint"
  - **Local Memory**: Private to you in this project (stored in `CLAUDE.local.md`)
    - Example: "Use my sandbox URL for testing: https://myapp.local"
  - **User Memory**: Available in all your projects (stored in `~/.claude/CLAUDE.md`)
    - Example: "Don't add new comments when editing code"

  The memory selector UI provides arrow key navigation and clear descriptions of each memory type's scope.

### Notebook Editing Improvements
- **Enhanced Jupyter notebook cell editing**: New dedicated UI for notebook cell operations with better visual feedback
  - Supports insert, delete, and replace operations on notebook cells
  - Shows cell type (code or markdown) and index information
  - Provides syntax-highlighted previews of cell contents
  - Displays diffs for cell replacements

### Git Operation Tracking
- **Automatic git operation analytics**: The CLI now tracks when you perform git commits and create pull requests through the bash tool, providing better insights into your workflow patterns.

## Improvements

### File Path Handling
- **Better support for files with spaces**: The bash tool now properly handles file paths containing spaces by automatically quoting them
  
  Example:
  ```bash
  cd "/Users/name/My Documents"  # Correctly handled
  python "/path/with spaces/script.py"  # Correctly handled
  ```

### Input System
- **Refined keyboard shortcuts**: The input system has been optimized with better handling of escape sequences and control keys

### Token Usage Warnings
- **New token threshold warnings**: The system now provides warnings when approaching token limits to help manage long conversations

## Technical Changes

### Removed Features
- Removed several internal memory management functions that were replaced by the new memory type selector
- Removed unused debugging and configuration variables
- Consolidated import statements for better module organization

### Internal Improvements
- Streamlined the CLAUDE.md file discovery system to support the new three-tier memory architecture
- Improved error handling for file operations
- Better organization of keyboard input handling code

## Breaking Changes

### MCP Scope Naming (from v0.2.49)
Note: The previous version (v0.2.49) renamed MCP server scopes:
- Previous "project" scope → now "local" 
- Previous "global" scope → now "user"

This version (v0.2.50) introduces a new "project" scope that allows committing MCP configurations to repositories.

## Bug Fixes
- Fixed issues with notebook cell editing UI layout
- Improved handling of special characters in file paths
- Better error messages for invalid MCP scope specifications
