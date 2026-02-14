# Changelog for version 0.2.25


### Fuzzy Matching for Commands
- Introduced fuzzy matching for slash commands (`/commands`), making it easier to find and execute commands without typing the exact name
- This feature was initially added in v0.2.21 and is now included in this release


### Approved Tools Management
- Added new `/approved-tools` command to manage pre-approved tools
- View, edit, and delete tools that Claude Code can use without asking for permission each time
- Interactive interface shows which specific Bash commands or command patterns are approved
- Provides clear visual indication when editing approved tools with delete/cancel options


### Exit Command Aliases
- Added `/exit` and `/quit` commands to exit the REPL
- These provide more intuitive ways to close the application compared to using Ctrl+C


### Enhanced Tool Validation
- Implemented `validateInput` functionality for tools to ensure input parameters are valid before execution
- Tool requests are now validated before being sent to the API, preventing invalid tool usage


### Web Authentication Check
- Added connectivity check to `claude.ai/code` and Anthropic's API endpoints
- Improved error handling for authentication and network connectivity issues


### Session Metrics Tracking
- Enhanced session tracking with new metrics:
  - `totalCost` - tracks API usage costs
  - `totalAPIDuration` - measures total API call duration
  - `lastInteractionTime` - monitors user activity
  - `readFileAllowedDirectories` and `writeFileAllowedDirectories` - tracks file system permissions


### Refactored Error Handling
- Simplified error logging function (renamed from `V0` to `A0`)
- Improved error message formatting and timestamp tracking


### ️ Code Reorganization
- Removed NPM prefix configuration functionality (`hQ2`, `xQ2`, `cQ2`, `iQ2` functions)
- Cleaned up unused imports and variables
- Updated SDK version references from 0.37.0 to 0.36.3
- Refactored global state management into a centralized `eA4()` function


### New Utilities
- Added comprehensive fuzzy search implementation using the Fuse.js algorithm
- Implemented string manipulation utilities (`PX`, `hY9`, `xY9`, `eC`, `nU2`, etc.)
- Added countdown timer component (`Qf2`) for UI timing displays


### Managing Approved Tools
```bash
# View and manage approved tools
/approved-tools

# The interface will show:
# - List of currently approved tools
# - Option to delete specific tools
# - Clear indication of which Bash commands are pre-approved
```


### Exiting the REPL
```bash
# Exit using the new commands
/exit
# or
/quit
```


### Fuzzy Command Search
```bash
# Find commands with fuzzy matching
/app  # might match /approved-tools
/ex   # might match /exit
```

## Notes
- The approved tools feature enhances workflow efficiency by reducing permission prompts for trusted commands
- Tool validation ensures safer execution of commands with proper parameter checking
- The fuzzy matching makes the CLI more user-friendly, especially for users who don't remember exact command names
