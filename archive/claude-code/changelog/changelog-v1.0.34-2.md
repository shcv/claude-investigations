# Changelog for version 1.0.34

The shebang changed to suppress Node warnings and enable source maps. This is a user-facing change since it affects how the CLI behaves.

Now I have all the information I need. Let me write the changelog:

# Changelog for version 1.0.34

## Summary

This is a maintenance release focused on internal improvements. The CLI now suppresses Node.js warnings for a cleaner output, and includes a new `forceLoginMethod` configuration option for enterprise deployments that require a specific authentication method.

## New Features

### Force Login Method Configuration
**What**: New configuration option to pre-select the authentication method during login.

**Usage**:
Add to your settings file:
```json
{
  "forceLoginMethod": "claudeai"
}
```

**Details**:
- Valid values: `"claudeai"` (Subscription Plan/Claude Pro/Max) or `"console"` (API Usage Billing/Anthropic Console)
- When set, users see "Login method pre-selected: [method]" during OAuth flow
- Useful for enterprise deployments with mandated billing arrangements
- Feature-flagged for telemetry via `tengu_oauth_claudeai_forced` and `tengu_oauth_console_forced`

**Evidence**: OAuth login component (search for `"Login method pre-selected"`)

## Improvements

### Cleaner CLI Output
Node.js warnings are now suppressed by default, providing cleaner terminal output during normal operation.

**Evidence**: Shebang line changed to `#!/usr/bin/env -S node --no-warnings --enable-source-maps`

### Smaller Bundle Size
The CLI package size is reduced by approximately 2,500 lines through replacing the webidl2js-based URL implementation with a lighter-weight alternative.

**Evidence**: Removed functions `FV1`, `CV1`, `NF2` containing webidl2js infrastructure (search for `"URLSearchParams Iterator"` in old version)

### Removed "Delete Allowed Tool" Confirmation Dialog
The confirmation dialog for deleting allowed tools from the permission list has been removed. Tool permissions can still be managed via the `/permissions` command.

**Evidence**: Removed component containing `"Delete allowed tool?"` string

## In Development

### Learn Mode [In Development]
**What**: New message type `learn_mode` and configuration option `learnMode` added.

**Status**: Stubbed — configuration option exists but the feature handler returns empty.

**Details**:
- Config schema accepts `learnMode: boolean` 
- Message renderer returns `null` for `learn_mode` type (no UI yet)
- Likely a future feature for educational or guided interaction modes

**Evidence**: Case handler returns `[]` (search for `"learn_mode"`)