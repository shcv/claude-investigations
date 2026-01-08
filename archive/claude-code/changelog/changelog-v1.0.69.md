# Changelog for version 1.0.69

Based on my comprehensive analysis of the diff file, here is the detailed changelog for Claude Code v1.0.69:

# Claude Code v1.0.69 Changelog

### 1. **Security Review Command** (New)
A powerful new `/security-review` command that performs automated security analysis of code changes:

**Usage:**
```bash
/security-review
```

**What it does:**
- Analyzes all pending changes on the current branch
- Performs comprehensive security-focused code review
- Identifies potential vulnerabilities including:
  - SQL/Command injection
  - Authentication & authorization flaws
  - Cross-site scripting (XSS)
  - Cryptographic weaknesses
  - Sensitive data exposure
  - Insecure deserialization

**Output:**
Generates a detailed markdown report with severity levels (HIGH/MEDIUM/LOW), file locations, exploit scenarios, and specific fix recommendations.

### 2. **Enhanced Background Task Management**
Improved handling of long-running processes with background execution:

**New BashOutput Tool:**
```bash
# Check output from background shells
BashOutput bash_1

# Filter output with regex patterns
BashOutput bash_1 "error|warning"

# List all background shells
/bashes
```

**Features:**
- Automatic notifications when background tasks complete
- Shows only new output since last check
- Regex filtering support for monitoring specific patterns
- Exit code tracking and completion status

### 3. **Claude Opus 4.1 Model Support**
Added support for the new Claude Opus 4.1 model:
- Model identifier: `claude-opus-4-1-20250805`
- Available across first-party, Bedrock, and Vertex AI platforms
- Enhanced region support with `VERTEX_REGION_CLAUDE_4_1_OPUS` environment variable

### **Autocheckpointing Enhancements**
- Better checkpoint management with improved state handling
- Async initialization for better performance
- Enhanced error recovery and status tracking
- Support for automatic checkpointing on prompts and bash commands

### **File Search Improvements**
- New `ZnB` function provides better file search with glob pattern support
- Improved handling of special characters in search patterns
- Better performance for file discovery operations

### **Shell Execution Enhancements**
- Better cleanup of background processes on exit
- Improved tracking of completed shells for attachment messages
- Enhanced shell output management with proper cleanup

### **Tool Permission Handling**
- Better handling of closed permission streams
- Improved error messages when permission stream is closed
- More robust pending request management

## Bug Fixes

- Fixed issue where input stream closure could leave pending permission requests hanging
- Improved cleanup of background shells on process termination
- Better handling of shell completion status notifications
- Fixed race conditions in background task management

### **New Functions Added:**
- `fnB` - Generate timestamped file names for prompts
- `CP1` - Smart string truncation with ellipsis support
- `iC8` - Enhanced attachment processing with background task status
- `Iz8` - Background task status collection
- `jkB` - Dynamic token limit calculation
- `jyB` - Command category detection for analytics
- `nE8` - Check if command is safe to run in background
- Various checkpoint management functions (`QiB`, `ZiB`, `AiB`, `DiB`)

### **Removed Functions:**
- Removed legacy checkpointing class `_A1` in favor of new async implementation
- Removed `BashOutput` tool implementation `ylB` (replaced with enhanced version)
- Removed various obsolete utility functions

### **Modified Functions:**
- Enhanced `hS0` class (previously `PS0`) with better stream closure handling
- Updated model selection logic to support Opus 4.1
- Improved shell management class `U01` with cleanup on exit

### Security Review:
```bash
# After making changes to your code
/security-review
# Claude analyzes changes and provides detailed security report
```

### Background Tasks:
```bash
# Start a long-running process
Bash npm run build

# Check background tasks
/bashes
# Output: bash_1 (running): npm run build

# Monitor output
BashOutput bash_1

# Filter for errors
BashOutput bash_1 "error|failed"
```

### Model Selection:
```bash
# Use the new Opus 4.1 model
claude --model claude-opus-4-1-20250805

# Or set via environment
export ANTHROPIC_MODEL=claude-opus-4-1-20250805
```

## Performance Improvements

- Async checkpoint initialization reduces startup time
- Better resource cleanup prevents memory leaks
- Improved background task management reduces CPU usage
- More efficient file search with optimized glob patterns

## Security Enhancements

- New security review tool helps identify vulnerabilities early
- Better handling of untrusted input in shell commands
- Improved permission management for tool execution
- Enhanced cleanup of sensitive data in background processes


This release focuses on security, background task management, and overall stability improvements, making Claude Code more powerful for real-world development workflows.
