# Changelog for version 1.0.45

# Claude Code v1.0.45 Changelog

### Agent System Enhancement
- **New Agent Tool**: Introduced a powerful new `Task` tool that allows launching specialized agents to handle complex, multi-step tasks autonomously
  - Multiple agent types available including: `general-purpose`, `context-collector`, `tech-researcher`, `test-engineer`, and more
  - Agents can be run in parallel for improved performance
  - Each agent type has specific tool access and use cases
  
  **Usage example:**
  ```
  /task "Research the authentication system in this codebase" --agent-type investigator
  ```

### Enhanced Metrics System
- Added organization-level metrics opt-out checking
- New API endpoint integration for checking metrics preferences
- Improved metrics logging with better error handling

### File Writing Improvements
- **Atomic File Writes**: Implemented atomic file writing to prevent data corruption
  - Creates temporary files first, then renames them atomically
  - Preserves original file permissions
  - Automatic fallback to non-atomic writes if atomic operation fails
  - Better error handling and logging for file operations

### UI Enhancements
- **Custom Spinner Words**: Removed the built-in spinner word generation system
- Now fetches spinner words from a remote configuration source
- More dynamic and customizable loading messages

### Smart Quote Handling
- Added intelligent quote normalization for better text matching
- Handles smart quotes (curly quotes) and converts them to standard quotes
- Improves search and text matching accuracy

### ️ Utility Functions
- Added new array manipulation functions:
  - `shuffle`: Randomly shuffle array elements
  - `sample`: Get random samples from arrays
  - `sampleSize`: Get multiple random samples with specified size
- Added number utility functions for better numeric operations

### Security Improvements
- Enhanced WSL detection for better platform-specific handling
- Improved process isolation and security checks

### Deprecated Components
- Removed the legacy `Search` tool (replaced by enhanced `Grep` functionality)
- Removed hardcoded spinner word list and generation logic
- Removed General Availability announcement components
- Removed various unused utility functions

### Performance
- Optimized file operations with atomic writes
- Better caching for metrics API calls (1-hour cache)
- Improved parallel agent execution

### Error Handling
- Enhanced error reporting for file operations
- Better fallback mechanisms for failed operations
- Improved logging throughout the application

## Bug Fixes
- Fixed potential file corruption issues during concurrent writes
- Improved handling of symlinks during file operations
- Better error recovery for failed atomic write operations

## Breaking Changes
- The `Search` tool has been removed - use `Grep` instead
- File writing now uses atomic operations by default, which may affect custom file watchers


This release focuses on reliability, performance, and the introduction of the powerful new Agent system for handling complex tasks. The atomic file writing ensures data integrity, while the new agent architecture allows for more sophisticated multi-step operations.
