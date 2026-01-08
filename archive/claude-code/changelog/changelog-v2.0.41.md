# Changelog for version 2.0.41

## Highlights

Version 2.0.41 introduces major improvements to git workflow management, including automatic tracking of uncommitted changes and unpushed commits, enhanced multi-agent planning with structured 4-phase workflows, and better terminal rendering with improved ANSI escape sequence handling and Unicode support.

### Git Repository Status Tracking
**What:** Comprehensive git status detection for branch management and workflow automation

**How it works:**
- Automatically detects commits ahead of default branch (main/master)
- Checks for uncommitted changes in working directory
- Detects unpushed commits to remote
- Warns before switching branches with uncommitted/unpushed work

**Details:**
- New functions: `lJ1()` at line 87137 (comprehensive status aggregator), `Hn9()` at line 87127 (commit counting), `dJ1()` at line 87177 (default branch detection)
- Integrated into branch switching workflows
- Prevents accidental loss of work during teleport operations
- **Evidence**: `lJ1()` at line 87137, `Hn9()` at line 87127, `dJ1()` at line 87177 in pretty-v2.0.41.js

### Uncommitted Changes UI
**What:** Interactive dialog when switching branches with uncommitted or unpushed changes

**How to trigger:**
```bash
# Automatically appears when switching branches with uncommitted work
claude  # then use teleport feature
```

**Details:**
- Shows different warnings for uncommitted changes vs unpushed commits
- Provides three options: Continue without committing, Commit and push changes, Cancel operation
- Prevents data loss during branch switches
- **Evidence**: `uT2()` at line 428379 in pretty-v2.0.41.js (replaces unrelated function at line 428358 in v2.0.37)

### Automatic Upstream Branch Setup
**What:** Automatically configures upstream tracking after git checkout

**How it works:**
After checking out a branch, automatically runs:
```bash
git branch --set-upstream-to=origin/<branch> <branch>
```

**Details:**
- Checks if upstream is already configured
- Verifies remote branch exists before setting upstream
- Logs all actions for debugging
- Called automatically after branch checkout operations
- **Evidence**: `tl5()` at line 427581 in pretty-v2.0.41.js (new function, doesn't exist in v2.0.37)

### Brace Expansion for CLAUDE.md Paths
**What:** Glob-style brace expansion in CLAUDE.md frontmatter configuration

**How to use:**
```markdown
paths: src/{components,utils}/{*.ts,*.tsx}
```

Expands to:
```
src/components/*.ts
src/components/*.tsx
src/utils/*.ts
src/utils/*.tsx
```

**Details:**
- Custom implementation supporting nested braces
- Recursive expansion for complex patterns
- Used in CLAUDE.md frontmatter `paths:` field
- **Evidence**: `nP0()` at line 52984, `aP0()` at line 53002 in pretty-v2.0.41.js (not present in v2.0.37)

### VCS Account Linking
**What:** OAuth-based GitHub account linking with Claude account

**How it works:**
- Automatically detects GitHub authentication via `gh` CLI
- Links GitHub account to Anthropic backend
- Enables enhanced GitHub integration features

**Details:**
- API endpoint: `https://api.anthropic.com/api/claude_code/link_vcs_account`
- Feature flag: `vcs_account_linking_enabled`
- Runs in background after authentication
- Tracks organization UUID and billing type
- **Evidence**: `cl5()` at line 426586, `mt1()` at line 426608 in pretty-v2.0.41.js (not in v2.0.37)

### Conductor App Detection
**What:** Detects when running inside Conductor desktop app

**Details:**
- Checks `process.env.__CFBundleIdentifier === "com.conductor.app"`
- Allows behavior customization for Conductor environment
- Similar to existing IDE detection (VSCode, Cursor, etc.)
- **Evidence**: `Vb9()` at line 47155 in pretty-v2.0.41.js (v2.0.37 has different code at line 47461)

### Glob Operations with Ripgrep (Experimental)
**What:** Optional performance optimization using ripgrep for file pattern matching

**How to use:**
Requires feature flag `tengu_glob_with_rg` to be enabled.

**Details:**
- Uses `rg --files --glob <pattern>` for matching
- Sorts results by modification time
- Includes hidden files
- Respects ignore patterns
- Performance benefit for large codebases
- **Evidence**: Feature flag check at line 483919 in pretty-v2.0.41.js (not in v2.0.37)

### Enhanced Multi-Agent Plan Mode
**What:** Structured 4-phase planning workflow with parallel agent coordination

**How it works:**
1. **Phase 1: Initial Understanding** - Read 3-4 relevant files, clarify ambiguities
2. **Phase 2: Multi-Agent Planning** - Launch 2 to N agents in parallel with different perspectives
3. **Phase 3: Synthesis** - Collect responses, ask trade-off questions
4. **Phase 4: Final Plan** - Present synthesized recommendation

**Details:**
- Quality over quantity: meaningful contrasts between agent perspectives
- Dynamic perspective generation (e.g., "simplicity vs performance vs maintainability")
- Parallel agent launches in single message (multiple tool calls)
- Context-aware perspective selection based on task type
- **Evidence**: Enhanced workflow at line 475195 in pretty-v2.0.41.js (basic version at line 473774 in v2.0.37)

### Network Path Security Enhancements
**What:** Expanded detection of suspicious Windows network paths

**Improvements over v2.0.37:**
- Added DavWWWRoot detection (WebDAV mounted drives)
- Added IP address-based UNC path detection (IPv4 and IPv6)
- Added forward slash variants for all patterns
- Added SSL port notation patterns (`@SSL@`, `@\d+@SSL`)

**Details:**
- Protects against WebDAV attacks
- Validates paths before execution
- Shows security warnings for suspicious paths
- **Evidence**: `ddA()` at line 222047 in pretty-v2.0.41.js (enhanced from `i2Q()` at line 222404 in v2.0.37)

### ANSI Escape Sequence Handling
**What:** Improved parsing of terminal color codes and escape sequences

**Details:**
- Proper handling of 256-color codes (`ESC[38;5;Nm`)
- Proper handling of RGB color codes (`ESC[38;2;R;G;Bm`)
- Fixes rendering bugs with complex color sequences
- More accurate terminal width calculations
- **Evidence**: `Km9()` at line 76407, `Em9()` at line 76423 in pretty-v2.0.41.js (different code at same lines in v2.0.37)

### Unicode Text Segmentation
**What:** Better handling of emoji and full-width characters in terminal output

**Details:**
- Uses `Intl.Segmenter` for proper grapheme cluster detection
- Detects full-width characters (CJK, emoji) for alignment
- Prevents terminal rendering issues with Unicode
- **Evidence**: `Nm9()` at line 76699, `$m9` initialization at line 76716 in pretty-v2.0.41.js (enhanced from v2.0.37)

### TodoList Tool Documentation
**What:** Comprehensive examples and guidance for todo list usage

**Improvements:**
- Added 4 detailed examples of when TO use (dark mode implementation, function renaming, e-commerce features, React optimization)
- Added 4 examples of when NOT to use (simple questions, informational requests, single edits, commands)
- Clarified `activeForm` requirement ("Fix bug" → "Fixing bug")
- Emphasized exactly ONE task must be in_progress at a time
- Added guidance not to mark tasks complete if tests fail

**Details:**
- Better user experience through clearer task status
- Prevents misuse for trivial tasks
- Ensures systematic progress tracking
- **Evidence**: Enhanced documentation in `Kv0` tool description at lines 1287-1469 in diff

### ExitPlanMode Tool Clarification
**What:** Clearer guidance on appropriate use of plan mode

**Details:**
- Only for tasks requiring code implementation planning
- NOT for research/understanding tasks  
- Must clarify ambiguities before exiting
- Added 3 specific examples distinguishing planning vs research
- **Evidence**: Enhanced guidance in `a12()` at lines 1902-1917 in diff

### LSP Diagnostic Improvements
**What:** Better handling of Language Server Protocol diagnostics

**Details:**
- Deduplication of diagnostics across multiple LSP servers
- More detailed logging for diagnostic delivery
- Better error messages for malformed LSP responses
- Reduces duplicate error reports in editor
- **Evidence**: Enhanced diagnostic handling at lines 1710-1734 in diff

### Error Message Improvements
**What:** More specific error types and clearer user feedback

**New error types:**
- `repeated_529` - Rate limit errors with specific guidance
- `prompt_too_long` - Oversized prompts with size information
- `pdf_too_large` - PDF page limit violations
- `oauth_org_not_allowed` - OAuth restriction details

**Details:**
- Better categorization of error conditions
- More actionable error messages
- Context-specific troubleshooting hints
- **Evidence**: New error types at lines 1499-1554 in diff

### Slash Command Documentation
**What:** Enhanced explanation of slash command behavior

**Details:**
- Clearer explanation that commands expand to prompts
- Shows `<command-message>` format example
- Warning not to invoke commands already running
- Better understanding of command execution model
- **Evidence**: Enhanced documentation at lines 96963-96982 in diff

### MCP Tool Token Tracking
Separate token usage tracking for MCP tools, distinguishing them from built-in tools in context window breakdown.
**Evidence**: Token tracking at lines 97073-97152 in diff

### Hook Summary Messages  
Consolidated plugin hook execution summaries showing hook count, errors, and prevention status with better formatting.
**Evidence**: `FaQ()`, `ij6()` at lines 3166-3181, 1625-1648 in diff

### Terminal Hyperlink Support
Added OSC 8 hyperlink support for creating clickable links in supported terminals using standard ANSI escape sequences.
**Evidence**: `X16()` at lines 1595-1606 in diff

### Truncation Indicators
Better warnings for truncated content, showing kilobytes removed for large tool results and warnings for git status truncation.
**Evidence**: Improvements at lines 1174, 2150-2151 in diff

### Thinking Mode Metadata
Enhanced thinking mode integration with better metadata passing and settings synchronization for `alwaysThinkingEnabled`.
**Evidence**: `dwQ()`, `pwQ()` at lines 61382-61438, 3485-3486 in diff


**Note:** This changelog covers changes from v2.0.37 to v2.0.41. All line numbers reference the prettified source files in the archive. Function names are from the minified/obfuscated source and may not reflect original implementation names.
