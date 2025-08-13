# Changelog for version 1.0.70

Now let me create the comprehensive changelog based on all the findings:

# Changelog for version 1.0.70

## Major Changes

### 🎯 New Onboarding Experience
Claude Code now features a comprehensive onboarding flow for first-time users:
- **Interactive setup screens** guide you through initial configuration
- **Theme selection** to personalize your experience from the start
- **Security awareness** with explicit information about Claude's capabilities
- **Terminal optimization** with specific key binding recommendations for your terminal

When you first run Claude Code v1.0.70, you'll be greeted with setup screens that help configure:
- Visual theme preferences
- OAuth login or API key authentication  
- Terminal-specific settings (e.g., Option+Enter for new lines in Apple Terminal)

### 🔒 Enhanced Security Model
- **Explicit permission dialogs** for MCP servers and hooks
- **Trust management** for code execution permissions
- **API key validation** with user confirmation for custom ANTHROPIC_API_KEY usage
- Clear security notes displayed during onboarding about Claude's file system access

### 🧹 Major Codebase Refactoring
- **66.3% structural similarity** to v1.0.69 (significant reorganization)
- **2,889 functions removed** and 2,257 new functions added
- **Complete removal of Sentry telemetry** and error tracking for improved privacy
- Reduced external dependencies and cleaner module structure

## Privacy Improvements

### Removed Telemetry
All Sentry integration has been removed, including:
- Error tracking and reporting
- Performance monitoring
- User activity telemetry
- Database instrumentation (Express, PostgreSQL, MySQL)
- Browser and network instrumentation

This means Claude Code no longer sends crash reports or usage data to external services, enhancing user privacy.

## Technical Improvements

### Module System Updates
- Added support for `createRequire` from Node.js native module system
- Better CommonJS and ES module interoperability
- Improved module loading and dependency resolution

### Process Handling
- Reorganized Windows-specific ENOENT error handling
- Maintained full cross-platform process spawning support
- Better error messages for missing executables

### File System Operations
Enhanced file system capabilities with new imports for:
- File watching (`watchFile`, `unwatchFile`)
- Stream operations (`createReadStream`, `createWriteStream`)
- Path handling for both POSIX and Windows systems

## Developer Experience

### Terminal Integration
- Automatic detection and optimization for different terminal emulators
- Custom key binding recommendations based on your terminal
- Improved handling of iTerm2 settings restoration

### Authentication Flow
- Clearer distinction between Claude AI subscription and Console API billing
- Better handling of custom API keys with validation
- Streamlined OAuth login process

## Breaking Changes

### Export Structure
The main module now exports three functions:
- `showSetupScreens` - Displays the onboarding flow
- `setup` - Main initialization function
- `completeOnboarding` - Marks onboarding as complete

## Internal Changes

### Code Organization
- Significant module restructuring for better maintainability
- Removed monitoring and instrumentation code
- Simplified export structure
- Cleaner dependency graph

### Performance
- Reduced bundle size due to removed dependencies
- Faster startup time without telemetry initialization
- More efficient module loading

## Bug Fixes

- Improved Windows process spawning error handling
- Better Node.js version compatibility checks
- Fixed issues with terminal settings restoration after interruption

## Notes

This version represents a major cleanup and privacy-focused release. The removal of all telemetry and external monitoring makes Claude Code more privacy-respecting while maintaining all core functionality. The new onboarding experience ensures users have a smooth first-run experience with proper configuration and security awareness.
