# Changelog for version 1.0.112

## 🎯 Highlights
Version 1.0.112 introduces skill.md file support for organizing commands hierarchically, adds enhanced network sandboxing with allow-lists, and removes unused internal network sandboxing code. Several improvements enhance command parsing, error tracking, and user configuration options.

## 🚀 New Features

### skill.md File Support
**What:** Organize multiple commands in a directory under a single skill.md file
**How to use:**
```bash
# Create a directory with related commands
mkdir my-commands/
echo "# My Skill" > my-commands/skill.md
echo "command content" > my-commands/command1.md

# Claude Code will now treat all .md files in this directory as part of the skill
```
**Details:**
- When multiple command files exist in a directory with a skill.md file, Claude Code prioritizes the skill.md
- Case-insensitive matching (skill.md, Skill.md, SKILL.MD all work)
- Helps organize complex command structures hierarchically
- **Evidence:** `uM0()` at line 424817 and `pZ5()` at line 424820 in v1.0.112

### Enhanced Network Sandboxing with Allow-Lists
**What:** Fine-grained network access control for sandboxed bash commands
**How to use:**
```bash
# Network sandboxing now supports allow-lists for specific hosts
# Configured through internal settings: sandbox.network.allow
```
**Details:**
- NetworkManager filters connections based on configured allow-list
- Blocks all network access except explicitly allowed hosts
- Logs allowed and blocked connections for transparency
- Works with HTTP proxy for controlled network access
- **Evidence:** `NetworkManager` implementation at line 373982-374129 in v1.0.112

### Automatic Feature Flag Updates
**What:** Statsig feature flags now refresh automatically every 6 hours
**Details:**
- Keeps feature flags up-to-date without restarting the CLI
- Runs in background, transparent to users
- Automatically disabled when using Bedrock/Vertex or when telemetry is disabled
- **Evidence:** `xqB()` at line 428347 in v1.0.112

## ✨ Improvements

### Configurable Spinner Tips
**What changed:** Added ability to disable spinner tips through configuration
**How it works now:**
```bash
# Configure in settings to disable tips during long operations
# Set spinnerTipsEnabled: false in configuration
```
**Evidence:** `NrB()` at line 437820

### Enhanced Command Parsing and Validation
**What changed:** Better error handling and validation before command execution
**Benefits:**
- Clearer error message: "Command cannot be parsed" for malformed commands
- Improved detection of input redirection patterns (e.g., `< file.txt`)
- More robust tokenization of complex commands with special characters
- **Evidence:** `lAB()` at line 384563, `qz0()` at line 373516, `ut2()` at line 373524

### Better Error Tracking
**What changed:** Error reports now include unique error IDs
**Benefits:**
- Easier to track and debug specific errors when reporting issues
- Better correlation between user reports and backend logs
- **Evidence:** `Rh1()` at line 428069 and `U1()` at line 428104

### Improved Native Installation Detection
**What changed:** Prevents auto-migration prompts for users already on native installations
**Benefits:**
- No more unnecessary migration notifications
- Cleaner user experience for native install users
- **Evidence:** `Lm1()` at line 435204

### Streamlined Terminal Output
**What changed:** More consistent terminal output rendering
**Benefits:**
- Fewer visual glitches in terminal display
- Better structured output handling
- **Evidence:** `IC9` variable at line 361107

## 🗑️ Removed

### Internal Network Sandboxing (macOS sandbox-exec)
**What was removed:** Unused internal network sandboxing implementation
**Details:**
- Removed `ST6()` (sandbox-exec profile generator) at line 373486 in v1.0.111
- Removed `ct2()` (macOS command wrapper) at line 373499 in v1.0.111
- Removed `at2()` (platform-agnostic sandbox orchestrator) at line 373547 in v1.0.111
- This was internal-only functionality not exposed to users
- Replaced by the enhanced NetworkManager implementation
