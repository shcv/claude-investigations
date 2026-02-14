# Changelog for version 1.0.55


### IDE Auto-Detection and Multi-IDE Support
- **Enhanced IDE detection**: Claude Code now automatically detects running IDEs on your system and can suggest installing the appropriate extension
- **Multi-IDE selection**: When multiple IDEs are detected, users can select which one to install the extension for via a new selection interface
- **Supported IDEs expanded**: Full support for VS Code, Cursor, Windsurf, and all JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, PhpStorm, RubyMine, CLion, GoLand, Rider, DataGrip, AppCode, DataSpell, Aqua, Gateway, Fleet, Android Studio)


### Auto-Connect IDE Dialog
- New first-run dialog asking users if they want to enable auto-connect to IDE
- Users can configure this later with `/config` or the `--ide` flag
- Setting persisted as `autoConnectIde` in user preferences


### Improved IDE Integration UI
- **Redesigned welcome screen** for IDE extensions with:
  - Color-coded IDE branding (new `ide` color in theme)
  - Clear indication of which IDE extension was installed
  - Better visual hierarchy with context indicators (⧉ for open files and selected lines)
  - Diff preview indicators showing how changes will appear (+11 -22)
  - Clearer hotkey instructions (Cmd+Esc for Quick Launch, Cmd+Option+K for file references)


### New Configuration Options
- `autoInstallIdeExtension`: Control whether Claude Code automatically installs IDE extensions (defaults to true)
- `hasIdeAutoConnectDialogBeenShown`: Tracks whether the auto-connect dialog has been shown


### Better IDE Status Reporting
- Enhanced `/ide` command output with more detailed connection status
- Clearer error messages when IDE extensions fail to install
- Version mismatch detection between installed extension and server


### Platform-Specific Enhancements
- Improved Windows path handling for better cross-platform compatibility
- Better process detection across macOS, Windows, and Linux
- Platform-specific process keyword matching for accurate IDE detection


### UI/UX Improvements
- New `ide` theme color (rgb(71,130,200)) for IDE-related UI elements
- Spinner tips system foundation added (for future loading screen tips)
- Better escape key handling in dialogs
- More consistent dialog styling with rounded borders


### Refactored IDE Detection System
- Centralized IDE configuration in new `oc` object containing all IDE metadata
- New utility functions:
  - `BBA()`: Check if an IDE is VS Code-based
  - `EV()`: Check if an IDE is JetBrains-based
  - `tc()`: Detect running IDEs on the system
  - `HV()`: Get display name for an IDE
  - `IBA()`: Get current terminal IDE if applicable


### Improved Shell Command Execution
- Simplified shell command construction removing conditional snapshot loading
- Better stdin handling for shell commands using PassThrough streams
- More robust error handling in shell execution


### Permission System Enhancement
- New `QJ4()` function for enhanced permission prompt handling
- Better integration with tool permission system
- Improved error messages for permission denials

## Bug Fixes

- Fixed duplicate comment issue in generated code
- Improved handling of IDE extension installation failures
- Better error recovery when IDE connection cannot be established
- Fixed path normalization issues on Windows

## Breaking Changes

None - this release maintains backward compatibility with existing configurations and workflows.
