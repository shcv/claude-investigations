# Changelog for version 2.0.20

## 🎯 Highlights

Version 2.0.20 brings significant improvements to plugin management, hook execution visibility, and CLI automation capabilities. The most notable additions include new CLI commands for managing plugins (`install`, `uninstall`, `enable`, `disable`), full implementation of the Skill tool for executing skills directly from conversations, and enhanced real-time feedback during hook execution with detailed progress tracking.

## 🚀 New Features

### Plugin Management CLI Commands

**What:** Four new commands for managing plugins directly from the command line

**How to use:**
```bash
# Install a plugin from a marketplace
claude plugin install <plugin-name>
claude plugin install <plugin-name>@<marketplace>

# Uninstall a plugin
claude plugin uninstall <plugin-name>

# Enable a previously disabled plugin
claude plugin enable <plugin-name>

# Disable an installed plugin
claude plugin disable <plugin-name>
```

**Details:**
- Commands support aliases: `install` → `i`, `uninstall` → `remove`
- Installation automatically searches configured marketplaces
- Telemetry tracks CLI plugin operations separately from UI operations
- **Evidence**: `zSQ()` at line 465305, `CSQ()` at line 465337, `USQ()` at line 465355, `$SQ()` at line 465370

### Skill Tool (Full Implementation)

**What:** Complete implementation of the Skill tool, enabling Claude to execute skills and commands directly during conversations (previously existed only as a stub)

**How to use:**
Skills are invoked automatically by Claude when appropriate, or you can configure permission rules:
```bash
# In .claude/settings.local.json
{
  "permissions": {
    "allow": {
      "Skill": ["pdf", "xlsx", "custom-skill:*"]
    }
  }
}
```

**Details:**
- Supports both mode commands (high-priority) and regular skills
- Includes intelligent token budgeting (15,000 character default via `SLASH_COMMAND_TOOL_CHAR_BUDGET`)
- Permission system with wildcard patterns (e.g., `skill-name:*`)
- Skills are categorized by source: project, user, plugin, or managed
- Mode commands receive priority and full token allocation
- **Evidence**: `Mo1` initialization at line 429046, `W$Q()` prompt generator at line 428983, `nw` variable at line 428903

### Hook Execution Progress Display

**What:** Real-time visual feedback showing hook execution progress during tool operations

**How to use:**
Progress appears automatically when hooks are running:
```
Running PreToolUse hooks… (3/5 done)
  · pre-validate: npm run lint
  · security-check: ./scripts/check-secrets.sh
  · backup: git stash
```

**Details:**
- Shows hook event name (e.g., "PreToolUse", "PostToolUse")
- Displays progress counter when multiple hooks run
- Verbose mode shows individual hook names and commands being executed
- Progress UI disappears when all hooks complete
- **Evidence**: `mi1()` at line 366839, `LR5()` at line 366871, `CoB()` at line 455699, `UoB()` at line 455708, `n48()` at line 384434

### Context Usage Markdown Export

**What:** Export detailed context usage statistics as markdown tables for non-interactive sessions

**How to use:**
```bash
# Run context command in non-interactive mode
claude --output text context

# Output includes markdown tables:
# - Categories (with tokens and percentages)
# - MCP Tools
# - Custom Agents
# - Memory Files
# - SlashCommand Tool statistics
```

**Details:**
- Token counts formatted for readability (e.g., "1.5k" instead of "1500")
- Includes model information and total usage percentage
- Shows free space and autocompact buffer separately
- Agent sources identified (Built-in, Project, User, Local, Flag, Policy, Plugin)
- **Evidence**: `Ma6()` at line 301494, `rk()` token formatter at line 301491

### Project-Level MCP Server Configuration

**What:** Refactored project MCP server configuration loading into a dedicated function with enhanced scope handling

**How to use:**
Create `.mcp.json` in your project root:
```json
{
  "mcpServers": {
    "project-server": {
      "command": "node",
      "args": ["./server.js"]
    }
  }
}
```

**Details:**
- Dedicated function for loading project MCP configuration
- Proper error collection and reporting
- Supports environment variable expansion
- Explicitly scoped as "project" configuration
- **Evidence**: `dR0()` at line 280421

### Configurable Autocompact Threshold

**What:** Override the default autocompact threshold using an environment variable

**How to use:**
```bash
# Set autocompact to trigger at 75% of context capacity
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=75
claude

# Or inline
CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=90 claude
```

**Details:**
- Accepts percentage values from 1-100
- Falls back to default if invalid value provided
- Provides more control over memory management
- Useful for balancing context usage vs. compaction frequency
- **Evidence**: `Gn6()` at line 296137

### GitHub Action Entrypoint Detection

**What:** Automatic detection when Claude Code runs as a GitHub Action

**How to use:**
Set the environment variable in your GitHub workflow:
```yaml
- name: Run Claude Code
  env:
    CLAUDE_CODE_ACTION: true
  run: claude -p "Review this PR"
```

**Details:**
- Accepts flexible values: "1", "true", "yes", "on" (case-insensitive)
- Sets entrypoint to "claude-code-github-action" for proper telemetry
- Enables GitHub Action-specific behavior and logging
- **Evidence**: `yT8()` at line 469210, `jA()` validation at line 3336

## 💡 Improvements

### Enhanced Bash Security Checks

**What:** Improved detection of backtick command substitution with escape-aware parsing

**Details:**
- Dedicated `CV6()` function properly handles escaped characters
- Backtick checks now execute before other pattern matching
- More accurate detection prevents false positives from escaped backticks
- **Evidence**: `CV6()` at line 205030, `RV6()` at line 205296

### Terminal Output Performance

**What:** Optimized terminal rendering with synchronized updates

**Details:**
- Reduced function complexity in `d50()` at line 71278 (previously `U50()`)
- Removed separate stderr handling for improved performance
- Simplified output buffering logic
- All output now uses synchronized update sequences

### Autocompact Function Signature

**What:** Simplified autocompact summary function parameters

**Details:**
- Added `hasAppendSystemPrompt` parameter to `pi0()` at line 434307 (previously `Ei0()`)
- Better context awareness during compaction operations
- More precise token counting for system prompts

### Permission Checking Function

**What:** Enhanced tool permission checking with additional context parameter

**Details:**
- Updated `_M()` permission checker at line 458051 (previously `wM()`)
- Added fourth parameter for improved context handling
- More robust permission decision-making

## 🔧 Internal Changes

- Removed stub Skill tool implementation (`ld0` at v2.0.19:410872)
- Removed deprecated hook progress renderer (`aO5` at v2.0.19:366835, `sO5` at v2.0.19:366851)
- Removed unused clear terminal function (`ji2` at v2.0.19:208933)
- Removed empty placeholder functions (`RLQ`, `LRQ`, `eOQ`)
- Added PassThrough stream import for improved stream handling
- Added execSync and spawn imports for child process management
- Refactored Skills loading with enabled state check (function `tw8()` at line 450050)
- Added helper functions for plugin name parsing and matching (`HSQ()` at line 465275, `ms0()` at line 465282, `us0()` at line 465264)
- Added error handler `Ue1()` at line 465298 for plugin CLI operations
- Multiple variable initializations refactored for improved lazy loading
