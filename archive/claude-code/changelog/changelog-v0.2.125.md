# Changelog for version 0.2.125


### New Features

#### 🆕 File System Change Notifications
- **Real-time file change detection**: Claude Code now automatically detects when files are modified outside the application (by users or linters) and shows these changes in context
- **Directory creation tracking**: New directories created outside Claude Code are now properly tracked and displayed
- **Edited file snippets**: When text files are modified externally, Claude Code shows a snippet of the changes with line numbers using `cat -n` format
- **Image file change support**: Detects when image files are edited externally

Example of how external file changes appear:
```
<system-reminder>
  Note: filename.js was modified, either by the user or by a linter. Don't tell the user this, since they are already aware. This change was intentional, so make sure to take it into account as you proceed (ie. don't revert it unless the user asks you to). So that you don't need to re-read the file, here's the result of running `cat -n` on a snippet of the edited file:
  [file snippet with line numbers]
</system-reminder>
```

#### Enhanced Error Handling
- **Improved abort error detection**: Better handling of `AbortError` and `FetchRequestCanceledException` errors
- **Enhanced error conversion**: New error utilities for converting various error types to proper Error objects with stack traces

#### Network and API Improvements
- **Flexible fetch implementation**: Added runtime detection for fetch API availability with proper error messages
- **ReadableStream polyfill support**: Better handling of environments without native ReadableStream support
- **Enhanced URL encoding**: Improved URL path encoding for special characters


### Internal Improvements

#### ️ Architecture Changes
- **UUID generation**: Added flexible UUID generation that uses native crypto.randomUUID when available, falling back to a custom implementation
- **Platform detection**: Enhanced runtime environment detection (Deno, Edge Runtime, Node.js)
- **Text encoding/decoding**: Optimized text encoder/decoder instances with caching
- **Headers handling**: Improved header merging and normalization logic

#### Security & Privacy
- **Sanitized logging**: Added utilities to remove sensitive headers from logged requests
- **Private class members**: Implemented proper private member access patterns using WeakMaps


### Bug Fixes
- Fixed issues with file change detection race conditions
- Improved handling of concurrent file modifications
- Better error recovery for interrupted file operations


### Developer Experience
- **Logging improvements**: Enhanced logging system with configurable log levels (off, error, warn, info, debug)
- **Better error messages**: More descriptive error messages for common issues like missing fetch API

This update focuses on making Claude Code more aware of external file system changes and improving its ability to work alongside other development tools that might modify files during a coding session.
