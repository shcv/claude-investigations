# Changelog for version 2.0.28

## 🎯 Highlights
Version 2.0.28 introduces marketplace branch/tag support for plugin repositories, enhanced cleanup when removing marketplaces, and several security and performance improvements including SSH pre-flight checks and agent transcript resumption capabilities.

## 🚀 New Features

### Marketplace Branch/Tag Support
**What:** Marketplaces can now be installed from specific branches, tags, or commit refs instead of only the default branch.

**How to use:**
```bash
# Install from a specific branch
claude marketplace add owner/repo#develop

# Install from a tag
claude marketplace add owner/repo#v1.2.3

# Install from a commit hash
claude marketplace add git@github.com:owner/repo.git#abc123
```

**Details:**
- Use `#ref` syntax after the repository name or URL to specify a branch, tag, or commit
- Updates to existing marketplaces now respect the specified ref
- Git clone operations include the `--branch` flag when a ref is specified (`Xd8() at line 264036`, `b5Q() at line 264043`, `Cd8() at line 264049`)
- Git update operations fetch and checkout the specified ref (`Bd8() at line 263476`)
- Clone and update logging now shows which ref is being used
- **Evidence**: New functions `Xd8() at line 264036`, `Bd8() at line 263476`, `b5Q() at line 264043`, `Cd8() at line 264049`; marketplace parsing extracts ref from URLs at line 263078-263135

### SSH Authentication Pre-flight Check
**What:** Claude now tests SSH authentication before attempting to clone GitHub repositories, avoiding unnecessary failed clone attempts for users without SSH keys configured.

**How it works:**
```bash
# When you add a marketplace, Claude now checks SSH first
claude marketplace add owner/repo

# If SSH is configured: "Cloning via SSH: git@github.com:owner/repo.git"
# If SSH is NOT configured: "SSH not configured, cloning via HTTPS: https://github.com/owner/repo"
```

**Details:**
- Executes `ssh -T git@github.com` to verify authentication before cloning
- Uses `BatchMode=yes` to prevent interactive prompts
- 2-second connect timeout and 3-second overall timeout for fast checks
- Automatically falls back to HTTPS without a failed clone attempt
- Provides clearer logging about SSH status
- **Evidence**: New function `Qd8() at line 263519`; usage in marketplace cloning logic at lines 263717-263750

### Agent Transcript Resumption
**What:** Agents can now resume from previous execution transcripts, allowing you to continue where a previous agent left off.

**How to use:**
```bash
# The Agent tool now accepts a 'resume' parameter
# When invoking an agent programmatically:
{
  "subagent_type": "investigator",
  "prompt": "Continue analyzing the codebase",
  "resume": "agent-abc123"  // ID of previous agent execution
}
```

**Details:**
- New `resume` parameter in Agent tool input schema
- Loads previous agent's message chain from transcript file
- Filters messages by agent ID and reconstructs conversation history
- Prepends previous messages to new prompt for continuity
- Previous messages are not re-recorded to session storage
- **Evidence**: New function `b_2() at line 465741`; `resume` parameter schema at line 449027-449032; resume logic at lines 449114-449130

### Help Command Fast Path
**What:** Commands ending with `--help` now bypass expensive API calls for prefix detection, significantly improving response time.

**Details:**
- Validates help commands using pattern matching before API calls
- Checks that command ends with `--help` and contains only valid flags
- Ensures no quotes are present (which would complicate parsing)
- Validates all tokens are alphanumeric or the `--help` flag
- Immediately returns the full command as its own prefix
- **Evidence**: New function `Yq8() at line 204259`; usage at line 204549

## ✨ Improvements

### Enhanced Marketplace Removal Cleanup
**What:** Removing a marketplace now automatically cleans up all references from settings files, preventing orphaned configuration entries.

**How it works:**
```bash
# When you remove a marketplace:
claude marketplace remove my-marketplace

# Now also removes:
# - extraKnownMarketplaces.my-marketplace from all settings files
# - All enabledPlugins entries like "plugin-name@my-marketplace"
# - Cleans userSettings, projectSettings, and localSettings
```

**Details:**
- Iterates through all settings files (user, project, local)
- Removes marketplace from `extraKnownMarketplaces`
- Removes all plugins associated with the marketplace from `enabledPlugins`
- Logs cleanup actions for each settings file
- Handles errors gracefully if settings write fails
- **Evidence**: Enhanced function `ruA() at line 263832` (replaced `suA()` from v2.0.27); cleanup loop at lines 263842-263868

### Improved Path Traversal Detection
**What:** Enhanced security check now detects paths with 3+ consecutive dots (e.g., `...`, `....`) as suspicious Windows path patterns.

**Why this matters:** Attackers sometimes use unusual dot sequences to bypass basic `..` filters. While `...` isn't standard, blocking it prevents potential exploits in path normalization edge cases.

**Details:**
- Adds regex check `/\.{3,}/` to Windows path validation
- Blocks paths like `C:\Users\....\file.txt` or `path/to/.../folder`
- Triggers manual approval prompt: "contains a suspicious Windows path pattern"
- Complements existing checks for reserved names, alternate data streams, and other Windows-specific attacks
- **Evidence**: Modified function `tf2() at line 465855` (renamed from `mf2()`); new check at line 465867

### Extended Git Operation Timeouts
**What:** Git clone and update operations now use 30-second timeouts instead of 5 seconds, improving reliability for large repositories or slow connections.

**Details:**
- Clone operations: timeout increased from 5000ms to 30000ms
- Update operations: timeout increased from 5000ms to 30000ms
- Reduces false failures on slow networks or large marketplaces
- **Evidence**: `Id8() at line 263544` uses `timeout: 30000`; `Bd8() at line 263476` uses `timeout: 30000`

### Terminal Output Height Detection
**What:** Improved detection of when terminal output needs to be redrawn, accounting for output height relative to terminal rows.

**Details:**
- Now considers whether output height exceeds terminal rows
- Checks both previous and current state for overflow conditions
- Prevents visual artifacts when output is taller than terminal
- **Evidence**: Enhanced function `OL0() at line 70043` (was `wL0()` in v2.0.27); checks `B.outputHeight >= B.rows` at line 70046

### Session Initialization with Current Working Directory
**What:** Session state now initializes with the actual current working directory instead of placeholder values.

**Details:**
- Calls `Uo2()` (likely `process.cwd()`) to get actual working directory
- Normalizes the path using `zo2()`
- Sets both `originalCwd` and `cwd` to the correct value at session start
- **Evidence**: Modified function `wo2() at line 3444` (was `Yo2()` in v2.0.27); uses `zo2(Uo2())` at line 3446

### Tool Permission Request Tracking
**What:** The permission stream class now tracks pending permission requests, enabling better state management and UI updates.

**Details:**
- New method `getPendingPermissionRequests()` on the stream class
- Returns array of pending `can_use_tool` requests
- Filters request map to find active permission prompts
- Stores request metadata alongside resolve/reject callbacks
- **Evidence**: Enhanced class `dzA at line 475314` (was `hzA` in v2.0.27); new method `getPendingPermissionRequests() at line 475580`; request storage at line 475650

### Agent Result Tracking
**What:** Agent execution results now include the agent ID for better tracking and correlation.

**Details:**
- Agent tool results now return `agentId` field along with content and usage stats
- Enables linking results back to specific agent invocations
- Supports transcript resumption and execution tracking
- **Evidence**: Modified function `Bv6() at line 448963` (was `dx6()` in v2.0.27); returns `agentId: B` at line 449019

### Model Override Support for Subagents
**What:** Agent model selection now supports an additional override parameter for finer-grained control.

**Details:**
- New third parameter `Q` in model resolution function
- If override is provided, it takes precedence over agent-specified model
- Falls back to agent model, then "inherit", then default
- Environment variable `CLAUDE_CODE_SUBAGENT_MODEL` still has highest priority
- **Evidence**: Modified function `akA() at line 144682` (was `lkA()` in v2.0.27); uses override parameter at line 144693

### Token Budget Capping
**What:** API requests now respect a token budget cap, adjusting both max_tokens and thinking budget_tokens when needed.

**Details:**
- New function ensures total tokens don't exceed specified budget
- Reduces thinking budget proportionally when capping is needed
- Prevents thinking budget from consuming all available tokens
- **Evidence**: New function `pb6() at line 460609`

### SessionStart Hook Context
**What:** Plugin SessionStart hooks now receive session context information for better initialization.

**Details:**
- Hooks receive session metadata when invoked
- Enables plugins to customize behavior based on session state
- **Evidence**: Modified function `Lz() at line 317267` (was `qz()` in v2.0.27); passes session context parameter `B` at line 317350

### Plugin Command Processing with Session ID
**What:** Plugin commands and skills now have access to session ID during processing.

**Details:**
- Session ID passed through to command/skill creation functions
- Enables session-aware plugin behavior
- Supports plugin state management across invocations
- **Evidence**: Modified functions `ZR2() at line 441792`, `YR2() at line 441892`, `yUA() at line 441803` now accept session ID parameter

### File Permission Check Consolidation
**What:** File write permission checks now use a centralized safety validation function for consistency.

**Details:**
- New `SL1()` function provides unified safety checks for write operations
- Checks for suspicious Windows paths, sensitive files, and permission rules
- Returns structured result with safety status and message
- Used by both direct file operations and tool permission handlers
- **Evidence**: New function `SL1() at line 465870`; used in `jL1() at line 466119` and `xn() at line 466119`

### Ripgrep Binary Loading Flexibility
**What:** Added support for custom ripgrep binary location via environment variable.

**Details:**
- New `RIPGREP_NODE_PATH` environment variable supported
- If set, loads ripgrep from specified path instead of bundled version
- Useful for custom deployments or testing
- Falls back to bundled ripgrep if not set
- **Evidence**: Modified function `To2() at line 3881` (was `Eo2()` in v2.0.27); checks `process.env.RIPGREP_NODE_PATH` at line 3882

## 🔧 Internal Changes

### Refactored Functions
- Session ID generation functions consolidated
- Permission stream class methods reorganized
- Skills loading function signatures updated for session context
- Git clone/update error handling refactored into shared `R5Q()` function at line 263494

### Import Optimizations
- Removed unused `stream` import
- Removed unused `node:child_process` import  
- Removed unused `node:process` import
- Added targeted imports: `execSync`, `spawn`, `readdir`, `readFile`, `PassThrough`, `homedir`, `openSync`, `existsSync`, `readFileSync`, `writeFileSync`, `dg6`, `cg6`, `pg6`
- Added process.cwd import: `import { cwd as iL0 } from "node:process"` at line 70611

### Code Organization
- Path validation logic consolidated into reusable `SL1()` function
- Git error handling extracted to `R5Q()` helper
- Agent ID generation moved to dedicated `HrA()` function at line 393160
- Transcript path functions reorganized (`bf2()` at line 465227, `PU()` at line 465250)

---

**Note:** This changelog focuses on user-visible changes and significant internal improvements. Many variable and function names appear random due to the code being previously minified. Line numbers reference the prettified v2.0.28 source file.
