# Changelog for version 0.2.96

# Claude Code v0.2.96 Changelog

## New Features

### Data Sharing and Development Partner Program
- **Development Partner Program Integration**: Organizations enrolled in the Development Partner Program now have their Claude Code sessions shared with Anthropic for service improvement and model training
  - New UI components display enrollment status and information
  - First-time users see a detailed message about data sharing
  - Subsequent sessions show a condensed enrollment indicator
  - Links to support documentation and admin settings included

### Cost Discounts for Partner Organizations
- **Discounted API Pricing**: Organizations in the Development Partner Program receive automatic cost reductions:
  - 90% discount on input tokens
  - 9% discount on prompt cache read tokens
  - Additional 12.5% discount on prompt cache write tokens
  - Applies to first-party Anthropic models only

## Enhanced Permission System

### Rule-Based File Access Control
- **Granular Permission Rules**: New pattern-based permission system for file operations
  - Support for glob patterns to allow/deny file access
  - Separate rules for read vs edit operations
  - Pattern prefixes:
    - `//` - Relative to root directory
    - `~/` - Relative to user's home directory
    - `/` - Relative to configured scope (project, user settings, etc.)
  
Example usage:
```bash
# Deny all access to sensitive files
claude code --deny-read "//etc/**" --deny-edit "~/.ssh/**"

# Allow specific directories
claude code --allow-read "/src/**" --allow-edit "/docs/*.md"
```

### Ignore Patterns Integration
- File ignore patterns from project settings now properly integrated with the permission system
- Automatic merging of ignore patterns with permission rules

## Technical Improvements

### Database Repair Mechanism
- **Automatic SQLite Recovery**: If the conversation database fails to open, Claude Code now:
  1. Detects the corruption
  2. Automatically rebuilds the better-sqlite3 native module
  3. Retries the connection
  4. Provides user feedback during the repair process

### OAuth Scope Changes
- **Always Request Full Permissions**: The `user:inference` scope is now always included in OAuth requests, regardless of environment
- Simplified authentication flow with consistent permission requests

## Bug Fixes

### Stream Handling
- Fixed missing stream import that could cause issues with certain operations
- Added proper PassThrough stream support for improved data handling

### Permission Context Management
- Migrated from React state-based permission context to Recoil atoms for better state management
- Ensures permission context persists correctly across component updates

### File System Operations
- Improved path resolution for permission rules
- Better handling of relative vs absolute paths in permission checks

## Removed Features

### Domain Whitelist for WebFetch
- Removed the hardcoded whitelist of allowed domains for web fetching
- WebFetch tool no longer restricts domains to a predefined list
- Security note removed about domain restrictions

### Deprecated Functions
- Removed several internal utility functions related to the old permission system
- Cleaned up unused domain validation logic

## Internal Changes

### Cache Management
- Added comprehensive cache clearing function (`k10`) that clears all tool caches
- Improves memory management during long sessions

### Model Cost Tracking
- Enhanced cost calculation to apply partner discounts dynamically
- Added telemetry for discount application

### UI Components
- New React components for data sharing notifications
- Improved styling and user messaging for partner program features
