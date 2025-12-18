# Changelog for version 2.0.22

## 🎯 Highlights

Version 2.0.22 removes the Development Partner Program data sharing functionality, introduces comprehensive user configuration support for MCP servers with interactive setup, adds session environment hooks for shell customization, and implements enterprise allowlist/blocklist controls for MCP server management.

## 🚀 New Features

### MCP Server User Configuration Support
**What:** Plugins can now request user-provided configuration values (API keys, paths, settings) through structured schemas defined in their manifest files.

**How to use:**
```bash
# When adding a plugin that requires configuration:
claude mcp add my-plugin

# If the plugin has user_config requirements, you'll see:
# Configure my-plugin server
# Field 1 of 3: API Key
# [Enter your value]

# Or configure an existing plugin:
claude mcp configure my-plugin server-name
```

**Details:**
- Plugins define `user_config` schemas in manifest.json with field types (string, number, boolean, file, directory)
- Interactive CLI prompts collect configuration values with validation
- Sensitive fields (API keys, tokens) are masked during input
- Configuration persisted to `~/.claude/userSettings.json` under `pluginConfigs`
- Server configs support variable substitution using `${user_config.fieldName}` syntax
- Validation ensures required fields are provided and types match schema
- **Evidence**: `CF1()` at line 280192, `q7B()` at line 280048, `fOQ()` at line 447320

---

### Session Environment Hooks
**What:** Shell environment can now be customized per session through hook scripts that persist throughout the session lifecycle.

**How to use:**
```bash
# SessionStart hooks can create environment files:
# Hook creates: ~/.claude/session-env/hook-1.sh

# Environment is automatically sourced before each Bash command
# Access the env file path via: $CLAUDE_ENV_FILE
```

**Details:**
- Hook scripts stored in `~/.claude/session-env/hook-{N}.sh` directories
- Multiple hooks are concatenated and sourced in numerical order
- SessionStart hooks receive `CLAUDE_ENV_FILE` environment variable pointing to persistent env file
- Environment modifications persist for entire session across all Bash tool executions
- Automatic cleanup of old session environment directories
- Cache invalidation supported for dynamic updates
- **Evidence**: `bNA()` at line 72216, `Vh1()` at line 247855, `ia0()` at line 454456

---

### Enterprise MCP Server Controls
**What:** Enterprise administrators can now restrict which MCP servers users are allowed to enable through allowlist and blocklist configurations.

**How to use:**
```bash
# Configuration stored in userSettings.json:
{
  "allowedMcpServers": [{"serverName": "approved-server"}],
  "deniedMcpServers": [{"serverName": "blocked-server"}]
}

# When users try to add blocked servers:
# Error: MCP server 'blocked-server' is not allowed by enterprise policy
```

**Details:**
- Allowlist: Only servers in the list can be enabled (empty allowlist blocks all servers)
- Blocklist: Explicitly blocked servers cannot be enabled regardless of allowlist
- Priority order: blocklist > allowlist > default (allow all)
- Enforcement applies when adding servers and when loading existing configurations
- Applies to all scopes: enterprise, user, project, local, and plugin
- Loaded servers automatically filtered by policy before being returned
- **Evidence**: `eR0()` at line 280589, `y7B()` at line 280584, `Ni()` at line 280640, `YP()` at line 280843

---

### Tool Permission Auto-Grant from Configuration
**What:** Tools can now be automatically approved via configuration, bypassing interactive permission prompts.

**Details:**
- Tools pre-approved in configuration skip permission prompts
- Telemetry event `tengu_tool_use_granted_in_config` tracks auto-granted tools
- Applies to both built-in and MCP tools
- **Evidence**: `QwQ()` at line 436163

## ✨ Improvements

### SessionStart Hook Responses Now Visible
**What:** SessionStart hook output is now displayed in interactive sessions, making it easier to see what environment setup is occurring.

**Details:**
- Hook responses with `hook_event: "SessionStart"` now appear at the beginning of session streams
- Only successful or non-blocking error responses are shown
- Improves visibility into session initialization process
- **Evidence**: `MT8()` at lines 5737-5743 in v2.0.22

---

### SDK Control for Max Thinking Tokens
**What:** SDK users can now dynamically change the maximum thinking tokens limit mid-session.

**How to use:**
```javascript
// Send control request in SDK:
{
  subtype: "set_max_thinking_tokens",
  max_thinking_tokens: 10000  // or null to disable
}
```

**Details:**
- Takes effect immediately for subsequent conversation turns
- Setting to null disables thinking tokens entirely
- Useful for adjusting reasoning depth based on task complexity
- **Evidence**: `MT8()` at lines 5859-5862 in v2.0.22

---

### Better Non-Interactive Session Tracking
**What:** Improved internal consistency for tracking non-interactive sessions throughout the codebase.

**Details:**
- Standardized API using options objects instead of scattered parameters
- Cleaner function signatures: `{querySource, agents, isNonInteractiveSession, hasAppendSystemPrompt}`
- Affects web fetch, conversation summarization, bug reporting, and command extraction
- **Evidence**: `Zn6()` at line 295359, `lGQ()` at line 408663, `cSQ()` at line 466310

## 🐛 Bug Fixes

### Fixed Tool Permission Checking Edge Case
**What:** Fixed potential crash when tools array is undefined during permission checking.

**Details:**
- Added null check for tools array before accessing
- Logs error and returns null gracefully instead of crashing
- Improves robustness of permission system
- **Evidence**: `$NQB()` at lines 1281-1285 in v2.0.22

---

### Fixed Escape Key Handling in History Search
**What:** Escape key now properly exits history search mode without cancelling the main session.

**Details:**
- Improved state management for history search modal
- Escape key handling now controlled by parent component
- Prevents unintended session cancellation when closing search
- **Evidence**: `mEQ()` at line 435476, `AwQ()` at line 436119

## 🗑️ Removed Features

### Development Partner Program Data Sharing
**What:** All functionality related to the Development Partner Program and automatic session data sharing with Anthropic has been removed.

**Previously included:**
- UI notifications about data sharing enrollment
- API calls to check organization's data sharing status
- Automatic sharing of Claude Code sessions for model training
- Cost discount calculations for enrolled organizations
- Git repository metadata collection when data sharing was enabled

**Impact:**
- Organizations previously enrolled will no longer see data sharing notifications
- Sessions are no longer automatically shared with Anthropic
- API usage cost calculations no longer include data sharing discounts

**Evidence**: Removed functions `Y7B()` at line 279890, `vd1()` at line 298392, `Ya6()` at line 298398, `Qn()` at line 298428, `Wa6()` at line 298432, `qFB()` at line 298438, `Ja6()` at line 298442, `EFB()` at line 298474, `Ia6()` at line 298488, `wFB()` at line 298512 in v2.0.21
