# Changelog for version 2.0.57

## Highlights

Version 2.0.57 introduces a new versioned plugin caching system (behind a feature flag), adds guest passes promotional UI to help users discover the sharing feature, and includes important shell execution improvements for reliability and security.


### Versioned Plugin System (Experimental)
**What:** A comprehensive plugin versioning and caching system that stores plugins by version in a dedicated cache directory, supporting multiple installation scopes (user/project).

**How to enable:**
The feature is controlled by the `tengu_enable_versioned_plugins` experiment flag.

**Details:**
- Plugins are cached at `~/.claude/plugins/cache/{scope}/{plugin-name}/{version}/`
- New V2 file format (`installed_plugins_v2.json`) supports multiple installations per plugin
- Intelligent component copying analyzes plugin manifests to copy only necessary files
- Version resolution uses manifest version, git SHA (12 chars), npm registry, or timestamp
- Automatic migration from V1 format when enabled
- **Evidence**: New functions `_lA()` at line 165557, `klA()` at line 165606, `pQB()` at line 165628, `C59()` at line 476313


### Guest Passes Upsell Banner
**What:** Promotional UI elements that inform eligible users about their 3 available guest passes for sharing Claude Code.

**How it appears:**
- Banner in header showing `[✻] [✻] [✻] · 3 guest passes at /passes`
- Sidebar feed card with styled guest pass promotion
- Only shown to eligible users who haven't visited `/passes` yet
- Stops showing after 3 impressions

**Details:**
- Uses existing `/passes` command infrastructure (the command existed in v2.0.56)
- Tracks `passesUpsellSeenCount` and `hasVisitedPasses` in persistent state
- Analytics events: `tengu_guest_passes_upsell_shown`, `tengu_guest_passes_visited`
- **Evidence**: New functions `E69()` at line 474712, `O69()` at line 474842, `HT3()` at line 474824, `CI1()` at line 474832


### Shell Extended Glob Disabling
**What:** Automatically disables extended glob patterns in bash and zsh before executing commands to prevent unexpected shell expansion.

**How to use:**
```bash
# Runs automatically - no user action needed
# Before your command executes, Claude Code now runs:
# Bash: shopt -u extglob
# Zsh: setopt NO_EXTENDED_GLOB
```

**Details:**
- Prevents patterns like `!(pattern)`, `+(pattern)`, `*(pattern)` from expanding
- Only applies to bash and zsh shells
- Errors are silently suppressed to avoid breaking command execution
- **Evidence**: New function `NO6()` at line 244643, integrated at line 244719


### Output Redirection with cd Command Protection
**What:** Commands that combine directory changes (`cd`) with output redirection (`>`, `>>`) now require explicit user approval.

**Details:**
- Prevents potential path resolution bypass when final working directory cannot be determined
- Error message: "Commands that change directories and write via output redirection require explicit approval"
- Applies to compound commands like `cd /tmp && echo "data" > file.txt`
- Single commands without `cd` or without redirection are unaffected
- **Evidence**: Enhanced function `j85()` at line 310479, new parameter `G` for cd detection


### Removed /init Onboarding Modal
The first-run dialog that prompted users to set up CLAUDE.md has been removed. The `/init` command remains available for manual use.

Evidence: Removed functions `D89()` at line 474327, `H89()` at line 474425, `C89()` at line 474428 in v2.0.56


### Improved Cross-Project Conversation Resume UX
When resuming a conversation from a different directory, the UI now renders a proper React component instead of writing directly to stdout before exit. This provides more reliable message display with a 100ms delay to ensure rendering completes.

Evidence: New component `mb3()` at line 519894, state-based rendering at line 519854


### Zod Validation Library Upgrade
Internal upgrade to a newer version of the Zod schema validation library, including JSON Schema generation improvements and new validation utilities.

Evidence: New class `z50` at line 405825, new functions for JSON schema conversion at line 406332


### Border Rendering Fix
Fixed potential negative dimension calculation when rendering borders in narrow terminal widths.

Evidence: Modified function `r26()` at line 218562, added `Math.max(0, ...)` for width/height calculations


### Remote Session Hydration Improvement
Changed timing of remote ingress URL setting during session hydration to occur in a `finally` block, ensuring it's set even if hydration fails.

Evidence: Modified function `dH9()` at line 513155, moved `setRemoteIngressUrl` to finally block at line 513248
