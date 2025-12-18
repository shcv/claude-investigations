# Changelog for version 2.0.62

## 🎯 Highlights

This release introduces model deprecation warnings for Claude 3 Opus and Claude 3.7 Sonnet, enhances session history search with fuzzy matching across message content, adds a new Slack app installation command, and improves the sandbox configuration with PTY and git config access options.

## 🚀 New Features

### Model Deprecation Warnings
**What:** Claude Code now displays proactive warnings when using models approaching retirement dates.
**Details:**
- Warns users when using Claude 3 Opus (retiring January 5-15, 2026 depending on provider)
- Warns users when using Claude 3.7 Sonnet (retiring February-May 2026 depending on provider)
- Displays as a high-priority notification: "⚠ [Model Name] will be retired on [Date]. Consider switching to a newer model."
- Different retirement dates based on provider (Bedrock, Vertex, or first-party API)
- **Evidence**: `$x7()` at line 483888, `jX1()` at line 483910, `KW9()` at line 483919

### Slack App Installation Command
**What:** New `/install-slack-app` command to easily install the Claude Slack app.
**How to use:**
```
/install-slack-app
```
**Details:**
- Opens the Slack Marketplace page for Claude in your browser
- Controlled by `code_slack_app_install_banner` feature flag
- **Evidence**: `bH9` at line 501391, `hH9` at line 501394

### Chrome Extension Detection
**What:** Claude Code can now detect if the Claude for Chrome extension is installed and notify users if not.
**Details:**
- Detects extension across multiple Chrome profiles
- Shows notification: "Chrome extension not detected · https://claude.ai/chrome to install"
- Works on macOS, Windows, and Linux
- **Evidence**: `qG9()` at line 480314, `Zk7()` at line 480347, `NG9()` at line 480378

### Plugin Scope Installation
**What:** Plugins can now be installed with different scopes: user, project, or local.
**How to use:**
When installing a plugin via the UI, you can now choose:
- "Install for you (user scope)" - Available across all projects
- "Install for all collaborators on this repository (project scope)" - Shared via `.claude/settings.json`
- "Install for you, in this repo only (local scope)" - Local only, not committed
**Details:**
- Plugin installation now tracks scope in `installed_plugins_v2.json`
- Supports migration from V1 plugin installation format
- **Evidence**: `_G9()` at line 480734, `rE()` at line 483476, `eI9()` at line 483520, `Ez9()` at line 511472

## ⚡ Improvements

### Enhanced Session History Search
**What:** Session history search now supports fuzzy matching across actual message content, not just titles and summaries.
**Details:**
- Uses Fuse.js for fuzzy matching with configurable threshold
- Shows matching snippets highlighted in search results
- Searches across message content from conversations
- Results sorted by combination of recency and match score
- **Evidence**: `Mf7()` at line 503542, `Lf7()` at line 503527, `Nf7()` at line 503053, Fuse search implementation at line 6186

### Improved Plugin Discovery UI
**What:** The plugin browser now includes pagination and improved scrolling for better navigation.
**Details:**
- Pagination indicator shows current position (e.g., "(1/15)")
- Visual scroll indicators for "more above" and "more below"
- Improved keyboard navigation with j/k support
- **Evidence**: `js()` at line 510132, `Ah7` (page size = 5) at line 510206

### Plugin Error Display
**What:** Enhanced plugin error messages with categorized error types and suggested fixes.
**Details:**
- Errors categorized by type: path-not-found, git-auth-failed, network-error, manifest-parse-error, etc.
- Provides actionable suggestions for each error type
- **Evidence**: `Yh7()` at line 512782, `Jh7()` at line 512822, `Mz9()` at line 512863

### EnterPlanMode Tool Enhancement
**What:** The EnterPlanMode tool description has been significantly expanded with better guidance on when to use it.
**Details:**
- Now explicitly recommends using plan mode proactively for non-trivial tasks
- Adds "New Feature Implementation" and "Code Modifications" categories
- Provides more nuanced examples including "Add a delete button to the user profile"
- Changes from "err on the side of starting implementation" to "err on the side of planning"
- **Evidence**: `nc2` at line 435451

### Sandbox PTY Support
**What:** macOS sandbox now supports pseudo-terminal (PTY) operations when configured.
**Details:**
- New `allowPty` configuration option
- Enables `/dev/ptmx` and `/dev/ttysXXX` device access
- Required for programs that need terminal control
- **Evidence**: `m64()` at line 49306, PTY sandbox rules at lines 5602-5612

### Sandbox Git Config Access Control
**What:** New `allowGitConfig` option to control sandbox access to `.git/config` files.
**Details:**
- Defaults to false (no access)
- When disabled, `.git/config` is excluded from sandbox read allowlist
- Accessible via `filesystem.allowGitConfig` configuration
- **Evidence**: `xc0()` at line 49880, sandbox path handling at line 5178

### UI Rendering Optimization
**What:** Improved terminal UI rendering with dirty node tracking to avoid unnecessary redraws.
**Details:**
- Nodes now track dirty state to skip unchanged subtrees during render
- Optimized style comparison to avoid unnecessary updates
- **Evidence**: `ue()` at line 194210, `Vu1()` at line 194183, `Fu1()` at line 194187

## 🔧 Other Changes

### Settings Source Tracking
- Added `flagSettings` as a new settings scope for flag-based settings
- Settings now track their source (managed, user, project, local, flag) for better debugging
- **Evidence**: `flagSettings` at line 2253, scope handling at lines 2476-2481

### Plugin Installation Improvements
- Plugin installation now uses versioned paths consistently
- Better handling of local vs. remote plugins during installation
- Migration support from V1 to V2 plugin installation format
- **Evidence**: `XV0()` at line 480814, `zk7()` at line 480667
