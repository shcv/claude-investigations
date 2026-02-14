# Changelog for version 1.0.91

## Highlights
Version 1.0.91 is a targeted refinement release focused on security enhancements, developer experience improvements, and user interface polish. Key additions include command obfuscation detection, native grep/ripgrep support, GitHub Actions integration templates, and enhanced CLI animations.


### Native grep and ripgrep Support
**What:** Added native support for `grep` and `rg` (ripgrep) commands within Claude's secure sandbox
**How to use:**
```bash
# Search for patterns in files
grep "TODO" src/*.js
rg "function.*async" --type js
```
**Details:**
- Both commands are treated as read-only operations
- Added to command descriptors and safe commands list
- Integrates with existing path restriction framework
- Eliminates need for shell execution for basic search operations


### Command Obfuscation Detection
**What:** New security feature that detects attempts to hide malicious command flags using quotes
**Implementation:** New `ML6` function at `archive/pretty/pretty-v1.0.91.js:374835`
**How it works:**
```bash
# These patterns will now trigger security prompts:
rm "-rf" /     # Quoted flag detected
ls "-"la       # Obfuscated flag pattern detected
```
**Details:**
- Analyzes command arguments for suspicious quoting patterns
- Prevents sophisticated command injection attempts
- Echo command exempted from checks as inherently safe
- Part of the enhanced command validation pipeline


### GitHub Actions Workflow Templates  
**What:** Pre-configured workflow templates for Claude Code CI/CD integration
**Implementation:** Two new templates added:
- `e_B` template for claude.yml workflow
- `AxB` template for claude-review.yml workflow
**Details:**
- Responds to @claude mentions in issues and PR comments
- Uses production `anthropics/claude-code-action@v1` (upgraded from beta)
- Includes proper permissions and trigger configurations
- Supports both manual triggers and automatic code review


### Enhanced CLI Animations
**What:** New shimmer and color interpolation animations for improved visual feedback
**Implementation:** New animation functions `yN0`, `xN0`, `bN0`, `fN0` at `archive/pretty/pretty-v1.0.91.js:398709-398954`
**Details:**
- RGB color interpolation for smooth transitions
- Character-by-character glimmer effects  
- Sine-wave opacity for natural pulsing animations
- Enhanced visual feedback during tool operations


### TodoWrite activeForm UI Display
**What:** Status spinner now displays the `activeForm` field from in-progress todos
**Implementation:** Removed feature flag `MQ("false")` at `archive/pretty/pretty-v1.0.91.js:398916-398919`
**How it works:**
- When a todo is marked as "in_progress", the spinner shows the `activeForm` text + "…"
- Example: "Fixing authentication bug…" instead of generic loading text
- Provides contextual progress feedback using present continuous tense
**Details:**
- Feature was implemented behind a disabled flag in v1.0.90
- Flag removal in v1.0.91 made the display unconditional
- Completes the TodoWrite enhancement that began with schema changes in v1.0.89


### Node.js Warning Monitoring
**What:** Automatic detection and reporting of Node.js runtime warnings
**Implementation:** New `UN2` function and warning patterns at `archive/pretty/pretty-v1.0.91.js:356268`
**Details:**
- Specifically monitors MaxListenersExceededWarning events
- Distinguishes between internal vs external warnings
- Tracks occurrence counts for telemetry
- Optional debug logging with `CLAUDE_DEBUG=true`


### OAuth Server Reliability
**What:** Enhanced OAuth callback server with dynamic port allocation
**Details:**
- Server class restructured from `zL0` to `rL0`
- Now starts on port 0 for OS-assigned available ports
- Prevents port conflicts during authentication flows
- Improved error handling and cleanup with `removeAllListeners()`


### OAuth Error Handling
**What:** Structured OAuth error classes and better error recovery
**Details:**
- New error classes: `cI`, `ak1`, `Ve`, `Ke` for different OAuth failure modes
- Enhanced metadata discovery with fallback mechanisms
- Better handling of various OAuth server implementations
- More robust token exchange processes


### Command Argument Processing
**What:** Fixed null pointer exception in command argument filtering
**Details:**
- Changed filter condition from `!B.startsWith("-")` to `!B?.startsWith("-")`
- Prevents crashes when processing commands with null/undefined arguments
- Improves robustness of command parsing pipeline


### Features NOT New in 1.0.91
The following were already present in v1.0.90 and are not new features:
- **Statsig Analytics Integration**: Full analytics infrastructure was already implemented
- **OAuth Authentication Core**: Basic OAuth functionality existed, only reliability improvements added
- **Command Security Framework**: Core security mechanisms were in place, only obfuscation detection added

## Technical Notes
- File structure similarity: 99.1% between versions
- Total changes: 74 additions, 16 deletions, 17 modifications  
- Primary focus on security, reliability, and user experience refinements
