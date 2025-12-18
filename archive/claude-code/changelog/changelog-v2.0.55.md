# Changelog for version 2.0.55

## 🎯 Highlights

This release introduces enterprise policy controls for marketplace management, improved terminal compatibility with version-aware detection for Ghostty and iTerm, enhanced async agent monitoring with real-time progress tracking, and new telemetry for repository identification. Error handling is improved with specific detection for oversized images.

## 🚀 New Features

### Enterprise Marketplace Policy Controls
**What:** Organizations can now restrict which external marketplaces users can install via the `strictKnownMarketplaces` policy setting.

**How it works:**
- Administrators set allowed marketplace sources in enterprise policy settings
- When users attempt to install a marketplace, the source is validated against the allowlist
- Blocked sources show clear error messages indicating the policy restriction

**Details:**
- Supports multiple source types: GitHub repos, URLs, git repos, npm packages, file paths, and directories
- Clear error messaging: `"Marketplace source 'X' is blocked by enterprise policy. Allowed sources: ..."`
- **Evidence:** `pEA()` at line ~164954, `apA()` at line ~164985, `So()` at line ~165393 in v2.0.55

### Configurable Sandbox Search Depth
**What:** New `mandatoryDenySearchDepth` setting controls how deep the sandbox scans for dangerous files and directories.

**Details:**
- Default value: 3 levels deep
- Configurable via policy settings
- Improves performance in large repositories by limiting recursive scanning
- **Evidence:** `Ye8()` at line ~188483, with default value of 3

### Repository Hash Telemetry
**What:** Claude Code now generates an anonymized hash identifier for repositories to improve telemetry without exposing actual repository URLs.

**How it works:**
- Parses git remote URLs (supports both SSH and HTTPS formats)
- Normalizes the URL to `host/path` format
- Generates a SHA-256 hash and uses the first 16 characters
- Included in telemetry events as `rh` property

**Details:**
- Supports formats like `git@github.com:org/repo.git` and `https://github.com/org/repo`
- **Evidence:** `pA6()` at line ~192113, `V7B()` at line ~192122

### Prompt Suggestion System (Experimental)
**What:** A new system that predicts and suggests the user's next prompt based on conversation context.

**Details:**
- Generates 3-8 word suggestions for natural follow-ups (e.g., "run the tests", "now fix the linting errors")
- Only triggers for main REPL thread queries
- Includes telemetry for suggestion display and acceptance tracking
- **Evidence:** Functions at lines ~409868-409929, telemetry event `tengu_prompt_suggestion_shown`

### Image Too Large Error Handling
**What:** Specific error detection and messaging when uploaded images exceed API size limits.

**Details:**
- Detects API 400 errors containing "image exceeds" and "maximum"
- Returns dedicated `image_too_large` error type
- User-friendly message: "Image was too large. Double press esc to go back and try again with a smaller image."
- **Evidence:** Error detection at line ~345176, message constant `FF5` at line ~345069

## 🔧 Improvements

### Enhanced Terminal Version Detection
**What:** Improved compatibility checking for Ghostty and iTerm terminals using semantic versioning.

**Before:** Simple environment variable check (`TERM === "xterm-ghostty"`)

**After:** 
- Uses proper semver comparison via `TERM_PROGRAM` and `TERM_PROGRAM_VERSION`
- Ghostty: requires version >= 1.2.0
- iTerm.app: requires version >= 3.6.6

**Details:**
- **Evidence:** New function `e46()` at line ~222505 with semver checking via `mUA.gte()`

### Enhanced Async Agent Details Panel
**What:** The async agent monitoring panel now shows significantly more information about running agents.

**New features:**
- Real-time task progress tracking with completion counters
- Token usage display (total tokens consumed)
- Tool use count tracking
- Recent activity feed showing current agent operations
- Increased prompt preview from 200 to 300 characters

**Details:**
- Integrates with todo state for task tracking
- Shows "Tasks (X/Y)" with completion progress
- Displays token and tool counts in status line
- **Evidence:** `O29()` at line ~468985 replaces older `PQ9()` function

### Enhanced sed Command Validation
**What:** The `sed` command validator now supports explicit file write permission control.

**How it works:**
- New `allowFileWrites` parameter controls whether in-place editing is permitted
- When in "acceptEdits" mode, `-i` and `--in-place` flags are allowed
- Otherwise, sed write operations require explicit approval

**Details:**
- Function signature changed to accept options object with `allowFileWrites`
- **Evidence:** `h92()` at line ~314399 with parameter `G?.allowFileWrites`

### Improved Pipe Command Parsing
**What:** Pipe segmentation for bash commands now uses tree-sitter parsing for more accurate command analysis.

**Details:**
- Uses `getPipeSegments()` method for reliable pipe detection
- Better handles complex shell syntax
- Falls back to basic parsing if tree-sitter unavailable
- **Evidence:** `R92()` at line ~313655 with `u01.parse()` integration

## 📊 Telemetry Changes

### New Telemetry Fields
- `repository_id` and `repository_owner_id` for GitHub Actions metadata
- `wsl_version` for Windows Subsystem for Linux environments
- `is_claubbit` flag for internal tooling detection
- `swe_bench_run_id`, `swe_bench_instance_id`, `swe_bench_task_id` for benchmark tracking
- `queryChainId` and `queryDepth` for fork agent query tracking
- Cache hit rate metrics for forked agent queries

### New Telemetry Events
- `tengu_fork_agent_query`: Tracks forked agent query performance and token usage
- `tengu_prompt_suggestion_shown`: When prompt suggestions are displayed
- `tengu_prompt_suggestion_accepted`: When users accept suggested prompts

## 🐛 Bug Fixes

### Bash Permission Check Reordering
**What:** Fixed the order of permission checks for bash commands to ensure dangerous file checks happen before subcommand evaluation.

**Details:**
- Dangerous file check (`ct1`) now runs after subcommand parsing
- Returns early if dangerous patterns detected, before proceeding to subcommand analysis
- **Evidence:** Function `et1()` at line ~314794 with reordered checks

### Session Memory Agent Removal
**What:** Removed the standalone `session-memory` agent type that was unused.

**Details:**
- Function `SS3()` removed from v2.0.54
- Memory extraction handled through other mechanisms
