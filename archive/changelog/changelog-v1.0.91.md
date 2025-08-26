# Changelog for version 1.0.91

Now I'll create the comprehensive changelog for version 1.0.91 based on all the verified changes.

# Changelog for version 1.0.91

## 🎯 Highlights
Version 1.0.91 enhances command-line security with obfuscation detection, adds native grep/ripgrep support, and introduces GitHub Actions workflow templates. The update also improves OAuth compatibility, adds sophisticated CLI animations, and integrates analytics capabilities.

## 🚀 New Features

### Native grep and ripgrep Support
**What:** Added full support for `grep` and `rg` (ripgrep) commands within Claude's secure sandbox
**How to use:**
```bash
# Search for patterns in files
grep "TODO" src/*.js
rg "function.*async" --type js

# These commands now work with path restrictions and permission checks
```
**Details:**
- Both commands are treated as read-only operations
- Custom path extraction handles complex argument structures
- Works within the existing security framework
- Supports common flags like `-e`, `--regexp`, `-f`, `--file` for grep
- Supports ripgrep-specific flags like `-g`, `--glob`, `-t`, `--type`

### Command Obfuscation Detection
**What:** New security feature that detects attempts to hide malicious flags using quotes
**How it works:**
```bash
# This will now trigger a security prompt:
rm "-rf" /  # Quoted flag detected
ls "-"la    # Obfuscated flag pattern detected
```
**Details:**
- Detects quoted characters within flag names
- Identifies patterns where quotes are used to bypass security
- Prompts user for confirmation when suspicious patterns are found
- Echo command is exempted as safe

### GitHub Actions Workflow Templates
**What:** Pre-configured GitHub Actions workflows for Claude Code integration
**How to use:**
```bash
# Templates are now available for automatic setup
# Two workflows included:
# 1. Claude Code - responds to @claude mentions
# 2. Claude Code Review - automatic PR reviews
```
**Details:**
- Triggers on issue comments, PR comments, and PR reviews containing "@claude"
- Includes proper permissions configuration
- Uses `anthropics/claude-code-action@v1`
- Supports both manual triggers and automatic code review

### Enhanced CLI Animations
**What:** Sophisticated visual feedback with color interpolation and pulsing effects
**Details:**
- **Tool-use mode**: Text now pulses with smooth color transitions instead of static symbol
- **RGB color interpolation**: Smooth transitions between colors for flash effects
- **Glimmer animations**: Enhanced character-by-character shimmer effects
- **Sine-wave opacity**: Creates natural breathing/pulsing animation
- Separate animation modes for different operation types

### Node.js Warning Monitoring
**What:** Automatic tracking and reporting of Node.js runtime warnings
**Details:**
- Captures MaxListenersExceededWarning events
- Distinguishes internal vs external warnings
- Tracks warning occurrence counts
- Sends telemetry for monitoring
- Optional debug mode logging with `CLAUDE_DEBUG=true`

### Analytics Integration
**What:** Statsig integration for feature flags and experimentation
**Details:**
- Connects to Anthropic's Statsig endpoint
- Enables A/B testing and feature rollouts
- Configured for production environment
- Custom user cache key generation

## 🔧 Improvements

### OAuth Authentication Enhancements
**What:** Improved compatibility with various OAuth server implementations
**Details:**
- **Dynamic authentication method selection**: Automatically chooses between `client_secret_basic`, `client_secret_post`, or `none` based on server capabilities
- **Better metadata discovery**: Refactored well-known endpoint discovery with fallback mechanisms
- **Enhanced error handling**: Structured OAuth error responses with proper error codes
- **Improved token exchange**: Proper Accept headers and custom authentication support
- **Comprehensive validation**: New Zod schemas for OAuth/OpenID provider metadata

### Local OAuth Server Improvements
**What:** Better port allocation for OAuth callback server
**Details:**
- Dynamic port allocation instead of fixed port
- Starts on port 0 to let OS assign available port
- Better error handling during server startup
- Cleaner shutdown with removeAllListeners()

## 🐛 Bug Fixes

### Command Argument Processing
**What:** Fixed null handling in command argument filtering
**Details:**
- Changed filter condition from `!B.startsWith("-")` to `!B?.startsWith("-")`
- Prevents crashes when processing commands with null arguments

### Import Organization
**What:** Cleaned up duplicate imports and reorganized crypto/stream imports
**Details:**
- Consolidated crypto imports using destructuring
- Removed redundant import statements
- Better code organization

## 📝 Other Changes

### Permission System Updates
**What:** Added grep and ripgrep to permission maps
**Details:**
- Both commands classified as "read" operations
- Added to path restriction framework
- Included in safe command lists for specific modes

### Telemetry Enhancements
**What:** New telemetry events for monitoring
**Details:**
- `tengu_node_warning` event for runtime warnings
- Warning occurrence tracking
- Internal vs external warning classification
