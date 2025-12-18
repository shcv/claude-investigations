# Changelog for version 2.0.70

## 🎯 Highlights

This release introduces a new feature discovery system to help users explore Claude Code's capabilities, adds the MCPSearch tool for better MCP tool management, and improves the teleport experience with a visual progress indicator.

## 🚀 New Features

### Feature Discovery System (`/discover`)
**What:** A new interactive feature discovery interface that helps users explore and track their usage of Claude Code's capabilities across organized categories.

**How to use:**
```bash
# Open the feature discovery interface
/discover
```

**Details:**
- Organizes features into 6 categories: Quick Wins, Speed, Code, Collaborate, Customize, and Power User
- Tracks which features you've explored with progress indicators
- Shows completion percentage and visual progress bar
- Each feature includes a "Try it" prompt for hands-on learning
- Navigate with arrow keys, Enter to explore, Esc to close
- **Evidence**: Feature categories defined at lines 168232-168267 in `pretty-v2.0.70.js`; `/discover` command at `PpZ` variable around line 463990

### MCPSearch Tool
**What:** A new tool that allows Claude to search and load MCP (Model Context Protocol) tools before using them, improving reliability of MCP integrations.

**How to use:**
MCP tools are now deferred and must be loaded via MCPSearch before use. Claude will automatically use this tool when you request MCP functionality.

**Details:**
- Supports two query modes: direct selection (`select:mcp__slack__read_channel`) or keyword search
- Returns up to 5 matching tools ranked by relevance
- Caches tool descriptions for faster subsequent searches
- Returns `tool_reference` content blocks that make selected tools available
- **Evidence**: `MCPSearchTool` implementation at `Ey2` variable, line 454185; tool name `Gy2 = "MCPSearch"` at line 454099

### Teleport Progress Display
**What:** Visual progress indicator when teleporting into a remote session, showing each step of the process.

**How to use:**
When teleporting to a session, you'll now see a multi-step progress display:
```
◐ Teleporting session…
  ✓ Validating session
  ◐ Fetching session logs
  ○ Getting branch info
  ○ Checking out branch
```

**Details:**
- Shows animated spinner for current step
- Displays checkmarks for completed steps
- Four stages: validating, fetching_logs, fetching_branch, checking_out
- **Evidence**: `di2` steps array at line 503776; `SU5` progress component at line 503695

### Feature Usage Tracking
**What:** Internal tracking of which features you've used to power the discovery system's progress indicators.

**Details:**
- Tracks feature usage in local config
- Powers the "explored X of Y features" progress display
- Per-category completion tracking
- **Evidence**: `featureUsage` state property referenced at lines 168212, 168631, 168637

### Coaching Mode Setting
**What:** New setting for controlling in-session coaching tips and guidance.

**Details:**
- Configurable coaching tip behavior
- Tracks coaching tips shown per session via `coachingTipsThisSession`
- Controlled via `coachingMode` setting (can be set to "off")
- **Evidence**: `coachingMode` getter at line 368908; `coachingTipsThisSession` at line 368906

## Other Changes

### Enhanced Marketplace Auto-Installation
The official Anthropic marketplace auto-installation now includes improved retry logic with exponential backoff:
- Tracks retry count, last attempt time, and next retry time
- Maximum 10 retry attempts with delays from 1 hour to 7 days
- Shows user notifications for installation status (success, failure, git unavailable)
- **Evidence**: Retry constants at `o51` variable, line 445893 (`MAX_ATTEMPTS: 10`, `INITIAL_DELAY_MS: 3600000`, `MAX_DELAY_MS: 604800000`)

### Dynamic MCP Server Configuration
New support for dynamically adding and removing MCP servers at runtime:
- `RU5()` function handles hot-reloading of MCP configurations
- Properly cleans up removed servers and initializes new ones
- Returns detailed results including which servers were added, removed, and any errors
- **Evidence**: `RU5()` function at line 502788

### Improved Tool Prompt Coaching
New prompt coaching system that can display contextual tips during tool use:
- Tracks tips shown per session
- Integrates with the coaching mode setting
- **Evidence**: `promptCoaching` state with `tip` and `shownAt` at line 487684

### Security Review Command Enhancements
The `/security-review` command now includes expanded false positive filtering guidelines:
- Added exclusions for React/Angular XSS (frameworks handle escaping)
- Added exclusions for client-side permission checking (backend handles this)
- Added exclusions for notebook vulnerabilities without concrete attack paths
- **Evidence**: Enhanced filtering rules in `ZV5` template starting at line 471235
