# Changelog for version 1.0.74

## Highlights
Claude Code 1.0.74 introduces Sonnet 4 with 1M token context for eligible organizations, a powerful new custom output modes system that lets you personalize how Claude communicates, and improved bash command handling with enhanced security controls.

### Sonnet 4 with 1M Token Context
**What:** Access to Claude Sonnet 4 with an extended 1 million token context window for processing large codebases and documents
**How to use:**
```bash
# Select from the model menu
claude /model
# Choose "Sonnet (1M context)" option

# Or set directly
claude /model sonnet[1m]
```
**Details:**
- Available to eligible organizations only (checked automatically)
- Higher token costs: $6/$22.50 per million tokens (vs $3/$15 for regular Sonnet)
- Automatically selected as default for users with Opus mode and 1M access
- One-time welcome notification explains the feature and rate limit implications
- Access status cached for 1 hour to minimize API calls

### Custom Output Modes
**What:** Create personalized output modes that modify how Claude Code communicates with you
**How to use:**
```bash
# Create a new custom output mode
claude /output-mode:new

# Select from available modes
claude /output-mode

# Set a mode directly
claude /output-mode Concise
```
**Details:**
- Output modes are markdown files with YAML frontmatter stored in `~/.claude/output-modes/` or `.claude/output-modes/`
- Built-in modes "Insights" and "Learn By Doing" can be overridden with custom versions
- New `output-mode-setup` agent guides you through creating modes with natural language
- Modes can customize response length, tone, format, and workflow preferences
- Project-level modes allow teams to share communication styles

### Opus Plan Mode
**What:** New hybrid model option that uses Opus 4.1 in plan mode and Sonnet 4 for execution
**How to use:**
```bash
claude /model
# Select "Opus Plan Mode" option
```
**Details:**
- Description: "Use Opus 4.1 in plan mode, Sonnet 4 otherwise"
- Provides optimal model selection based on the current operation mode
- Automatically switches between models for planning vs implementation

### Enhanced Bash Command Generation
**What changed:** Improved handling of bash redirections and file descriptors
**Impact:** More reliable command execution with complex shell redirections like `2>&1`, `1>/dev/null`, and file descriptor routing

### Granular Permission System
**What changed:** Separated trust dialogs into three distinct categories
**Impact:** Users can now approve bash commands, hooks, and general operations independently, providing finer control over security permissions

### UI Polish with Shimmer Effects
**What changed:** Added shimmer colors to all themes for Claude-related UI elements
**Impact:** Subtle visual feedback improvements with colors like `rgb(245,149,117)` for light theme and `rgb(235,159,127)` for dark theme

### Command Source Tracking
**What changed:** All built-in commands now include a `source: "builtin"` field
**Impact:** Better organization and potential for future command source filtering or custom command sources

### Organization Feature Tracking
**What changed:** Added first token date tracking and per-organization feature flag caching
**Impact:** Better analytics and feature rollout capabilities for organization-specific features

### Fixed: Process Import Issue
- **Issue:** Incorrect import statement for process.cwd
- **Cause:** Using default import instead of named import
- **Resolution:** Changed from `import ndB from "node:process"` to `import { cwd as RM2 } from "node:process"`

### Fixed: Output Mode Key Consistency
- **Issue:** Inconsistent naming between internal keys and display names
- **Cause:** Built-in modes used kebab-case internally but title case for display
- **Resolution:** Standardized on title case for both internal keys and display ("Insights", "Learn By Doing")

### Fixed: Statsig Gate Caching
- **Issue:** Feature gates were being fetched repeatedly without caching
- **Cause:** Missing cache implementation for Statsig gates
- **Resolution:** Added `cachedStatsigGates` to configuration with proper cache management
