# Changelog for version 0.2.57

Based on my analysis of the diff file for version 0.2.57 of Claude Code CLI, here's the detailed changelog:

# Claude Code CLI v0.2.57 Changelog

## New Features

### 🎯 Project-Level Tool Permissions
- **Project settings support**: You can now configure allowed tools at the project level using `.claude/settings.json`
- Permissions can be defined in three scopes:
  - CLI arguments (`cliArg`)
  - Local settings (`localSettings`)
  - **NEW**: Project settings (`projectSettings`)
- Project-level permissions are automatically loaded and respected when working in a project directory

### 🎨 Enhanced User Experience

#### Improved Spinner Animations
- **Haiku-powered spinners**: The loading spinner now generates contextual, whimsical verbs based on your input
- When typing in prompt mode, the spinner dynamically generates related action words (e.g., "Searching", "Building", "Analyzing")
- Configurable spinner styles with haiku word generation for a more engaging experience

#### Better Error Handling
- Enhanced error messages with clearer formatting
- New `eT` error class for better error content handling
- Improved truncation of long error messages in bug reports

### 🛠️ Shell Improvements
- **Shell snapshot creation**: Automatically creates snapshots of shell configuration for better session persistence
- Improved shell detection and compatibility checking
- Better handling of shell configuration files (`.bashrc`, `.zshrc`, `.profile`)
- New `tT` function for setting the current working directory with validation

### 📊 Enhanced Output Display
- **(ctrl+r to expand)** indicator for truncated tool results
- Cleaner output formatting for tools with image detection
- Improved visual hierarchy with better spacing and layout

### 🔧 Developer Tools
- New background task management system with improved task classes:
  - `FL1`: Base task class with status tracking
  - `Kb2`: Background tasks using PersistentShell
  - `Fb2`: Background tasks using new shell command system
- Better task output streaming and management

## Improvements

### Performance & Efficiency
- Repository listing now warns when content exceeds 40,000 characters
- Optimized file listing with configurable ignore patterns for common directories
- Better handling of large repository structures

### Code Quality
- Improved message validation for tool use selection
- Enhanced tool permission context management
- Better separation of concerns in permission handling

### User Interface
- Cleaner configuration panel with better visual organization
- Improved theme labels in settings (e.g., "Light text" instead of just "dark")
- Tab key now works alongside Enter/Space for changing settings

## Technical Updates

### Dependencies & Imports
- New imports for better file handling: `basename`, `extname`, `dirname`, `join`, `resolve`
- Added `EOL`, `platform`, and `homedir` from OS module
- Improved stream handling with `Readable` and `PassThrough` streams

### Internal Changes
- Version bump to 0.2.57
- Updated changelog constant with current version
- Improved error tracking and telemetry
- Better handling of Git repository detection with `vL1` function

## Bug Fixes
- Fixed issue where messages without text or Edit tool usage were incorrectly validated
- Improved handling of shell process lifecycle
- Better error recovery in background task management

## Configuration Changes
- New `diffTool` setting in user configuration (defaults to "terminal")
- Project settings now support permission configurations
- Enhanced settings validation with proper schemas

This update focuses on improving the developer experience with better project-level configurations, more engaging UI elements, and robust shell handling capabilities. The addition of project-level tool permissions provides better security and flexibility when working across different projects.
