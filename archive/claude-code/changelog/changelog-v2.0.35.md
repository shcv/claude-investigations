# Changelog for version 2.0.35

## 🎯 Highlights

Version 2.0.35 significantly strengthens security around network path access and file attachments. The update adds comprehensive UNC path detection to prevent unauthorized network resource access, implements file size limits for at-mention attachments, and introduces an optional auto-exit feature for idle sessions. Additionally, slash command search performance was improved through better indexing.

## 🔒 Security Enhancements

### Enhanced UNC Path Detection

**What:** Expanded detection of Universal Naming Convention (UNC) paths that could access network shares and remote resources.

**Details:**
- **Comprehensive pattern detection** - Now detects 6 different UNC path patterns (previously only 1):
  - Traditional backslash notation: `\\server\share`
  - Forward-slash notation: `//server/share`
  - WebDAV paths containing `DavWWWRoot`
  - IPv4-based paths: `\\192.168.1.1\share`
  - IPv6-based paths: `\\[2001:db8::1]\share`
  - SSL/port notation variations: `@SSL@443`, `@443@SSL`
- **Defense-in-depth check** - Added explicit UNC path verification in permission checking that triggers before other path validation, requiring manual user approval with message: "Claude requested permissions to read from {path}, which appears to be a UNC path that could access network resources"
- **Evidence**: `kB1() at line 469623`, `Cm() at line 474419` (new UNC check at lines 474427-474436)

### Expanded Windows Path Security

**What:** Additional checks for potentially dangerous Windows path patterns.

**Details:**
- Blocks paths containing `$` or `%` characters (environment variable references like `%APPDATA%` or `$env:USERNAME`)
- Integrated comprehensive UNC detection into suspicious path validation
- **Evidence**: `hs2() at line 474240` (new checks at lines 474253-474254)

### File Size Limits for At-Mentions

**What:** Enforces a 256KB size limit when files are attached via at-mention (`@` symbol).

**How it works:**
```bash
# If you try to attach a large file via at-mention:
@/path/to/large-file.log

# Claude Code will now check the file size first and reject if > 256KB
```

**Details:**
- Prevents accidental attachment of large log files, binaries, or data files that would waste tokens
- Size check happens before file content is read, saving processing time
- Logs telemetry event `tengu_attachment_file_too_large` with file size for monitoring
- Regular Read tool usage (without at-mention) is unaffected and can still handle large files with offset/limit parameters
- **Evidence**: `npA() at line 481542`, `ob1() at line 313340` (size check at lines 313344-313349)

## ⚡ Performance Improvements

### Optimized Slash Command Search

**What:** Improved slash command autocomplete performance through better data structure indexing.

**Details:**
- Reduced redundant array creation during fuzzy search by pre-building search index
- Changed from creating multiple search entries per command (via `flatMap`) to single structured entries (via `map`)
- Improves responsiveness when typing `/` to search available commands
- **Evidence**: `p22() at line 381579` (refactored from `d22()` which used `flatMap` at v2.0.34 line 381594)

### Automatic Image Compression

**What:** New wrapper function that automatically compresses images exceeding 25KB to optimize token usage.

**Details:**
- Transparently compresses large images before sending to the API
- Uses multi-strategy compression: resizing, format optimization, quality adjustment
- Default threshold: 25KB (25,000 tokens)
- **Evidence**: `rk1() at line 276879`

## 🔧 Configuration Changes

### Simplified Permission System

**What:** Migrated `ignorePatterns` configuration to unified permissions system.

**Details:**
- The `ignorePatterns` field is automatically migrated to permission rules on first run
- After successful migration, `ignorePatterns` is removed from config file
- Runtime file access checking now uses unified `xC()` permission function instead of separate `GN()` ignore checker
- Behavior remains the same - patterns still block file access, just through the permissions infrastructure
- **Evidence**: `u6A() at line 474347` (simplified from `IsA()`), `se2() at line 487463` (migration with cleanup at line 487480)

## 🆕 New Features

### Optional Auto-Exit on Idle

**What:** Claude Code can now automatically exit after a configured period of inactivity.

**How to use:**
```bash
# Set idle timeout to 60 seconds (60000 milliseconds)
export CLAUDE_CODE_EXIT_AFTER_STOP_DELAY=60000
claude

# Claude Code will now exit automatically after 60 seconds of no activity
```

**Details:**
- Disabled by default - only activates when `CLAUDE_CODE_EXIT_AFTER_STOP_DELAY` environment variable is set
- Value is in milliseconds (e.g., 60000 = 60 seconds)
- Timer resets whenever Claude Code processes a command
- Useful for automated testing, CI/CD pipelines, or managing long-running sessions
- **Evidence**: `XA9() at line 488655`, exit message at line 488668

### Improved Model Name Recognition

**What:** Better handling of model names with bracketed suffixes like `[1m]`.

**Details:**
- Recognizes model names with `[1m]` suffix (e.g., `claude-3-5-sonnet-20241022[1m]`)
- Strips suffix and validates against known model list
- Improves compatibility with certain API responses or model name formats
- **Evidence**: `ce5() at line 466959`

## 🐛 Bug Fixes

### Fixed Assistant Message Handling

**What:** Improved reliability of assistant message extraction from streaming responses.

**Details:**
- Changed from `return` on first assistant message to collecting all messages and returning the last one
- Prevents potential issues where intermediate assistant messages could be missed
- Adds explicit error if no assistant message found in stream
- **Evidence**: `ES() at line 468457` (formerly `HS()`)

### Enhanced Read Tool Validation

**What:** Read tool now properly validates file paths against permission context during input validation.

**Details:**
- Passes `toolPermissionContext` to validation function to check permissions earlier
- Prevents attempting to read files that will be denied by permissions
- More accurate error messages about why files cannot be read
- **Evidence**: `t4.validateInput(F, B) at line 313355` in v2.0.35 (previously missing context parameter)

## 📝 Internal Improvements

- Refactored permission checking for read operations to use consistent code paths
- Added IDE selection context filtering to respect file permissions
- Consolidated path normalization helpers using `node:path` posix/win32 utilities
- Improved stream handling with consistent PassThrough stream usage across modules
- Better separation of initialization logic from runtime functionality

---

**Note:** This changelog focuses on user-visible changes and security improvements. Many internal function renamings due to code minification are not included unless they represent functional changes.
