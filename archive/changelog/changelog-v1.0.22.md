# Changelog for version 1.0.22

# Claude Code v1.0.22 Changelog

## New Features

### MCP Resource Management Commands
Two new commands have been added for working with MCP (Model Context Protocol) resources:

- **`listMcpResources`** - Lists all available resources from configured MCP servers
  ```bash
  # List all resources from all MCP servers
  claude listMcpResources
  
  # List resources from a specific server
  claude listMcpResources --server myserver
  ```

- **`readMcpResource`** - Reads a specific resource from an MCP server
  ```bash
  # Read a resource by server name and URI
  claude readMcpResource --server myserver --uri my-resource-uri
  ```

### Enhanced Permission Modes
- Added new permission mode: **`plan`** - Allows planning mode for complex operations
- Added `defaultMode` configuration option in permissions settings
- Added `disableBypassPermissionsMode` option to prevent bypassing permissions entirely
- Permission modes now available: `acceptEdits`, `bypassPermissions`, `default`, `plan`

### XDG Base Directory Support
Claude Code now follows the XDG Base Directory specification for better organization of files:
- **State files**: `$XDG_STATE_HOME/claude/` (defaults to `~/.local/state/claude/`)
- **Cache files**: `$XDG_CACHE_HOME/claude/` (defaults to `~/.cache/claude/`)
- **Data files**: `$XDG_DATA_HOME/claude/` (defaults to `~/.local/share/claude/`)
- **Executables**: `~/.local/bin/claude`

The application will automatically migrate existing files from the old location (`~/.claude/`) to the new XDG-compliant locations on first run.

## Improvements

### Jupyter Notebook Enhancements
- **Cell ID Support**: Notebooks now support reading individual cells by their ID
  ```bash
  # Read a specific cell from a notebook
  claude notebook-read notebook.ipynb --cell-id cell-123
  ```
- Large cell outputs are now truncated with a helpful message indicating how to read the full output
- Improved cell metadata handling with proper cell IDs

### Command History Navigation
- Enhanced history navigation with better state management
- History now properly tracks command length for improved user experience
- More robust handling of empty commands and history state

### Session Management
- Session message retrieval is now asynchronous for better performance
- Improved session file handling with async operations
- Better error handling for session loading and storage

## Bug Fixes

- Fixed duplicate imports and removed unused stream imports
- Removed redundant Unicode sanitization variable declarations
- Cleaned up unused launcher script variables
- Fixed permission mode resolution to respect configuration settings

## Technical Changes

- Updated version to 1.0.22
- Improved code organization with better module separation
- Enhanced error messages for MCP operations
- Better type safety in permission mode handling
- Streamlined directory structure initialization

## Migration Notes

When upgrading to v1.0.22, Claude Code will automatically:
1. Check for existing files in `~/.claude/`
2. Create new XDG-compliant directory structure
3. Migrate your existing data to the new locations
4. Create a migration marker to prevent repeated migrations

Your existing configurations, sessions, and data will be preserved during the migration.
