# Changelog for version 2.0.25

## 🎯 Highlights
Version 2.0.25 introduces session-only plugin loading via `--plugin-dir`, adds session titles to memory templates for better organization, and enhances editor integration with Sublime Text wait flag support.

## 🚀 New Features

### Session-Only Plugin Loading
**What:** Load plugins from local directories for the current session without permanently installing them
**How to use:**
```bash
# Load plugins from one or more directories
claude --plugin-dir ./my-plugins --plugin-dir ../shared-plugins

# Plugins are active only for this session
claude --plugin-dir /path/to/custom/plugins chat
```
**Details:**
- Plugins loaded with `--plugin-dir` are marked with `@inline` source designation
- Multiple plugin directories can be specified by repeating the flag
- Plugins are loaded after standard installed plugins
- Path validation occurs before loading - non-existent paths are logged and skipped
- Session plugins persist only for the current command execution
- **Evidence**: `Td6()` function at line 264116, `GQA()` at line 3778, `YQA()` at line 3781, CLI option at line 475753 in v2.0.25

### Session Title in Memory Template
**What:** Session memory now includes a dedicated title section for quick identification
**How to use:**
The session memory agent automatically generates a "Session Title" section when creating or updating session notes:
```markdown
# Session Title
_A short and distinctive 5-10 word descriptive title for the session. Super info dense, no filler_
```
**Details:**
- Appears as the first section in session memory notes
- Designed to be information-dense and distinctive
- Makes it easier to identify and navigate between different work sessions
- Complements the existing 7 sections (Task specification, Files and Functions, etc.)
- **Evidence**: Template variable `ng8` at line 467211 in v2.0.25 (vs `dg8` at line 467131 in v2.0.24)

## ✨ Improvements

### Environment Variable for Session Memory Model Selection
**What:** Control which AI model handles session memory updates via environment variable
**How to use:**
```bash
# Use Haiku for faster, more cost-effective session memory updates
export USE_HAIKU_SESSION_MEMORY=1
claude chat

# Default behavior (Sonnet) - no environment variable needed
claude chat
```
**Details:**
- Defaults to Sonnet for highest quality session memory extraction
- Set `USE_HAIKU_SESSION_MEMORY=1` to use Haiku for faster, cheaper updates
- Useful for rapid iteration or cost-conscious workflows
- **Evidence**: `Gu8()` function at line 467294 in v2.0.25 uses conditional model selection vs inline object at line 467224 in v2.0.24

### Enhanced Editor Wait Flag Support
**What:** Improved external editor integration now supports Sublime Text with proper blocking behavior
**Details:**
- VS Code continues to use `code -w` for blocking behavior
- Sublime Text now properly configured with `subl --wait`
- Refactored from inline conditional to extensible configuration map
- Makes future editor additions straightforward
- **Evidence**: `Fy8` configuration map at line 431215 with usage at line 431189 in v2.0.25 vs inline ternary at line 431126 in v2.0.24

### Debug Log Path Display
**What:** Debug mode now shows the actual log file path instead of the symlink
**Details:**
- Previously displayed: `~/.claude/debug/latest` (symlink)
- Now displays: `~/.claude/debug/1234567890.txt` (actual file)
- Makes it clearer which specific file is being written to
- Improves troubleshooting when multiple debug sessions exist
- **Evidence**: `fc()` function at line 3821 used at lines 441483 and 441622 in v2.0.25

## 🔧 Internal Improvements

- Refactored Node.js module imports for better code organization
- Separated session memory template structure from update instructions
- Streamlined debug logging path resolution logic
