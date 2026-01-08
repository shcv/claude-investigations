# Changelog for version 0.2.69

# Claude Code v0.2.69 Changelog

### Enhanced Permission System
- **Added deny permissions support**: The permission system now supports both `allow` and `deny` rules for tools, giving users more granular control over what tools can be used in their projects.
  
  **Usage example:**
  ```json
  {
    "permissions": {
      "allow": ["Read", "Write"],
      "deny": ["Bash", "WebFetch"]
    }
  }
  ```
  
  Previously, only `allow` rules were supported. Now you can explicitly deny specific tools even if they might be allowed by other rules.

### Improved Rule Management
- **New deny rules functionality**: Added support for "always deny" rules alongside the existing "always allow" rules. This provides a more comprehensive permission model where certain tools can be permanently blocked.

- **Rule source tracking**: Permission rules now track their source (e.g., "projectSettings", "localSettings") and behavior type ("allow" or "deny"), making it easier to understand why a tool is allowed or denied.

### Code Organization
- **Stream handling update**: Switched from default stream import to using named `PassThrough` import, improving code clarity and tree-shaking capabilities.

- **Process module update**: Changed from default process import to named `cwd` import for better modularity.

### New Utility Functions
- **Added `$j2` function**: A new string processing utility that splits text by newlines, processes each line, and rejoins them. This appears to be used for formatting multi-line content.

- **Added `Hb5` function**: Retrieves all deny rules from the permission system, formatting them with their source and rule details.

- **Added `Ab5` function**: Checks if a specific tool is denied by any rule, returning the matching deny rule if found.

### Permission Rule Handling
- **Fixed rule removal logic**: The `Pj2` function (formerly `Lj2`) now correctly handles both allow and deny rules when removing permissions from project settings. Previously, it only supported removing "allow" rules.

- **Fixed rule addition logic**: The `Tj2` function now properly handles both allow and deny rules when adding new permissions, instead of throwing an error for non-allow rules.

### New Configuration Schema
- The permission object schema (`Yb5`) now includes both `allow` and `deny` arrays:
  ```javascript
  {
    permissions: {
      allow: ["Tool1", "Tool2"],  // optional
      deny: ["Tool3", "Tool4"]     // optional
    }
  }
  ```

### Constants
- Added new constant `oy5 = 13` (appears to be a configuration value)
- Added new constant `ii5 = 3` (appears to be a configuration value)
- Removed constant `ci5 = 10`

## Breaking Changes

None identified. The changes maintain backward compatibility while extending functionality.

## Migration Notes

Projects using the previous permission system will continue to work as before. The new deny rules are optional and only take effect when explicitly configured. Existing "allow-only" configurations remain valid.
