# Changelog for version 0.2.90

# Claude Code v0.2.90 Changelog

## New Features

### JetBrains IDE Integration Support
Claude Code now supports integration with JetBrains IDEs! This major addition enables users to connect Claude Code with popular JetBrains development environments.

**Supported IDEs:**
- PyCharm
- IntelliJ IDEA (Ultimate and Community)
- WebStorm
- PhpStorm
- RubyMine
- CLion
- GoLand
- Rider
- DataGrip
- AppCode
- DataSpell
- Aqua
- Gateway
- Fleet
- Android Studio

**How it works:**
- When `ENABLE_IDE_INTEGRATION="true"` is set, Claude Code can now detect and install the JetBrains plugin
- The plugin (`claude-code-jetbrains-plugin`) is automatically deployed to the appropriate plugin directories
- Claude Code intelligently detects existing installations and handles version management

**Usage:**
```bash
# Enable IDE integration
export ENABLE_IDE_INTEGRATION="true"
claude
```

### Tool Permission System
A new permission prompt system has been introduced for tool usage, providing better control over what actions Claude can perform.

**Key components:**
- Tools can now prompt for permission before execution
- Two permission behaviors: `allow` (with optional input modifications) or `deny` (with explanation)
- Permission decisions are tracked with detailed reasoning

**Example interaction:**
When Claude attempts to use a tool that requires permission, you'll see a prompt asking whether to allow the action. You can:
- Allow the tool to proceed (optionally with modified parameters)
- Deny the tool with a reason

### Enhanced Onboarding Flow
The onboarding process now returns a boolean indicating whether onboarding was shown, allowing for better flow control in automated scenarios.

## Improvements

### Better IDE Detection Logic
- Consolidated IDE detection into a single `R86()` function for VS Code-like editors
- Added comprehensive JetBrains IDE directory detection across macOS, Windows, and Linux
- Improved plugin version comparison using semantic versioning

### Stream Processing Enhancement
- Added `PassThrough` stream support from Node.js stream module for better data handling

### Path Resolution Updates
- New path utilities imported: `extname`, `isAbsolute`, `relative`, and `resolve`
- Better handling of absolute vs relative paths

## Internal Changes

### Refactored Functions
- `W56()` → `M86()`: IDE connection detection now includes additional safety check for `Ib` flag
- `q08()` → `g08()`: Onboarding function now returns boolean to indicate if onboarding was displayed

### Removed Functions
- Removed separate VS Code/Cursor/Windsurf detection functions in favor of unified approach
- Consolidated extension installation logic

### New Helper Functions
- `qh5()`: Finds JetBrains IDE configuration directories
- `$86()`: Locates JetBrains plugin directories
- `z86()`: Extracts plugin version from JAR files
- `EX1()`: Recursively copies directories
- `RX1()`: Recursively removes directories
- `U86()`: Manages JetBrains plugin installation and updates
- `C86()`: Checks if JetBrains plugin is installed
- `E86()`: Unified IDE extension detection
- `nQ6()`: Formats permission prompt results

## Bug Fixes

- Fixed potential issues with IDE integration when environment flags are not properly set
- Improved error handling in plugin installation processes

## Notes

This version represents a significant expansion in IDE support, moving beyond just VS Code-family editors to include the entire JetBrains ecosystem. The new permission system also provides users with more granular control over tool execution, enhancing security and user confidence when working with Claude Code.
