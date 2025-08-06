# Changelog for version 1.0.37

# Claude Code v1.0.37 Changelog

## New Features

### Print Mode Support
- Added support for `-p` / `--print` command-line flags and automatic detection of non-TTY output
- When running `claude -p` or `claude --print`, or when output is piped/redirected, Claude will operate in print mode
- This allows for better integration with scripts and command pipelines

### Enhanced Configuration Management

#### Automatic Config Backup and Recovery
- Configuration files are now automatically backed up when corruption is detected
- If the main config file is corrupted, a timestamped backup is created (e.g., `config.json.corrupted.1234567890`)
- Users are notified of backup locations and provided with recovery instructions
- Example recovery message:
  ```
  Claude configuration file at ~/.claude/config.json is corrupted
  The corrupted file has been backed up to: ~/.claude/config.json.corrupted.1234567890
  A backup file exists at: ~/.claude/config.json.backup
  You can manually restore it by running: cp "~/.claude/config.json.backup" "~/.claude/config.json"
  ```

#### Improved Config File Locking
- Added file locking mechanism for configuration updates to prevent concurrent write conflicts
- If locking fails, the system gracefully falls back to non-locked saves with appropriate logging

### Cost Reporting Control
- New environment variable `CLAUDE_CODE_DISABLE_COST_REPORTING` to disable cost reporting features
- Usage: `export CLAUDE_CODE_DISABLE_COST_REPORTING=true`

### Agent Plan Rejection Handling
- Added proper error messaging when an agent's proposed plan is rejected by the user
- Provides clearer feedback in the interactive workflow

## Technical Improvements

### Error Handling
- Added new `AbortError` class for better error categorization and handling of aborted operations

### Stream Processing
- Migrated from generic stream imports to more specific `PassThrough` stream for improved performance

### Tool Permission System
- Added new permission request structure for tools, including:
  - Tool name identification
  - Input validation
  - Unique tool use request IDs for tracking

## Bug Fixes

- Fixed configuration reading and writing logic to be more robust
- Improved error messages and user guidance for configuration issues
- Enhanced logging throughout the configuration management system

## Internal Changes

- Refactored configuration file operations with better error handling and recovery
- Added comprehensive logging for debugging configuration issues
- Improved modularization of stream processing components
