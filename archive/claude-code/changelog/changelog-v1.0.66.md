# Changelog for version 1.0.66

# Claude Code v1.0.66 Changelog


### Session Feedback System
A new interactive feedback prompt has been added that appears during your coding sessions. When prompted, you can rate how Claude is performing:
- Press `1` for "Bad"
- Press `2` for "Fine" 
- Press `3` for "Good"
- Press `0` to dismiss the feedback prompt

The feedback system intelligently appears based on session duration and interaction count, helping improve Claude's performance over time.


### Session Bookmarking
You can now bookmark important coding sessions for easy reference later. Bookmarked sessions are preserved and marked in the session history, making it easier to find and return to significant conversations.


### Enhanced File Security
- Added validation to prevent access to potentially sensitive file paths
- File operations now include additional security checks before processing
- Improved handling of file paths in IDE integration features


### Better Error Handling
- Settings file operations now return detailed error information when issues occur
- Invalid JSON in settings files is caught and reported with helpful error messages
- More robust error recovery for configuration file issues


### Performance Optimizations
- Replaced asynchronous checkpoint loading with synchronous operations for better reliability
- Streamlined import statements to reduce overhead
- Optimized session data structures for faster access

## Bug Fixes

- Fixed an issue where checkpoint data could be loaded incorrectly in certain scenarios
- Resolved duplicate import statements that were causing unnecessary overhead
- Corrected the feedback prompt display logic to properly handle all input states

## Technical Changes

- Updated to use more specific Node.js imports (`node:process`, `node:stream`)
- Refactored feedback configuration to support model-specific settings and probability controls
- Improved session file format to support the new bookmark feature

This update focuses on improving the user experience with helpful feedback collection and better session management, while also strengthening security and reliability throughout the codebase.
