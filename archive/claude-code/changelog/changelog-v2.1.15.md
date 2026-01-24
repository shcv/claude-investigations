# Changelog for version 2.1.15


## Summary

This release introduces internal cowork plugin directory support for development/testing workflows, activates API billing attribution headers, and significantly improves UI performance through comprehensive React Compiler automatic memoization adoption.

### Cowork Plugins Directory Support [Hidden]

**What**: A new hidden `--cowork` flag enables an alternate plugin directory for development and testing workflows.

**Usage**:
```bash
# Via CLI flag
claude plugins list --cowork
claude plugins install my-plugin --cowork

# Via environment variable
CLAUDE_CODE_USE_COWORK_PLUGINS=true claude
```

**Details**:
- When enabled, plugins are stored in `cowork_plugins/` instead of `plugins/`
- Settings file changes to `cowork_settings.json` instead of `settings.json`
- The `--cowork` flag is hidden from help output (`.hideHelp()`)
- Only available with `user` scope for certain commands; attempting to use with other scopes results in an error
- Can be enabled via `CLAUDE_CODE_USE_COWORK_PLUGINS` environment variable

**Evidence**: `Cn5()` at line 90980 (plugin directory selector, contains `"cowork_plugins"`), CLI definitions at line 560985 (contains `"--cowork", "Use cowork_plugins directory"`)

### API Billing Attribution Headers

**What**: Claude Code now sends version and entrypoint information in API requests for better usage tracking and diagnostics.

**Details**:
- Header format: `x-anthropic-billing-header: cc_version=2.1.15.{hash}; cc_entrypoint={entrypoint}`
- The entrypoint is read from `CLAUDE_CODE_ENTRYPOINT` environment variable (defaults to "unknown")
- Previously this header was stubbed to always return an empty string (gated by `tengu_ant_attribution_header_new` flag)

**Evidence**: `X61()` at line 158274 (attribution header generator, contains `"x-anthropic-billing-header"`)

### React Compiler Memoization

**What**: The entire UI layer has been updated to use React Compiler's automatic memoization through `useMemoCache`.

**Details**:
- In v2.1.14: Only 1 reference to `react.memo_cache_sentinel` (the definition in React internals)
- In v2.1.15: 736 usages across UI components
- A new shared `e()` function wraps `useMemoCache` for use across all components
- This provides automatic fine-grained memoization without manual `useMemo`/`useCallback` calls
- Should improve rendering performance by avoiding unnecessary re-renders

**Evidence**: `e = function(A) { return dn5.H.useMemoCache(A) }` at line 92039, 736 occurrences of `Symbol.for("react.memo_cache_sentinel")` checks throughout UI code

### Remote Mode State Tracking

**What**: Added internal state tracking for remote/teleport mode sessions.

**Details**:
- New `isRemoteMode` boolean state in the global state object
- Getter `Hf1()` and setter `Fg6()` functions added
- Used to modify behavior when running in remote session context (e.g., preventing empty input submission)

**Evidence**: `k6.isRemoteMode = A` at line 2350, usage checks at lines 548372 and 548402

## Notes

The `--cowork` flag and cowork plugins directory are hidden internal features, likely intended for Anthropic development and testing workflows. They are not documented in public help output and should be considered unsupported for general users.
