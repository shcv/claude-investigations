# Changelog for version 2.0.31

## 🎯 Highlights

Version 2.0.31 introduces startup performance profiling capabilities, significantly enhances sed command security validation, and adds support for the latest web-search API. Additionally, internal improvements to diff rendering and telemetry tracking provide better visibility into Claude Code's operations.

## 🚀 New Features

### Startup Performance Profiling

**What:** Optional profiling system to measure Claude Code's startup performance and memory usage across initialization phases.

**How to use:**
```bash
# Enable startup profiling
CLAUDE_CODE_PROFILE_STARTUP=1 claude

# The profiling report will automatically display after startup showing:
# - Time elapsed at each checkpoint (absolute and delta)
# - Memory usage (RSS and heap) at each checkpoint
# - Total startup time
```

**Details:**
- Tracks 30+ checkpoints throughout the startup sequence
- Records both timing (via Node.js `perf_hooks`) and memory metrics
- Zero overhead when disabled (default)
- Useful for diagnosing slow startup issues or investigating performance regressions
- **Evidence**: `o5()` at line 3881, `RB9()` at line 3891, `B80()` at line 3919, profiler initialization in `aqA` at line 3926

### File Operation Telemetry

**What:** Privacy-preserving telemetry that tracks file operations (read, write, edit) using hashed identifiers.

**How it works:**
- File paths are hashed (SHA256, first 16 characters) for anonymization
- File content is hashed (SHA256) to detect duplicate operations
- Operation type and tool name are recorded
- Data sent via existing telemetry infrastructure

**Details:**
- Automatically enabled when telemetry is active
- Only metadata is recorded - actual file paths and content remain private
- Helps Anthropic understand common file operation patterns
- **Evidence**: `sM()` function at line 249864, hash functions `Nd8()` at line 249858 and `Ld8()` at line 249861

### Web Search API Update

**What:** Support for the new `web-search-2025-03-05` beta API.

**Details:**
- Automatically enabled for Vertex AI platform with Claude 4.x models
- Provides access to updated web search capabilities
- Part of Anthropic's beta features system
- **Evidence**: `ErB = "web-search-2025-03-05"` at line 203723, `AT8()` function at line 203732

## 🔒 Security Enhancements

### Enhanced Sed Command Validation

**What:** Significantly improved security validation for sed commands to prevent dangerous operations while allowing safe read-only usage.

**How it works:**
The validation now uses a comprehensive whitelist approach with multiple layers:

1. **Pre-parsing flag detection** - Blocks dangerous flag combinations like `-ew`, `-we` before parsing
2. **Whitelist validation** - Only allows two safe patterns:
   - Print-only operations with `-n` flag (e.g., `sed -n '1,10p' file.txt`)
   - Simple substitutions with safe flags (e.g., `sed 's/old/new/' file.txt`)
3. **Comprehensive blacklist** - Blocks 15+ dangerous patterns including:
   - Write commands (`w`, `W`)
   - Execute commands (`e`, `E`)
   - Non-ASCII characters and escape sequences
   - Command chaining with semicolons in certain contexts
   - Braces, negation operators, and other advanced features

**Details:**
- Builds upon existing sed validation from v2.0.30 (function `hoB` at line 209135)
- Adds four new validation helpers: `Aj8()` at line 209202, `Bj8()` at line 209245, `Qj8()` at line 209254, `Zj8()` at line 209384
- New validation function `JtB()` at line 209288 replaces `hoB`
- Dangerous flag combination detection in `Gj8()` at line 209345
- Prevents file modification and command execution while allowing safe text processing
- **Evidence**: Comparison of `hoB()` at line 209135 in v2.0.30 vs `JtB()` at line 209288 in v2.0.31

## 🔧 Improvements

### Diff Rendering Simplification

**What:** Streamlined diff patch rendering with cleaner code and fewer configuration options.

**Changes:**
- Removed `skipUnchanged` and `hideLineNumbers` parameters from diff rendering
- Eliminated conditional dimmed color variants (`diffAddedWordDimmed`, `diffRemovedWordDimmed`)
- Simplified component interface from 7 parameters to 5
- Removed `hidden` parameter from line number component calls

**Details:**
- Function signature changed from `hB6(A, B, Q, I, G, Z, Y)` to `$Q6(A, B, Q, I, G)`
- More consistent visual rendering across different diff contexts
- **Evidence**: `hB6()` at line 288996 in v2.0.30 vs `$Q6()` at line 289176 in v2.0.31; word diff function `fB6()` at line 288906 in v2.0.30 vs `wQ6()` at line 289088 in v2.0.31

### Settings Loading Profiling

**What:** Added profiling checkpoints around settings initialization.

**Details:**
- Tracks time spent loading settings from various sources
- Helps identify slow configuration loading
- **Evidence**: `o5("eagerLoadSettings_start")` at line 485096, `o5("eagerLoadSettings_end")` at line 485107 in function `Bo5()` at line 485095

### CLI Argument Parsing Instrumentation

**What:** Added profiling checkpoints before and after CLI argument parsing.

**Details:**
- Helps identify overhead from command-line option processing
- Part of the overall startup profiling infrastructure
- **Evidence**: `o5("cli_before_main_import")` at line 486806, `o5("cli_after_main_import")` at line 486808 in function `Wo5()` at line 486798

## 🐛 Bug Fixes

### Redirect Operator Quoting

**What:** Fixed shell command quoting logic to correctly handle file descriptor redirects.

**Details:**
- File descriptor redirects like `2>` or `2>>` are no longer incorrectly quoted
- Prevents errors when redirecting stderr or other file descriptors
- **Evidence**: Function `ET8()` at line 204583 adds check for `\d+>>?` pattern, replacing `bR8()` at line 204525 in v2.0.30

### Hook Removal Edge Case

**What:** Fixed settings cleanup when removing the last hook from a configuration source.

**Details:**
- Ensures `hooks` object is properly removed when empty
- Prevents empty configuration objects from persisting
- **Evidence**: Function `rV2()` at line 414417 adds proper cleanup logic at lines 414433-414435, improving upon `qV2()` at line 414128 in v2.0.30

## 📦 Internal Changes

### Import Organization

**What:** Consolidated and reorganized various module imports.

**Changes:**
- Replaced `import Ae from "stream"` with `import { PassThrough as Lr5 } from "stream"` at line 482338
- Replaced `import e51 from "node:child_process"` with `import { execSync as U6Q, spawn as Qd8 } from "node:child_process"` at line 249174
- Added `import { cwd as hR0 } from "node:process"` at line 70725
- Added `import { homedir as br5 } from "node:os"` at line 484007
- Added `import { createHash as pB6, randomBytes as lB6 } from "crypto"` at line 286520
- Removed redundant `import BP9 from "node:os"` and `import il2 from "node:process"`

**Details:**
- More explicit imports improve tree-shaking and code clarity
- Reduces namespace pollution from default imports

### Color Diff Module Loading

**What:** Updated native color diff module loading with better error handling.

**Details:**
- Added async function `GVQ()` at line 289328 for loading the Rust-based ColorDiff module
- Improved fallback behavior when native module unavailable
- Better logging for debugging color diff issues
- **Evidence**: Function `GVQ()` at line 289328, initialization in `uy1` at line 289318

### Component Refactoring

**What:** Various minor component and utility function additions.

**Details:**
- Added `BVQ` component at line 289014 for diff patch rendering
- Added utility functions: `Vc()` at line 446305, `Qp5()` at line 460873, `xM2()` at line 429780
- Added helper functions for tool management: `Gu2()` at line 456056, `Ve1()` at line 456053, `Iu2()` at line 456048

---

**Note:** This changelog focuses on user-visible changes and significant internal improvements. Version 2.0.31 includes additional internal refactoring and code organization improvements not detailed here.
