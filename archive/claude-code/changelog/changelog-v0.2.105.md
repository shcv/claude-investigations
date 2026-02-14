# Changelog for version 0.2.105

# Claude Code v0.2.105 Changelog


### Enhanced Model Selection
- **Simplified model selection UI**: The model selector now presents "Sonnet (recommended)" as the default option with clearer pricing information ($3/$15 per Mtok)
- **New model display format**: Model names now show both the user-friendly name and the actual model ID (e.g., "sonnet (claude-3-7-sonnet)")


### File Path Handling Improvements
- **New path display functions**: Added `x21()` for converting absolute paths to relative or home-relative paths (~/...) for cleaner display
- **Enhanced path resolution**: New `xO0()` function properly resolves relative paths (./), home paths (~/), and absolute paths


### @-mention File References
- **Markdown @-mention parsing**: The CLI now detects and resolves file paths mentioned with @ syntax in markdown content
- **Line number support**: File references can include line numbers using GitHub-style syntax: `@filename.js#L10-20`
- **Smart path detection**: Automatically identifies valid file paths in @-mentions while filtering out email addresses and other non-path content

Example usage:
```
# In your message to Claude:
"Please review the code @./src/main.js#L45-60 and compare it with @~/projects/other/utils.js"
```


### IDE Integration Enhancements
- **Installation status tracking**: The CLI now properly tracks and displays IDE extension installation status with detailed error messages
- **Visual installation feedback**: Shows success/error states for IDE extension installation attempts
- **Persistent error display**: Installation errors remain visible for 5 seconds with helpful troubleshooting advice


### MCP Server Notification Support
- **New `at_mentioned` notification handler**: IDE extensions can now notify Claude when files are mentioned, with automatic line number conversion
- **Real-time file selection**: IDE can push file references directly to Claude's context


### Memory Management Visualization
- **Hierarchical memory display**: Memory panel now shows file relationships with indentation for better understanding of included files
- **Parent-child file relationships**: Visual tree structure showing which files reference other files


### Cost Tracking Enhancements
- **Dual cost calculation**: Now tracks both "sticker price" and "final price" (with discounts applied)
- **More accurate token pricing**: Refactored cost calculation to use a unified `SB6()` function with usage object


### UI/UX Improvements
- **Theme reactivity**: New `C$6()` hook ensures UI components update immediately when theme changes
- **Better error messaging**: IDE extension errors now provide specific troubleshooting steps
- **Status panel enhancements**: The `/status` command now includes IDE installation information


### API Enhancements
- **Beta parameter support**: All API classes (Models, Completions) now properly handle `betas` parameter for accessing beta features
- **Improved parameter handling**: Cleaner separation of beta headers from request body parameters


### GitHub Action Template
- **Expanded event triggers**: GitHub action now responds to `edited` events on comments and reviews, not just `created` events
- **Pull request review support**: Added support for triggering on pull request review submissions
- **Updated action version**: Changed from `anthropics/claude-action@v1` to `anthropics/claude-action@beta`


### Error Handling
- **Better installation error recovery**: IDE extension installation errors are now caught and displayed gracefully
- **Improved notification error handling**: @-mention notifications include try-catch error handling


### Code Organization
- **New imports**: Added modular imports for `cwd`, `EOL`, `platform`, and `homedir` from Node.js
- **Stream handling**: Switched from direct `Stream` import to `PassThrough` for better stream manipulation
- **React hooks**: Added proper React imports for new UI components


### Performance
- **Lazy initialization**: IDE installation check now uses lazy loading pattern
- **Reduced unnecessary checks**: IDE status only updates when actually changed


### Internal Updates
- **Version bump**: Updated from 0.40.1 to 0.41.0
- **Renamed internal functions**: Various function renames for better code organization
- **New configuration constant**: Added `Y98 = 5` for configuration purposes
