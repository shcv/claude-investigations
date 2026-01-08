# Changelog for version 1.0.111

## Highlights

This release focuses on improving robustness and user experience with enhanced shell command parsing, model validation, and visual feedback for long-running operations. Key improvements include safer shell parsing with error handling, API-based model validation to prevent invalid models, and visual indicators when operations are taking longer than expected.

### API-Based Model Validation
**What:** The `/model` command now validates custom model names by making a test API request before accepting them.

**How to use:**
```bash
# Try setting a custom model - it will be validated first
/model claude-opus-4-20250514

# If the model doesn't exist, you'll get an error immediately:
# "Model 'claude-opus-4-20250514' not found"
```

**Details:**
- Validation occurs automatically when setting custom models
- Built-in models (sonnet, haiku, opus) bypass validation for faster response
- Validated models are cached to avoid repeated API calls
- Provides specific error messages for model-not-found vs other API errors
- **Evidence**: `HDB()` at line 425289 in v1.0.111.js

### Shell Command Error Handling Improvements
**What:** Shell command parsing now uses error-safe wrapper functions that gracefully handle malformed commands instead of throwing exceptions.

**Details:**
- New `vC()` function at line 348215 wraps parse operations with try-catch
- New `q8()` function at line 348265 provides unified quoting with fallback strategies
- New `NX9()` function at line 348229 handles quote operations with error checking
- Commands with syntax errors now fail gracefully rather than crashing
- Improved handling of complex shell redirections and pipes
- **Evidence**: `vC()`, `NX9()`, and `q8()` functions at lines 348215, 348229, and 348265

### Stalled Operation Visual Indicator
**What:** The spinner now changes color from blue to orange when operations take longer than 3 seconds, providing visual feedback about potentially stuck processes.

**Details:**
- Spinner starts blue during normal operation
- After 3 seconds, gradually transitions to orange over the next 3 seconds
- Fully orange at 6+ seconds to indicate significantly delayed operation
- Smooth color interpolation provides clear visual feedback
- Only affects the spinner appearance, doesn't change functionality
- **Evidence**: `nE0()` at line 402439, color interpolation in `cE0()` at line 402326 and `lE0()` at line 402369

### Read File Caching for At-Mentions
**What:** Files mentioned with `@` are no longer re-read if they haven't been modified since the last read.

**Details:**
- Prevents redundant file reads when the same file is mentioned multiple times
- Checks file modification timestamps before reading
- Returns cached content if file is unchanged
- New `already_read_file` attachment type (not shown to user)
- Primarily benefits files that were written by Claude during the session
- **Evidence**: `PE0()` at line 398623 with timestamp checking at lines 398630-398649

### Environment Variable Whitelist
**What:** Settings files (`.claude/settings.json` and `.claude/settings.local.json`) can now only set specific whitelisted environment variables.

**Details:**
- 45 allowed environment variables including:
  - API configuration: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`
  - Feature flags: `DISABLE_TELEMETRY`, `DISABLE_ERROR_REPORTING`
  - Proxy settings: `HTTP_PROXY`, `HTTPS_PROXY`
  - Tool timeouts: `BASH_MAX_TIMEOUT_MS`, `MCP_TIMEOUT`
- Prevents arbitrary environment variable injection via settings files
- Security enhancement to protect against potential configuration exploits
- **Evidence**: `YCB` Set at lines 427822-427867, `WCB()` at line 427868

### Compact Error Message Clarity
The error message when conversations become too long now correctly instructs users to press escape twice instead of once:
- Old: "Press esc to go up a few messages and try again"
- New: "Press esc twice to go up a few messages and try again"
- **Evidence**: Variable `Ks6` at line 398957

### Memory Management During Compaction
Enhanced microcompact to clean up cached file data when compacting old tool results, preventing memory accumulation over long sessions.
- **Evidence**: `av()` function at line 399242 with cleanup logic at lines 399328-399344

### User Sentiment Tracking
Added detection for negative sentiment and "keep going" phrases in user prompts for better analytics and potential future UX improvements.
- **Evidence**: `usB()` at line 435565 and `msB()` at line 435571

### Terminal Resume Handling
Improved handling of terminal resume after Ctrl+Z by resetting line counts when receiving SIGCONT signal.
- **Evidence**: `handleResume()` in class `xU1` at line 362978

### Session Title Generation
Enhanced session title generation to skip slash commands and command output when extracting representative user prompts.
- **Evidence**: `h55()` at line 426021

### Model Display in Transcripts
Transcript mode now displays the model name used for each assistant response.
- **Evidence**: `WDB()` at line 424710

### Tool Permission Notification Improvements
Enhanced notification messages for tool permission requests to be more descriptive.
- **Evidence**: `_f5()` at line 431409

### TTY Detection Improvements
Fixed handling of non-TTY environments by checking `stdout.isTTY` instead of using a global flag, improving compatibility with piped output and CI environments.
- **Evidence**: Multiple locations including class `xU1` at line 361792

### Shell Working Directory Persistence
Added option to skip automatic working directory updates for certain shell operations to prevent unintended directory changes.
- **Evidence**: `uT6()` signature change at line 373626 with new parameter at line 373560

### Attachment Type Handling
Improved attachment normalization to handle background remote sessions and other new attachment types gracefully.
- **Evidence**: `rn6()` at line 396057 with new cases at lines 402372-402381

## Internal Changes

- Refactored shell parsing to use centralized wrapper functions for consistency
- Renamed and restructured ink rendering class from `A$1` to `xU1`
- Improved color application in text rendering with transform-based approach
- Enhanced border rendering to use theme-aware color functions
- Removed unused dependencies (onetime, signal-exit, stream imports)
- Cleaned up unused functions and variables (19 removed total)


**Note:** This changelog focuses on user-visible changes and significant improvements. Many internal refactorings and code reorganizations have been omitted for brevity.
