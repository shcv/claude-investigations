# Changelog for version 1.0.128

## 🎯 Highlights
Version 1.0.128 introduces a comprehensive plugin marketplace system enabling plugin discovery and installation from multiple sources (npm, GitHub, git repositories, and local paths). The release also enhances the notification system with priority-based queuing and adds Claude Agent SDK support to better track programmatic usage.

## 🚀 New Features

### Plugin Marketplace System
**What:** A complete plugin distribution and installation infrastructure that enables discovering and installing plugins from centralized marketplaces.

**How to use:**
```bash
# Enable a plugin from a marketplace
# Use the format: plugin-name@marketplace-name
claude settings --set enabledPlugins.formatter@official=true
```

**Details:**
- Marketplace manifests (`marketplace.json`) define available plugins with metadata
- Multiple marketplace sources supported: URL, GitHub repos, Git URLs, NPM packages, and local files
- Plugin sources: npm packages, GitHub repositories, git URLs, local directories
- Plugin ID format: `plugin@marketplace` (e.g., `code-formatter@official-plugins`)
- Marketplaces cached in `~/.config/claude-code/plugins/marketplaces/`
- Plugin installations cached in `~/.config/claude-code/plugins/cache/`
- Strict mode (default) requires `plugin.json` manifest in plugin folder
- Non-strict mode uses marketplace entry as manifest if `plugin.json` is missing
- Supports plugin versioning, categories, tags, and rich metadata
- **Evidence**: `ba4()` marketplace loader at line 377017, `la4()` plugin cacher at line 377152, `aa4()` plugin loader at line 377392, marketplace schemas at lines 376680-376846

### Claude Agent SDK Integration
**What:** Added support for tracking when Claude Code is invoked through the Claude Agent SDK, enabling better analytics and contextual identity.

**How it works:**
When the `CLAUDE_AGENT_SDK_VERSION` environment variable is set, it's automatically included in telemetry and user agent strings.

**Details:**
- User agent string enhanced from `claude-cli/1.0.128 (external, <entrypoint>)` to `claude-cli/1.0.128 (external, <entrypoint>, agent-sdk/<version>)` when SDK is used
- New `agentSdkVersion` field in telemetry data (line 440142)
- Enables Anthropic to distinguish direct CLI usage from SDK-mediated usage
- **Evidence**: `IM()` user agent function at line 368228, telemetry field at lines 140142-440144

### Adaptive System Prompt Identity
**What:** Claude Code now uses different identity strings based on operational context (interactive CLI vs non-interactive SDK usage).

**Details:**
- **Interactive CLI mode:** "You are Claude Code, Anthropic's official CLI for Claude."
- **SDK with custom system prompt:** "You are Claude Code, Anthropic's official CLI for Claude, running within the Claude Agent SDK."
- **SDK without custom prompt:** "You are a Claude agent, built on Anthropic's Claude Agent SDK."
- Vertex AI provider always uses the standard CLI identity
- Enables context-aware behavior based on how Claude Code is being used
- **Evidence**: Identity selection function `A$1()` at line 366028, identity strings at lines 366024-366027

### File Checkpointing Enablement
**What:** Unlocked the file checkpointing ("Rewind") feature that allows reverting file changes to previous snapshots.

**Details:**
- Feature existed in previous versions but was hardcoded to disabled
- Now activatable via the `tengu_use_file_checkpoints` feature flag
- UI toggle added in settings: "Checkpointing (Rewind)" (line 400220)
- Can be disabled via `CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING` environment variable
- Tracks file modifications and creates snapshots at message boundaries
- Enables rewinding files to previous states during conversations
- Disabled in headless mode
- Still behind a feature flag for gradual rollout
- **Evidence**: Activation function `u7()` at line 380874, UI controls at lines 400220-400237

## ✨ Improvements

### Enhanced Notification System
**What:** Replaced simple single-notification system with a sophisticated priority-based queue.

**Details:**
- Four priority levels: immediate (0), high (1), medium (2), low (3)
- Notifications queued and displayed based on priority sorting
- "Immediate" priority can interrupt currently displayed notifications
- State structure: `{ current: notification | null, queue: notification[] }`
- Notifications support rich content via `jsx` property for React components
- Unique `key` property for deduplication
- Visual theming via `color` property
- Default 8000ms timeout (configurable via `timeoutMs`)
- **Evidence**: Priority queue function `Qz()` at line 363067, priority sorting `F19()` at line 363140, priority mapping at line 363139

### Optimized Credential Storage
**What:** Refactored credential storage from factory functions to singleton objects with memoized read operations.

**Details:**
- Keychain storage (`Hy1`) and plaintext storage (`pZ1`) now singleton objects
- Read operations memoized to avoid redundant file/keychain access
- Storage path computation cached via `jV0()` helper
- Explicit cache invalidation after `update()` or `delete()` ensures correctness
- Improved performance through reduced object allocation and I/O operations
- No user-visible changes to behavior
- **Evidence**: Keychain singleton at line 378779, plaintext singleton at line 378823, path memoization at line 378818

### Plugin Manifest Schema Enhancements
**What:** Extended plugin manifest schema with richer metadata and flexible configuration options.

**Details:**
- Support for `homepage`, `repository`, `license`, and `keywords` fields
- Plugin name validation enforces kebab-case (no spaces allowed)
- Author information with name, email, and URL
- Marketplace entries support categories and tags for discoverability
- Additional hooks via manifest: inline hook definitions or paths to hook files
- Additional commands/agents via manifest file references
- MCP server configurations can be specified in plugin manifests
- Semantic versioning support following semver.org specification
- **Evidence**: Plugin manifest schema at lines 376570-376602, hooks schema at line 376603, commands schema at line 376631

## 🔧 Internal Changes

- Refactored notification system architecture from component-local to global state management
- Renamed minified function names as part of routine obfuscation (e.g., `BM()` → `IM()`, `m7()` → `u7()`)
- Updated URL reference from `https://claude.ai/code` to `https://claude.com/claude-code` (line 385020)
- Added synchronized rendering control via ANSI escape sequences: `Mt1` (start) and `Ot1` (end) at lines 357199-357200
- Enhanced plugin loading with support for multiple command/agent paths via `commandsPaths` and `agentsPaths` arrays
- Added helper functions for git operations, npm package installation, and directory copying
- Improved error handling with specific error types like `cC` for invalid schemas

## 🔍 Developer Notes

### Plugin Marketplace File Structure
```
~/.config/claude-code/plugins/
├── known_marketplaces.json       # Registry of configured marketplaces
├── marketplaces/                 # Cached marketplace manifests
│   └── <marketplace-name>/
│       └── marketplace.json
└── cache/                        # Installed plugin files
    └── <plugin-name>/
        ├── .claude-plugin/
        │   └── plugin.json
        ├── commands/
        ├── agents/
        └── hooks/
```

### Marketplace Manifest Format
```json
{
  "name": "Official Plugins",
  "owner": { "name": "Anthropic", "email": "support@anthropic.com" },
  "plugins": [
    {
      "id": "formatter",
      "name": "Code Formatter",
      "source": { "source": "npm", "package": "@anthropic/formatter-plugin" },
      "category": "development",
      "tags": ["formatting", "code-quality"]
    }
  ]
}
```

### Breaking Changes
None - all changes are backward compatible or additive.
