# Changelog for version 2.0.8

## Highlights
Version 2.0.8 focuses on cleanup and simplification, removing experimental features and completing the migration period for the new permissions system. The beta GitHub Actions workflow template has been removed, the migration helper for legacy settings has been retired, and internal session handling has been streamlined.


### Migration Helper for Legacy Settings Removed
**What:** The automatic migration from old-style `allowedTools` and `ignorePatterns` arrays to the new `.claude/settings.local.json` permissions format has been removed.

**Context:** In v2.0.5, Claude Code introduced a migration helper (`l4A() at line 351970`) that automatically converted:
- Old format: `allowedTools: ["Read", "Edit"]` and `ignorePatterns: ["node_modules/**"]` 
- New format: `.claude/settings.local.json` with permissions rules

**What this means:**
- Users upgrading from versions **before v2.0.5** directly to v2.0.8 or later will need to manually migrate their settings
- Users who already upgraded through v2.0.5-v2.0.7 are unaffected (their settings were already migrated)
- The new `.claude/settings.local.json` permissions format remains fully supported

**Evidence:** Migration functions `WdQ() at line 351945`, `JdQ() at line 351955`, and `l4A() at line 351970` in v2.0.5 are not called in v2.0.8


### Beta GitHub Actions Template Removed
**What:** The beta version workflow template for GitHub Actions integration has been removed. Only the stable `@v1` template remains.

**How it worked before:**
In v2.0.5, users setting up GitHub Actions could choose between two templates:
- Beta version using `anthropics/claude-code-action@beta`
- Stable version using `anthropics/claude-code-action@v1`

**How it works now:**
Only the stable `@v1` template is offered during setup, simplifying the decision for users.

**Evidence:** Beta template found at lines 407475-407659 in v2.0.5, completely absent in v2.0.8 which only contains the v1 template at lines 398115-398165


### Non-Functional customNotifyCommand Stub Removed
**What:** Removed dead code for custom notification commands that was never actually implemented.

**Details:**
The `customNotifyCommand` configuration option was introduced in v0.2.115 but never functioned—it always contained an early `return;` statement preventing execution. Users who set this option never received custom notifications as it was silently ignored.

**User impact:** Zero. The feature never worked, so removing it doesn't change behavior.

**Evidence:** Stub function `pb6() at line 406840` present in v2.0.5, removed completely in v2.0.8 (notification function `H01() at line 397504` no longer checks for customNotifyCommand)


### Session Persistence Deduplication Simplified
**What:** Removed client-side duplicate checking before persisting session entries, relying entirely on server-side validation.

**Technical details:**
In v2.0.5, the persist function (`K8B() at line 397234`) checked a local Map (`Dv1`) to skip API calls for session entries that had already been sent. In v2.0.8, this optimization was removed from the persist function (`KPB() at line 436398`), and all entries are now sent to the server.

**Implications:**
- Slightly more API calls in scenarios involving duplicate persist attempts
- Server remains authoritative for deduplication via `Last-Uuid` header validation
- Simpler client logic with fewer edge cases

**Evidence:** Duplicate checking logic at lines 397235-397240 in v2.0.5 is absent from the v2.0.8 persist function


### Billing Type Information Added to Telemetry
**What:** Internal telemetry now includes the organization's billing type alongside subscription type.

**Technical details:**
The function that gathers subscription information (`nC0() at line 397096` in v2.0.8, formerly `QN0() at line 406454` in v2.0.5) now extracts and includes `billingType` from the organization data when available.

**User impact:** None visible—this is purely for internal analytics.

**Evidence:** Line 23953 in diff shows addition: `if (B?.organization?.billing_type !== void 0) G.billingType = B.organization.billing_type;`


### Updated GitHub Actions Documentation Links
**What:** Documentation URLs in GitHub Actions workflow template comments now point to the dedicated CLI reference instead of the generic SDK page.

**How to use:**
When reviewing the generated workflow files, the comments now reference:
- **New URL:** `https://docs.claude.com/en/docs/claude-code/cli-reference`
- **Old URL:** `https://docs.claude.com/en/docs/claude-code/sdk#command-line`

**Details:**
The updated documentation provides more specific guidance for CLI usage in GitHub Actions workflows.

**Evidence:** Updated at lines 398162 and 398261 in v2.0.8 (formerly lines 407707 and 407765 in v2.0.5)


### Simplified GitHub Actions Example
**What:** The example `claude_args` in the workflow template is now clearer and more focused.

**Before:**
```yaml
# claude_args: '--model claude-opus-4-1-20250805 --allowed-tools Bash(gh pr:*)'
```

**After:**
```yaml
# claude_args: '--allowed-tools Bash(gh pr:*)'
```

**Why:** Removing the model specification makes the example less cluttered and focuses on the most common customization (tool permissions).

**Evidence:** Line 398163 in v2.0.8 shows simplified example (compare to line 407708 in v2.0.5)

## Version Notes

This changelog compares v2.0.5 to v2.0.8. Versions 2.0.6 and 2.0.7 are not present in the available archive, so changes may have occurred incrementally across these intermediate releases.
