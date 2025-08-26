# Changelog for version 1.0.85

Now I'll create the final, accurate changelog based on all my investigations:

# Changelog for version 1.0.85

## 🎯 Highlights
Version 1.0.85 introduces comprehensive rate limit messaging with clear feedback about usage limits and spending caps, automatic session memory that maintains persistent notes about your work, and improved environment variable validation with helpful warnings when values are misconfigured.

## 🚀 New Features

### Rate Limit Status Messaging
**What:** Complete system for communicating rate limits, usage limits, and spending caps with clear, actionable messages
**How to use:**
```bash
# You'll automatically see messages when approaching or hitting limits:
# "Approaching spending cap"
# "5-hour limit reached • resets in 2h 15m"
# "Weekly limit reached • resets Monday 9am"
# "Opus weekly limit reached • resets in 3 days"
```
**Details:**
- Different messages for 5-hour, weekly, and Opus-specific limits
- Human-readable reset times showing when limits clear
- Warnings when approaching limits before hitting them
- Special handling for team/enterprise accounts with admin contact guidance
- Spending cap and overage status tracking

### Session Memory (Automatic Notes)
**What:** Automatic background system that maintains structured notes about your ongoing development work
**How to use:**
```bash
# Automatically activates after 5 messages in a session
# Notes are saved to ~/.claude/session-memory/[session-id].md
# Customize with your own templates:
mkdir -p ~/.claude/session-memory
echo "Your template" > ~/.claude/session-memory/template.md
echo "Your prompt" > ~/.claude/session-memory/prompt.md
```
**Details:**
- Captures task specifications, worklog, code documentation, and learnings
- Updates transparently in the background without interrupting your work
- Persists context across conversations for better continuity
- Customizable template and update prompts for project-specific needs

### Environment Variable Validation Framework
**What:** Structured validation system for environment variables with detailed feedback
**How to use:**
```bash
# Set environment variables with automatic validation:
export BASH_MAX_OUTPUT_LENGTH=40000  # Validates and caps if needed
export CLAUDE_CODE_MAX_OUTPUT_TOKENS=16000  # Validates with warnings

# Invalid values show warnings but don't crash:
export BASH_MAX_OUTPUT_LENGTH=invalid  # Warning: Invalid value "invalid" (using default: 30000)
export BASH_MAX_OUTPUT_LENGTH=100000   # Warning: Capped from 100000 to 50000
```
**Details:**
- BASH_MAX_OUTPUT_LENGTH: Default 30000, max 50000 characters
- CLAUDE_CODE_MAX_OUTPUT_TOKENS: Default 32000, max 32000 tokens
- Non-fatal warnings for invalid or capped values
- Clear feedback about what values are actually being used

### SessionEnd Hook Event
**What:** New hook event that fires when Claude Code shuts down, enabling cleanup actions
**How to use:**
```bash
# Configure in your hooks file to run cleanup on exit:
# Hook will receive: {hook_event_name: "SessionEnd", reason: "logout" | "other"}
```
**Details:**
- Triggers before Claude Code exits
- Provides shutdown reason (logout vs other termination)
- Allows external programs to perform cleanup
- 2-second timeout ensures quick shutdown

## 💪 Improvements

### Enhanced Heredoc Security Validation
**What changed:** More robust validation for heredoc patterns in bash command substitutions
**Previous behavior:** Simple pattern matching could miss complex quoting scenarios
**New behavior:** Multi-step validation ensures each heredoc is properly paired and safe
**Impact:** Fewer false positives when using valid heredoc constructs with complex quoting patterns like `cat <<'EOF'` or `cat <<\EOF`

### Better Process Cleanup
**What changed:** Improved handling of child processes during shutdown
**Previous behavior:** Some child processes could linger after Claude Code exits
**New behavior:** More thorough cleanup ensures all spawned processes terminate properly
**Impact:** Cleaner system state after using Claude Code, no orphaned processes

## 🐛 Bug Fixes

### Fixed: Heredoc Delimiter Validation
- **Issue:** Valid heredoc patterns with multiple quotes were incorrectly rejected
- **Cause:** Regex pattern didn't account for all valid quoting variations
- **Resolution:** New validation logic handles complex delimiter patterns correctly
- **Affected versions:** v1.0.78 through v1.0.84

### Fixed: Environment Variable Error Handling
- **Issue:** Invalid CLAUDE_CODE_MAX_OUTPUT_TOKENS values could crash the application
- **Cause:** Direct error throwing without graceful fallback
- **Resolution:** Invalid values now trigger warnings and use defaults
- **Affected versions:** v1.0.80 through v1.0.84

### Fixed: Missing Cleanup on Graceful Shutdown
- **Issue:** Some cleanup handlers weren't executing during normal shutdown
- **Cause:** Shutdown sequence didn't properly await all cleanup operations
- **Resolution:** Improved shutdown flow ensures all handlers run within timeout
- **Affected versions:** v1.0.82 through v1.0.84
