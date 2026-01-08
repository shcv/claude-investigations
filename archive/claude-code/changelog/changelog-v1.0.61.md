# Changelog for version 1.0.61

### New Features

#### Enhanced Clipboard Integration for macOS
- **Improved image paste handling**: The CLI now includes better support for pasting images from the clipboard on macOS
- **Screenshot detection**: Automatically detects when users paste screenshots (e.g., from macOS screenshot tool) and handles them appropriately
- **Clipboard polling**: Added a 50ms polling mechanism to check for clipboard images when paste events are detected

#### Flag Settings Support
- **New settings type**: Added `flagSettings` as a new configuration type alongside existing settings (userSettings, projectSettings, localSettings, policySettings)
- **Flag settings path management**: New functions to get and set the flag settings path:
  ```bash
  # The CLI now supports flag-based configuration settings
  # These are separate from user/project/local settings
  ```

### Improvements

#### Better Command Injection Protection
- **Enhanced stdin handling**: Improved protection against command injection by adding `< /dev/null` to piped commands
- **Smart command parsing**: The CLI now intelligently detects pipe operators and adds null input redirection to prevent unintended stdin reading
- **Backtick handling**: Special handling for commands containing backticks to ensure proper escaping

#### Symlink Resolution
- **File operations now follow symlinks**: When reading files, the CLI now resolves symlinks and logs when reading through them
- **Better error handling**: Gracefully handles cases where symlink resolution fails

#### Installation Detection Improvements
- **Native installation PATH checking**: For native installations, the CLI now checks if `~/.local/bin` is in your PATH and provides specific instructions if it's missing
- **Windows-specific PATH handling**: Added proper path separator handling for Windows environments
- **Better diagnostics**: More detailed error messages when installation issues are detected

### Bug Fixes

#### Hook Display Filtering
- **Fixed duplicate hook messages**: Tool progress messages now properly filter out "running_hook" type messages to prevent duplication
- **Cleaner output**: Hook status messages are now displayed separately from tool progress

#### Settings File Handling
- **Flag settings exclusion**: The `flagSettings` type is now properly excluded from certain write operations (similar to `policySettings`)
- **Improved validation**: Better error handling when reading and parsing settings files

### Internal Changes

#### Code Organization
- **Stream imports consolidated**: Replaced multiple stream imports with PassThrough imports from both `node:stream` and `stream`
- **Function refactoring**: Several internal functions were restructured for better maintainability
- **Async operations**: Installation detection functions now use async/await pattern instead of synchronous execution

#### Environment Variable Handling
- **New helper function**: Added `X$2()` to parse boolean environment variables, recognizing "0", "false", "no", and "off" as false values

### Developer Notes

- The paste handling mechanism now includes references to whether content was pasted vs typed
- Installation type detection is more robust and provides actionable feedback
- The CLI maintains backward compatibility while adding these new features
