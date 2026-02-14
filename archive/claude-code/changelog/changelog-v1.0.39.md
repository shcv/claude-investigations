# Changelog for version 1.0.39

# Claude Code v1.0.39 Changelog


### Activity Tracking System
- Added comprehensive activity tracking to monitor user and CLI operation timings
- New `cp` class tracks active operations and distinguishes between user activity and CLI activity
- Automatically records activity durations for analytics purposes
- 5-second timeout for user activity detection


### Checkpointing System
- **New checkpoint feature** for saving and restoring project states within git repositories
- Automatically creates shadow git repositories in `.claude/checkpoints/` for tracking changes
- Commands available (implementation details):
  - Save checkpoints with custom labels
  - Restore to previous checkpoints with automatic backup
  - List all checkpoints in reverse chronological order
- Checkpoints are stored per git repository using SHA-256 hashing of the repository path


### Interactive Mode Detection
- Added functions to detect and manage interactive vs non-interactive sessions:
  - `d91()` - Check if running in non-interactive mode
  - `yBA()` - Check if running in interactive mode
  - `kBA()` - Set interactive mode
  - `xBA()` - Get client type
  - `vBA()` - Set client type
- Client types supported: "cli", "github-action", "sdk-typescript", "sdk-cli"


### Model Support
- Enhanced model name display in `Cj()` function
- Now properly displays names for all Claude models:
  - Opus 4
  - Sonnet 4
  - Sonnet 3.7
  - Sonnet 3.5
  - Haiku 3.5


### IDE Detection
- Added support for Android Studio in IDE detection
- JetBrains IDE list now includes "androidstudio"


### Command Detection
- Improved command availability checking with new `ih()` function
- Uses proper executable path resolution before checking file permissions


### Version Update
- Updated to version 0.55.1 (internal version tracking)
- Main version updated to 1.0.39


### New Dependencies
- Added several internal utility modules for HTTP handling, base64 encoding, and query string building
- New imports for crypto functions (`createHash`, `randomBytes`)
- Added `PassThrough` stream support


### Code Organization
- Refactored installer diagnostics (`YT5` function) with simplified logic
- Removed several unused functions:
  - `ph` - Command availability checker (replaced by `ih`)
  - `UA6` - IDE detection helper (replaced by `R06`)
  - `Qw0` - String splitting function
  - `z9A` - Shell configuration finder
  - `wx2` - Version display formatter (replaced by `$v2`)
  - `uO5` - Permission description helper (replaced by `dP5`)


### Session Management
- Enhanced `Kw0` class (formerly `lz0`) to support checkpoints
- Session logs now include checkpoint entries
- Added `getAllCheckpoints()` method to retrieve checkpoints for a session
- Modified log entry structure to handle checkpoint type

## Bug Fixes

- Fixed duplicate import statements
- Improved error handling in checkpoint operations
- Better process detection on macOS (returns null immediately instead of attempting detection)

## Usage Examples

While the checkpoint system is integrated into the codebase, it would typically be used through CLI commands (exact command syntax would depend on the CLI implementation):

```bash
# Save a checkpoint with a custom label
claude checkpoint save "Before major refactoring"

# List all checkpoints
claude checkpoint list

# Restore to a previous checkpoint
claude checkpoint restore <checkpoint-id>
```

The activity tracking and interactive mode detection work automatically in the background to provide better analytics and adapt behavior based on the execution context.
