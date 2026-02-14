# Changelog for version 1.0.38


### Major Features

#### Hook System (New)
- **Pre/Post Tool Hooks**: Execute custom commands before and after tool operations
  - `PreToolUse` - Run commands before tools execute (e.g., validation, logging)
  - `PostToolUse` - Run commands after tools complete (e.g., notifications, cleanup)
  - `Stop` - Execute commands when Claude stops responding
  - `Notification` - Trigger commands for system notifications
- **Hook Configuration**: Configure hooks with matchers to target specific tools or patterns
  - Support for regex and pipe-separated matchers
  - Hooks can approve/block operations or provide feedback
  - JSON output parsing for structured hook responses
  - 60-second timeout with automatic cancellation

#### Enhanced Search Tool (Grep)
- **New Grep Tool**: Powerful search based on ripgrep with advanced features
  - Multiple output modes: `content`, `files_with_matches`, `count`
  - Context lines support with `-A`, `-B`, `-C` flags
  - Line numbers with `-n` flag
  - Case-insensitive search with `-i` flag
  - File type filtering with `type` parameter
  - Glob pattern support for file filtering
  - **Multiline mode**: Search across line boundaries with `multiline: true`
  - Head limit to control output size
- Optimized for correct permissions and file access
- Never invokes `grep` or `rg` as bash commands directly


### New Commands & Features

#### Memory Management
- Enhanced memory system with support for adding memories to specific files
- Memory updates preserve existing content and structure
- Automatic section detection for organized memory storage

#### ️ Terminal Integration
- **Ghostty Terminal Support**: Added configuration for Shift+Enter keybinding
- Improved terminal setup for multiple environments
- Better handling of paste operations with image detection

#### ️ IDE Detection
- Automatic detection of JetBrains IDEs when launched from within them
- Supports: PyCharm, IntelliJ, WebStorm, PhpStorm, RubyMine, CLion, GoLand, Rider, DataGrip, AppCode, DataSpell, Aqua, Gateway, Fleet


### Improvements

#### Security & Privacy
- Enhanced API key redaction in logs
- Support for AWS, GCP, and generic API key patterns
- Better handling of authorization tokens and service accounts

#### Performance & Reliability
- Improved proxy configuration with AWS SDK
- Better handling of aborted operations in hooks
- Enhanced error messages for hook failures
- Optimized file search with modification time sorting

#### UI/UX Enhancements
- Visual indication when hooks are running
- Better feedback for blocked operations
- Improved diff view for file edits
- Enhanced paste detection with visual feedback


### Technical Updates

- Updated dependencies and imports
- Improved TypeScript/JavaScript parsing
- Better handling of multiline patterns in search
- Enhanced abort signal propagation
- Optimized memory usage for large file operations


### Bug Fixes

- Fixed duplicate comment issues
- Improved error handling in hook execution
- Better cleanup of resources on exit
- Fixed terminal focus detection issues
- Resolved paste operation edge cases


### Breaking Changes

None - This release maintains backward compatibility with existing configurations and workflows.


### Configuration

New hook configuration example:
```javascript
// Configure hooks in settings
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "file_edit|str_replace",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'About to edit a file' | tee -a /tmp/claude.log"
          }
        ]
      }
    ]
  }
}
```

New Grep tool usage examples:
```bash
# Search for function definitions
claude> Search for "function.*Error" in all JavaScript files

# Multiline search for struct definitions
claude> Search for struct definitions with a "field" property using multiline mode

# Count occurrences with context
claude> Count how many times "TODO" appears in the codebase with 2 lines of context
```
