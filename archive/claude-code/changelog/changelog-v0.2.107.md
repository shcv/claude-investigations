# Changelog for version 0.2.107

# Claude Code v0.2.107 Changelog

### Enhanced Project-Level Memory (CLAUDE.md)
- **Automatic project context loading**: Claude Code now automatically discovers and loads `CLAUDE.md` files from parent directories up to your home directory
- **Nested memory attachments**: When working in subdirectories, Claude Code will now find and include all relevant `CLAUDE.md` files in the directory hierarchy
- **Usage**: Simply place a `CLAUDE.md` file in your project root or any parent directory, and Claude Code will automatically use it for context when working in that project or its subdirectories

### IDE Integration Improvements
- **JetBrains IDE support**: Added specific guidance for JetBrains IDE users
- **New prompt for plugin installation**: When using a JetBrains IDE without the plugin installed, you'll now see:
  ```
  Please install the plugin and restart the IDE:
  https://plugins.jetbrains.com/plugin/27310
  ```
- **Conditional extension management**: Extension installation prompts now only appear for supported IDEs (VS Code)

### Memory System Enhancements
- Added `CX6` function for discovering CLAUDE.md files in parent directories
- New `Ha5` function handles nested memory attachment triggers
- Improved `vs` function now properly tracks visited paths to prevent infinite recursion

### Code Organization
- Refactored stream imports to use named imports (`PassThrough` from "stream")
- Consolidated process imports to use named imports (`cwd` from "node:process")
- Added new variable `yU6` for improved code organization

### Database Warning Removal
- Removed the persistent database unavailability warnings
- Removed the `/doctor` command prompt for database issues
- Removed better-sqlite3 troubleshooting messages and links
- These changes suggest that database functionality has been stabilized or reimplemented

## Under the Hood

- Function renaming: Several internal functions were renamed for consistency
- Improved error handling in the nested memory attachment system
- Better separation of concerns between VS Code and JetBrains IDE features
