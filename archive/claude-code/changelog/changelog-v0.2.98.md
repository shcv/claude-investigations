# Changelog for version 0.2.98

# Claude Code v0.2.98 Changelog


### Dynamic Model Configuration
The CLI now provides enhanced model selection capabilities with runtime configuration support:

- **Statsig Integration**: Model configuration now integrates with Statsig for A/B testing and feature flags
- **Environment Variable Priority**: The `ANTHROPIC_MODEL` environment variable takes precedence over other configuration methods
- **Fallback Chain**: Implements a robust fallback mechanism for model selection:
  1. Check environment configuration
  2. Check process environment variable
  3. Use Statsig-provided model
  4. Fall back to default model

Example usage:
```bash
# Set a specific model via environment variable
ANTHROPIC_MODEL=claude-3-opus-20240229 claude

# The model will persist across sessions if set in config
```


### Settings UI Enhancements
The settings panel now tracks configuration changes more comprehensively:

- **Change Tracking**: All setting modifications are now logged with telemetry events
- **Model Configuration**: Removed the separate model configuration UI in favor of environment-based settings
- **Verbose Output**: The verbose setting is now properly persisted and tracked


### MCP Configuration File
New support for `.mcp.json` configuration files in your project directory:

```javascript
function saveMcpConfig(config) {
  let mcpPath = path.join(cwd(), ".mcp.json");
  writeFileSync(mcpPath, JSON.stringify(config, null, 2), { encoding: "utf8" });
}
```

This allows you to configure MCP servers and tools on a per-project basis.


### Parent Process Detection
New utilities for detecting if Claude Code is running as a child of a specific process:

```javascript
function isChildOfProcess(pid) {
  if (!isProcessAlive(pid)) return false;
  // Walks up the process tree to check ancestry
  // Useful for IDE integration detection
}
```


### IDE Name Resolution
Enhanced IDE detection with friendly name mapping:

```javascript
function getIDEDisplayName(ideId) {
  switch (ideId) {
    case "vscode": return "VS Code";
    case "cursor": return "Cursor";
    case "windsurf": return "Windsurf";
    case "pycharm": return "PyCharm";
    case "intellij": return "IntelliJ IDEA";
    case "webstorm": return "WebStorm";
    // ... and many more IDEs
  }
}
```

Supports detection of 20+ different IDEs including JetBrains suite, VS Code variants, and Android Studio.


### Enhanced Limit Status Tracking
The rate limit status now includes time-based information:

```javascript
// Previous version
{ status: "limited" }

// New version
{ 
  status: "limited",
  hoursTillReset: 3  // Hours until rate limit resets
}
```

This provides users with better visibility into when they can resume using the service.


### Conversation Path Resolution
New functionality to resolve and track conversation paths across sessions:

```javascript
async function resolveConversationPaths() {
  // Automatically resolves parent-child relationships
  // between conversations for better context tracking
}
```

This helps maintain conversation context when switching between related discussions.

## Technical Improvements

- **Stream Handling**: Added `PassThrough` stream support for better data pipeline management
- **Removed Dependencies**: Cleaned up unused imports and variables for a leaner codebase
- **State Management**: Introduced new Recoil atoms for slow/capable model configuration with proper state persistence

## Bug Fixes

- Fixed model configuration not persisting across restarts
- Improved error handling in process detection utilities
- Enhanced telemetry event tracking for configuration changes
