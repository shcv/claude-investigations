# Changelog for version 1.0.26

Based on the diff analysis, here's the changelog for Claude Code v1.0.26:

# Claude Code v1.0.26 Changelog

### Resume Conversation Command
- Added new `/resume` command to restore and continue previous conversations
- When using `claude resume` or `/resume`, you'll see a list of your past conversations
- Select a conversation to resume exactly where you left off
- Helpful tip: The CLI will periodically remind you that you can "Run claude --continue or claude --resume to resume a conversation"

### New Interaction Modes
- Introduced mode cycling for different interaction styles:
  - **Default mode**: Standard interaction
  - **Accept Edits mode**: Streamlined mode for accepting file changes
  - **Plan mode**: For planning complex implementations before coding
  - **Bypass Permissions mode**: Available when needed for advanced operations
- Modes cycle through in order, returning to default after bypass permissions

### Enterprise and Team Support
- Added support for new subscription tiers:
  - Claude Enterprise
  - Claude Team
  - Claude Max (previously supported)
  - Claude Pro (previously supported)
- The CLI now properly identifies and displays your subscription type

### IDE Extension Auto-Updates
- Enhanced automatic updates for VS Code and JetBrains IDE extensions
- Added support for Cursor and Windsurf editors alongside VS Code
- Extensions will automatically upgrade when newer versions are available
- Better error handling and reporting during extension installation

### Working Directory Management
- Improved handling of working directory changes in bash commands
- Added automatic reset to original directory when needed
- Better tracking of directory navigation during sessions

### Authentication Updates
- Refined OAuth token handling for different subscription types
- Improved organization type detection (enterprise, team, max, pro)
- Better error messages for subscription-specific features

### Performance
- Added streaming support with PassThrough for better real-time responses
- Improved memory management with new buffer limits (10,000 character limit for certain operations)
- More efficient file handling and validation

### Error Handling
- Better error reporting for missing plugin directories
- Improved version checking for IDE extensions
- Enhanced validation for JetBrains plugin installations

## Bug Fixes
- Fixed authentication flow for various subscription types
- Resolved issues with mode switching logic
- Corrected plugin installation path detection
- Fixed workspace role permission checks

## Notes
- Claude Pro users continue to use Sonnet 4 model (Opus 4 not available for Pro tier)
- The `--continue` flag is an alias for the new resume functionality
- Extension auto-updates can be controlled via environment variables if needed
