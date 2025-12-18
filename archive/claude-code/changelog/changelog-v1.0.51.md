# Changelog for version 1.0.51

## Claude Code v1.0.51 Changelog

### New Features

#### Setup Notes Display
A new component has been added to display setup notes and warnings to users during initialization. When there are important setup considerations or configuration requirements, the CLI will now show:
- A warning icon with "Setup notes:" header
- Bulleted list of setup messages
- Clean formatting with proper indentation

This helps users understand any special configuration or setup steps needed for their environment.

### Internal Changes

#### Update Lock File Path Resolution
The update lock file path is now dynamically resolved using a new `hk()` function instead of being statically defined. This provides more flexibility in determining the lock file location.

#### Reduced Memory Threshold
The internal memory threshold has been decreased from 80,000 to 70,000, which may improve performance in memory-constrained environments.

#### New Dependencies
- Added `PassThrough` stream import for improved stream handling
- Added `cwd` import from node:process for better working directory management

### Removed Features

#### File Watching System Removed
The entire file watching infrastructure has been removed, including:
- Chokidar-based file system watcher
- Settings file monitoring for automatic reload
- External change detection system
- The "Detected changes to settings.json. Restart to apply." notification

This means users will now need to manually restart Claude Code after making changes to configuration files rather than seeing automatic notifications about external changes.

#### Removed Dependencies
Several file system and path-related imports have been removed as they were part of the now-removed file watching system.

### Summary
This update focuses on simplifying the codebase by removing the automatic file watching system while adding better setup guidance for users. The removal of file watching may require users to be more mindful about restarting the application after configuration changes, but it reduces complexity and potential resource usage from continuous file monitoring.
