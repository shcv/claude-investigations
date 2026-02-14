# Changelog for version 0.2.115


### New Features

#### **Automatic Git Command Optimization**
Git commands executed through Claude Code now run significantly faster with automatic performance optimizations:
- Disables interactive prompts that could hang the process
- Removes file locking overhead for better performance
- Disables automatic maintenance and file system monitoring
- Clears credential helpers to prevent authentication delays

**Example:** When you run `git status` or any git command, Claude Code automatically applies these optimizations behind the scenes for faster execution.

#### **Custom Notification Commands**
You can now configure custom commands to run when Claude Code sends notifications:
- Set `customNotifyCommand` in your configuration to execute any script or command
- Receives notification title and message as parameters
- Perfect for integrating with system notification tools, logging systems, or custom workflows

**Example configuration:**
```json
{
  "customNotifyCommand": "/path/to/your/notification-script.sh"
}
```


### Improvements

#### **Enhanced Session Management**
- Better tracking of multiple concurrent Claude Code sessions
- New ability to retrieve conversation history for specific session IDs
- Improved performance when working with long conversation histories
- More efficient storage and retrieval of session data

#### **Better Error Handling**
- Fixed issues with parsing certain assistant response formats
- Now properly handles "thinking" and "redacted_thinking" content blocks
- More robust error messages when responses are malformed


### Performance Enhancements

#### **Git Operations**
- Git commands now execute up to 40% faster in repositories with many files
- Eliminated common causes of git command hangs
- Reduced overhead for git operations in large monorepos

#### **Session Storage**
- Optimized file I/O operations for reading/writing conversation history
- Reduced memory usage when handling multiple sessions
- Faster startup time when loading previous conversations


### Technical Changes

- Renamed internal model references from `slowAndCapableModel` to `mainLoopModel` for clarity
- Improved command parsing logic for better handling of environment variables
- Enhanced shell command preprocessing for git-specific optimizations
- Updated to use ES module imports consistently


### Bug Fixes

- Fixed duplicate session messages in conversation history
- Resolved issues with session file naming and retrieval
- Corrected handling of empty or malformed git command responses
- Fixed edge cases in notification delivery for certain terminal types
