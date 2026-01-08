# Changelog for version 2.0.11

## Highlights

Version 2.0.11 introduces support for structured outputs (a new Claude API feature in beta), adds a new Explore agent for faster codebase navigation, and includes various internal improvements and bug fixes.

### Structured Outputs Support (Beta)

**What:** Support for Claude's new structured outputs API feature via the beta header `structured-outputs-2025-09-17`

**Details:**
- Tools can now opt-in to strict schema validation by setting `strict: true`
- When using a model with structured outputs support and tools marked as strict, Claude will enforce exact adherence to the tool's input schema
- Core tools (Bash, Read, Edit, Write) have been updated with `strict: true` for improved reliability
- Automatically detected via model name containing `-structured-`
- **Evidence**: New constant `Ey2 = "structured-outputs-2025-09-17"` at line 376349 and detection function `OV0()` at line 376356 in v2.0.11

### Explore Agent

**What:** New built-in agent specialized for fast codebase exploration and file searching

**When to use:**
```bash
# Automatically invoked when searching for files or exploring code
# Fast operations: finding files by patterns, searching code for keywords,
# answering questions about codebase structure
```

**Details:**
- Optimized for rapid file pattern matching with Glob
- Powerful regex-based code searching with Grep  
- Efficient file reading and bash operations
- Uses the fast Haiku model for quick responses
- Tools available: Glob, Grep, Read, Bash
- **Evidence**: New agent definition `Ds5` at line 428791 in v2.0.11 with `agentType: "Explore"`

### Enhanced Marketplace Operations

**What:** Marketplace git operations now provide progress feedback during cloning and pulling

**Details:**
- Progress callbacks report status during `git clone` and `git pull` operations
- Better error messages with specific guidance for common failures (connection issues, timeouts, HTTP errors)
- Improved cleanup and error recovery when marketplace operations fail
- More robust handling of corrupted marketplace cache directories
- **Evidence**: Functions `ky2()` and `yr4()` at lines 377040 and 377088 in v2.0.11 now accept progress callback parameter `Q`

### File Timestamp Checking

**What:** More efficient file modification time checking

**Details:**
- Introduced dedicated `BK()` function for consistent timestamp retrieval
- Replaces inline `Math.floor(statSync().mtimeMs)` patterns throughout codebase
- **Evidence**: New function `BK()` at line 441199 in v2.0.11

## Internal Changes

- Removed legacy teleport session validation functions (replaced by Sessions API implementation)
- Simplified agent color assignment logic
- Removed deprecated usage limit message handling code
- Removed unused dynamic config fetching function
- Streamlined sandbox initialization (removed `--sandboxed-bash` flag logic in favor of settings-based configuration)
- Refactored permission helper functions for better organization
- Removed legacy git default branch detection code
- Improved error formatting for marketplace/plugin operations with structured error types
