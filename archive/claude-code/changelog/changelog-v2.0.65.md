# Changelog for version 2.0.65

## Highlights

This release introduces a new `/tag` command for organizing sessions with searchable labels, a unified `TaskOutput` tool replacing previous separate agent/bash output tools, and enhanced MCP tool support with deferred loading capabilities for improved token efficiency. It also adds git worktree detection, remote settings synchronization infrastructure, and headless profiling metrics.

### Session Tagging with `/tag` Command
**What:** A new command to add searchable tags to your sessions for better organization and retrieval.
**How to use:**
```bash
/tag bugfix        # Add tag to current session
/tag bugfix        # Run again to remove (toggle behavior)
/tag feature-auth  # Use descriptive names
```
**Details:**
- Tags appear after the branch name in `/resume` list
- Tags are searchable with `/` search functionality
- Running the same tag command again removes the tag (toggle)
- **Evidence**: `c55()` at line 483604, `HG0()` at line 491331, `nh2()` at line 491336

### Unified TaskOutput Tool
**What:** New consolidated tool that retrieves output from any task type (background shells, agents, or remote sessions).
**How to use:**
```bash
# Model uses TaskOutput instead of separate BashOutput/AgentOutputTool
TaskOutput --task_id <id> --block true --timeout 30000
```
**Details:**
- Replaces the previous `BashOutput` and `AgentOutputTool` with a single unified interface
- Works with local bash tasks, local agents, and remote agent sessions
- Supports blocking and non-blocking retrieval modes
- **Evidence**: `BH = "TaskOutput"` at line 375878, `R31` tool definition at line 454807

### MCP Tool Deferred Loading
**What:** MCP tools can now be loaded on-demand to reduce initial token overhead.
**How to use:**
- Configure in settings; MCP tools marked for deferred loading won't count against initial token budget
- Tools load when needed during conversation
**Details:**
- New "MCP tools (deferred)" category shows in `/context` breakdown
- Deferred tools excluded from main token total until used
- **Evidence**: `deferredToolTokens: H` at line 380202, `defer_loading` property in `fQ1()` at line 457318

### Git Worktree Detection
**What:** Claude Code now detects and works with git worktrees for multi-branch development workflows.
**Details:**
- Automatically detects worktree configurations
- Reports worktree paths to session context
- Telemetry event `tengu_worktree_detection` tracks usage
- **Evidence**: `worktree` parsing logic starting at line 2461

### Prompt Suggestions Enhancement
**What:** After task completion, Claude now suggests the next logical prompt based on conversation context.
**Details:**
- Suggestions appear as placeholder text in input field (press Enter to accept)
- Filters inappropriate suggestions (too long, gratitude responses, etc.)
- Telemetry tracks acceptance rates
- **Evidence**: `HN2()` at line 440590, `wN2()` at line 441103, `_B5()` at line 441117

### Headless Profiling System
**What:** Built-in performance profiling for SDK/headless usage with turn-level metrics.
**How to enable:**
```bash
export CLAUDE_CODE_PROFILE_STARTUP=1  # Enable verbose logging
```
**Details:**
- Tracks key checkpoints: system message generation, query start, first response chunk
- Reports metrics via telemetry for 5% of sessions
- **Evidence**: `e30()`, `p1A()`, `A80()` functions at lines 445732-445745

### File Suggestion Hook
**What:** Custom hook support for file path suggestions during `@` mentions.
**Details:**
- Configure via `fileSuggestion` in hooks settings
- Supports command-type hooks that receive query context and return file paths
- **Evidence**: `E60()` at line 460683, hook check in `dH2()` at line 424845

### CLI Plugin Management Commands
**What:** Full CLI support for plugin enable/disable/update operations.
**How to use:**
```bash
claude plugin enable <name> --scope user
claude plugin disable <name> --scope project
claude plugin update <name> --scope local
```
**Details:**
- Enable disabled plugins: `jRA()` at line 451234
- Disable enabled plugins: `PRA()` at line 451237
- Update specific plugins: `SRA()` at line 451240
- Supports scope-aware operations (user/project/local)
- **Evidence**: `Ld2()`, `Md2()`, `Od2()`, `Rd2()`, `Td2()` CLI handlers at lines 497930-498062

### Auto-Update Installed Marketplaces
**What:** Background auto-update for installed marketplace plugins.
**Details:**
- Runs automatically on startup (non-headless mode only)
- Updates each marketplace sequentially with error isolation
- **Evidence**: `_j2()` at line 450763

### Teleport URLs
**What:** Infrastructure for generating session teleport links to claude.ai.
**Details:**
- Generates URLs in format: `https://claude.ai/code/{sessionId}`
- CLI command format: `claude --teleport {sessionId}`
- **Evidence**: `TtB()` at line 369714, `_tB()` at line 369717

### Task Status Attachments
Background tasks now include delta summaries in attachments for smoother conversation flow. New function `o78()` at line 358386 handles task status attachment generation with status, description, and delta summary fields.

### Remote Settings Infrastructure
Added framework for enterprise remote settings synchronization including authentication, validation, and local caching. New file `remote-settings.json` at line 3494 and related authentication handling.

### LSP Tool Position Parameters
LSP operations now use 1-based line/character positions (matching editor display) instead of 0-indexed. This affects `goToDefinition`, `findReferences`, `hover`, `documentSymbol`, and `workspaceSymbol` operations. Evidence: Schema definitions at line 455590.

### Settings Source Display
New function `zy2()` at line 462818 provides detailed information about active settings sources, distinguishing between remote and local enterprise managed settings.

### Plugin Installation Tracking V2
Plugin tracking migrated to v2 format with per-installation metadata including scope, project path, version, and timestamps. Functions `Q31()` at line 447959 and `IM2()` at line 447977 handle the new format.

### Session Search Improvements
Sessions can now be searched by tag in addition to content. Function `$h()` at line 491493 supports multi-path session loading with tag filtering.

### Auto-Compact Environment Control
New `DISABLE_COMPACT` environment variable allows disabling auto-compact behavior. Function `wAA()` at line 4001 checks this setting.

### MCP Tool Search Integration
New MCP tool discovery tool schema (`XwZ`, `WwZ`) at line 456454 enables dynamic MCP tool querying with configurable result limits.
