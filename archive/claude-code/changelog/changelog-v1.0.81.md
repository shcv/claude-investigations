# Changelog for version 1.0.81

## Highlights
Claude Code v1.0.81 introduces a powerful plugin system for extending functionality through custom commands and agents, improves concurrent query handling to prevent race conditions, and adds enhanced telemetry for better usage insights.

### Plugin System (Experimental)
**What:** Complete plugin framework for extending Claude Code with custom commands, agents, and hooks
**How to use:**
```bash
# Enable plugin system (currently requires environment variable)
export ENABLE_PLUGINS=1
claude

# Plugins are loaded from ~/.claude/plugins/repos/
# Structure: ~/.claude/plugins/repos/owner/repo/
```
**Details:**
- Supports three types of extensions: commands, agents, and hooks
- Git-based distribution with automatic updates via `git pull --ff-only`
- Plugin manifest format (`plugin.json`) with name, version, description, and author metadata
- Commands and agents are namespaced (e.g., `pluginName:commandName`)
- Individual plugins can be enabled/disabled per repository
- Supports `${CLAUDE_PLUGIN_ROOT}` variable for referencing plugin files
- Currently disabled by default - requires `ENABLE_PLUGINS` environment variable

### Prompt Caching Infrastructure (Disabled)
**What:** Infrastructure for caching API prompts to local JSON files
**Details:**
- Saves prompts to `.claude-cache/prompts/{sessionId}/{timestamp}.json`
- Currently disabled via hardcoded flag - likely for future release
- Captures complete prompt data including tools, system prompts, and messages
- Silent error handling to prevent interruption of normal operations

### Enhanced Concurrent Query Handling
**What changed:** Concurrent queries are now blocked with user feedback instead of causing undefined behavior
**Impact:** Prevents race conditions and provides clear messaging when users submit queries too quickly. Shows "Previous query still processing. Please try again." warning message.

### Output Style Management
**What changed:** Automatic cache refresh when output styles are created or modified
**Impact:** New output styles are immediately available without requiring a restart. The output-style-setup agent now includes a callback that clears the style cache after successful operations.

### Improved Telemetry
**What changed:** Added categorization for agent and output style usage tracking
**Impact:** Better insights into feature usage patterns with categories like:
- `agent:default`, `agent:custom`, `agent:{agentType}` for agent usage
- `outputStyle:default`, `outputStyle:custom`, `outputStyle:{styleName}` for output styles

### Plugin Agent Discovery
**What changed:** Agent discovery now supports plugin-provided agents in addition to built-in and custom agents
**Impact:** Plugin agents appear seamlessly integrated in the agent list with "Plugin: {pluginName}" attribution

### Fixed: Concurrent Query Race Condition
- **Issue:** Users could submit multiple queries simultaneously, causing unpredictable behavior
- **Cause:** Previous implementation only logged telemetry without preventing concurrent execution
- **Resolution:** Now blocks concurrent queries with proper mutex protection and user feedback

### Fixed: Output Style Cache Staleness
- **Issue:** Newly created output styles weren't immediately available
- **Cause:** Output style cache wasn't cleared after modifications
- **Resolution:** Added callback mechanism to clear cache after output-style-setup agent completes
