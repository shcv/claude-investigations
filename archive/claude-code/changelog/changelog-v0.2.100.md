# Changelog for version 0.2.100

### Database Availability Improvements

**New database availability checking**
- Added `Wv()` function to check if the database is available before attempting database operations
- All database-dependent functions now check availability first and return empty results if unavailable
- Added helpful error message (`q90()`) that explains when the database is unavailable:
  ```
  Database is not available. Continue/resume features are disabled.
  This is likely due to issues with the better-sqlite3 dependency.
  To fix: Try globally reinstalling better-sqlite3 with your package manager.
  For more detail, see: https://github.com/WiseLibs/better-sqlite3/blob/master/docs/troubleshooting.md
  ```

This means if you have issues with the better-sqlite3 dependency, Claude Code will now gracefully degrade instead of crashing. Features like conversation history and continue/resume will be disabled, but the core functionality will still work.

### Permission System Updates

**Local settings now trigger refresh**
- When adding or deleting permission rules for local settings, the system now calls `Jt1()` to ensure changes are properly refreshed
- This fixes potential issues where local permission changes weren't immediately reflected

### Code Cleanup

**Removed legacy tool name mappings**
- Removed the `MC8` variable that contained old tool name mappings (AgentTool → Task, Replace → Write, View → Read, etc.)
- Removed the `EC8()` function that performed automatic migration of old tool names in project settings
- This suggests the tool naming migration from older versions is now complete

### Import Reorganization

**Streamlined imports**
- Replaced multiple stream-related imports with more specific ones
- Added `PassThrough` from stream module
- Using `cwd` from `node:process` instead of importing the entire process module
- Removed unused `exec` import from child_process

### Summary

This update focuses on robustness and cleanup. The main user-facing improvement is better handling of database unavailability - if you have issues with the better-sqlite3 dependency, Claude Code will now show a helpful error message and continue working with reduced functionality rather than failing completely. The permission system has also been improved to ensure local settings changes are properly applied.
