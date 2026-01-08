# Changelog for version 1.0.59

Based on my analysis of the diff file, here is the changelog for Claude Code version 1.0.59:

### New Features

#### **Checkpointing System** 🆕
Claude Code now automatically saves checkpoints of your work during sessions, providing a safety net for your changes.

- **Automatic checkpoint creation**: Claude Code creates incremental snapshots of your codebase as you work
- **Shadow Git repository**: Checkpoints are stored in `.claude/checkpoints/` using Git for efficient version tracking
- **Opt-out option**: Disable checkpointing by setting the environment variable `CLAUDE_CODE_DISABLE_CHECKPOINTING`
- **Configuration**: New `checkpointingEnabled` setting (enabled by default)

**Usage**: Checkpoints are created automatically in the background. No user action required.

```bash
# To disable checkpointing:
export CLAUDE_CODE_DISABLE_CHECKPOINTING=true
claude
```

### Improvements

#### **Performance Optimizations**
- Removed duplicate import statements for Node.js streams
- Streamlined internal Zod library usage
- Improved Git operations with `core.untrackedcache` for better performance

#### **UI Simplification**
- Removed agent color index management system for a cleaner interface
- Simplified how parallel agents are displayed

### Bug Fixes

- Fixed internal error handling structures
- Improved checkpoint initialization error recovery
- Enhanced configuration validation

### Internal Changes

- Added cryptographic utilities for checkpoint directory hashing
- Updated internal agent management functions
- Refined memory usage tracking
- Structural code improvements (98.7% similarity to previous version)

### Configuration

New configuration option added:
```json
{
  "checkpointingEnabled": true  // Enable/disable checkpoint feature
}
```

### Notes

- The checkpointing feature operates transparently in the background
- Checkpoint data is stored locally in your project's `.claude/checkpoints/` directory
- Each project gets its own unique checkpoint directory based on SHA-256 hash
- The feature adds minimal overhead to your workflow while providing recovery options

This release focuses on improving reliability and safety with the new checkpointing system while maintaining the familiar Claude Code experience.
