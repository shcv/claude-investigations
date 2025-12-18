# Changelog for version 0.2.67

# Claude Code v0.2.67 Changelog

## New Features

### Project Settings Management
- **New project permission system**: Added ability to manage tool permissions at the project level
  - The new `Pj2` function retrieves allowed tools from project settings
  - Tools can now be allowed/denied through a `projectSettings` configuration
  - Permission rules follow a structure with `source`, `ruleBehavior`, and `ruleValue` properties

### UI Enhancements
- **New divider component**: Added a customizable horizontal divider for better visual separation in the terminal UI
  - Use dividers with customizable characters and colors
  - Support for titled dividers with padding options
  - Example usage in the interface:
    ```
    ─────────────── Title ───────────────
    ```

## Improvements

### Permission System
- **Enhanced permission checking**: The permission removal function (`Lj2`, previously `Ej2`) now properly validates:
  - Ensures the rule source is `projectSettings`
  - Verifies the rule behavior is `allow`
  - Checks if the tool actually exists in the allowed list before attempting removal
  - Better error handling when modifying project permissions

### OAuth Role Detection
- **Improved admin detection**: The admin check function now handles cases where organization or workspace roles might be undefined
  - Returns `true` (admin access) when roles are not defined, providing a safer default
  - Previously would return `false` for undefined roles, potentially blocking legitimate access

## Technical Changes

### Code Organization
- Restructured imports for better modularity:
  - Stream operations now use named imports (`PassThrough`)
  - Process utilities use named imports (`cwd`)
  - File system operations consolidated with `existsSync` and `statSync`

### Internal Updates
- Added new internal functions for future features:
  - `mT5`: Placeholder for file reading functionality (currently returns `null`)
  - `oy2`: Placeholder function (currently no-op)
- New configuration variable `Ii5` set to value `5` (likely a retry or timeout setting)
- Added `View` constant (`ty5`) for UI component naming

## Breaking Changes
None - this version maintains backward compatibility with v0.2.66.

## Bug Fixes
- Fixed potential issues with permission management when project settings are missing or malformed
- Improved handling of undefined OAuth roles to prevent access issues
