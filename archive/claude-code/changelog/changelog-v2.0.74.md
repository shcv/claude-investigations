# Changelog for version 2.0.74


## Summary

This release adds agentic session search with AI-powered matching, automatic LSP plugin recommendations, and Shift+Enter keybinding support for Kitty, Alacritty, Zed, and Warp terminals. It also includes security hardening for process substitution in bash commands, performance improvements for large git diffs, and the removal of the experimental teammate/swarm feature.

### Agentic Session Search

**What**: AI-powered search that semantically understands your session history to find relevant past conversations.

**Usage**: In the session picker, type a search query and the system now uses Claude to intelligently match sessions based on meaning, not just keywords.

**Details**:
- Searches across session titles, tags, branches, summaries, and transcript content
- Prioritizes exact tag matches, then partial matches, then semantic similarity
- Uses a dedicated prompt to rank sessions by relevance
- Can cancel search with Escape while in progress

**Evidence**: `dbA()` at line 500168 (agentic search function, contains `"Agentic search"` log messages and `N77` system prompt)


### LSP Plugin Recommendations

**What**: Automatic recommendations for LSP plugins based on files you're working with, with one-click installation.

**Usage**: When you open a file type that could benefit from LSP support, a prompt offers to install a matching plugin:

```
LSP Plugin Recommendation
─────────────────────────
Plugin: typescript-lsp
Triggered by: .ts files

Would you like to install this LSP plugin?
> Yes, install typescript-lsp
  No, not now
  Never for typescript-lsp
  Disable all LSP recommendations
```

**Details**:
- Checks if required binary exists before recommending
- Prioritizes official marketplace plugins
- Remembers "never suggest" preferences per plugin
- Auto-disables after 3 consecutive ignored recommendations
- 28-second timeout before auto-dismissing

**Evidence**: `y29()` at line 472686 (recommendation lookup, contains `"[lspRecommendation]"` logging), `g29()` at line 472891 (UI component with `"LSP Plugin Recommendation"` title)


### Terminal Keybinding Setup: Kitty, Alacritty, Zed, and Warp

**What**: `/terminal-setup` now supports configuring Shift+Enter keybindings for Kitty, Alacritty, Zed terminals, plus guidance for Warp.

**Usage**:
```bash
claude
> /terminal-setup
```

**Details**:
- **Kitty**: Adds `map shift+enter send_text all \e\r` to `~/.config/kitty/kitty.conf`
- **Alacritty**: Adds keyboard binding to `~/.config/alacritty/alacritty.toml`
- **Zed**: Adds Terminal context binding to `~/.config/zed/keymap.json`
- **Warp**: Provides manual configuration instructions (Warp doesn't support custom Shift+Enter)
- Creates backups before modifying existing configs
- Warns if existing Shift+Enter binding conflicts

**Evidence**: `NB3()` at line 196977 (Kitty installer, contains `"Installed Kitty Shift+Enter key binding"`), `LB3()` at line 197031 (Alacritty installer), `MB3()` at line 197098 (Zed installer), `OB3()` at line 197093 (Warp guidance)


### Plugin Install Count Caching

**What**: Plugin marketplace now caches install counts for faster browsing.

**Details**:
- Caches are stored in the plugins config directory
- 24-hour cache expiry to keep data reasonably fresh
- Improves plugin browser responsiveness

**Evidence**: `RG7()` at line 507573 (cache reader with `"Install counts cache"` messages)


### Large Git Diff Performance Optimization

When working with large diffs (>500 files changed), Claude Code now uses `git diff --shortstat` first to quickly determine file counts before fetching full diff details. This prevents timeouts on very large changesets.

**Evidence**: `ks5()` at line 448558 (parses shortstat format with `filesCount`, `linesAdded`, `linesRemoved`), modified `Pl2()` at line 448405 (uses `Ps5 = 500` threshold)


### Process Substitution Security Check

Bash commands using process substitution (`>(...)` or `<(...)`) now require manual approval, as these can execute arbitrary commands that bypass normal validation.

**Evidence**: Modified `gX1()` at line 412086 (contains `"Process substitution (>(...) or <(...)) can execute arbitrary commands and requires manual approval"`)


### MCP Tool Token Tracking Improvements

Token counting for MCP tools now tracks which tools are actually loaded vs. deferred, providing more accurate context budget reporting when tool search is enabled.

**Evidence**: `jyA()` at line 402721 (returns `mcpToolTokens`, `deferredToolTokens`, `loadedMcpToolNames`)


### Queued Message Preview Improvements

The UI for queued messages now displays a more compact preview with better layout handling.

**Evidence**: `Bt2()` at line 463428 (queued message container with `isQueued` context)


## Bug Fixes

- Fixed thinking trigger word highlighting in user messages to properly segment text around trigger locations (`oF0()` at line 405859, `$o2()` at line 452842)


### Teammate/Swarm Feature Removed

The experimental teammate/swarm functionality has been completely removed from this release. This includes:
- `TeammateTool` and all spawn/assignTask operations
- `TeammateMailbox` communication system
- Swarm permission polling
- Plan mode swarm launching options
- `CLAUDE_CODE_AGENT_ID` environment variable handling for teammates

If you were using the swarm feature, this functionality is no longer available. The agent/subagent system (`Task` tool) remains available as the supported method for multi-agent workflows.

**Evidence**: 203 removed functions/variables related to teammate functionality, including `TeammateMailbox`, `TeammateTool`, swarm operations


## Notes

The teammate/swarm feature was an experimental capability for spawning multiple Claude instances in tmux panes. Its removal simplifies the codebase and focuses multi-agent workflows on the `Task` tool's subagent system, which provides a more controlled approach to parallelizing work.
