# Changelog for version 0.2.79


### New Features

#### 🆕 Local File Context Command
- Added a new `files` command that lists all files currently in context
- Usage: Simply type `files` to see which files Claude is currently aware of
- Useful for keeping track of what files you're working with in longer sessions

#### Enhanced Directory Support for @-mentions
- You can now @-mention directories in addition to files
- When you @-mention a directory path, Claude will include the directory's contents in context
- Example: `@src/components` will include information about all files in that directory

#### Improved Large File Handling
- Large files that exceed size limits are now partially loaded instead of being completely skipped
- When a file is too large, the first 100 lines are loaded with a truncation indicator
- This ensures you can still reference and work with large files, even if only partially


### Improvements

#### Performance & Stability
- Added proper timeout handling for bash commands
  - Default timeout: 2 minutes (120 seconds)
  - Maximum configurable timeout: 10 minutes (600 seconds)
- Fixed Windows path handling for escaped characters
- Improved telemetry for metrics collection

#### Environment Configuration
- Environment variables from configuration are now loaded earlier in the startup process
- This ensures custom environment settings are available throughout the entire session

#### Better User Onboarding
- New users (fewer than 10 startups) now receive targeted tips:
  - "Start with small features or bug fixes, tell Claude to propose a plan, and verify its suggested edits"
- Replaced advanced git worktree tips with more beginner-friendly guidance

#### ️ Safety Improvements
- Added supervisor interrupt handling with clear messaging
- New interrupt message: "Interaction interrupted by the safety supervisor."
- Better separation of different interruption scenarios (user interrupts vs safety interrupts)


### Internal Changes

- Removed unused stream import
- Consolidated process imports
- Added project onboarding tracking counter
- Improved code organization and error handling


### Bug Fixes

- Fixed issue where environment variables weren't being applied early enough
- Improved error handling for directory and file access
- Better validation for file paths and permissions
