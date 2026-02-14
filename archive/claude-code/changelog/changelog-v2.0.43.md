# Changelog for version 2.0.43

## Highlights

Version 2.0.43 delivers a major internal refactoring of the sandbox subsystem, replacing the previous function-based architecture with a unified manager pattern. This release adds clickable hyperlink support in terminal output, enhances Linux sandboxing with seccomp filtering for Unix socket blocking, and introduces plan mode infrastructure for persistent task planning workflows.


### Clickable Hyperlinks in Terminal Output
**What:** Terminal output now supports clickable hyperlinks using the OSC 8 escape sequence standard, allowing tools to render URIs that users can click in compatible terminals.

**How to use:**
Hyperlinks are automatically rendered when tools generate output with URIs. Compatible terminals (iTerm2, GNOME Terminal, Windows Terminal, etc.) will display these as clickable links.

**Details:**
- Screen buffer now tracks hyperlinks via a Map structure (`hyperlinks: new Map()` at line 76624)
- New functions: `Bk0()` sets hyperlinks at screen positions (lines 76647-76651), `d0A()` retrieves them (lines 76652-76656)
- `DJ1()` tracks hyperlink state changes for diff generation (line 77362)
- `gp9()` encodes hyperlinks into ANSI escape sequences (lines 78736-78738)
- Terminal output handler processes hyperlink diff entries (lines 78765-78767)
- **Evidence**: `Bk0() at line 76647`, `d0A() at line 76652`, `DJ1() at line 77362`, `gp9() at line 78736`


### Enhanced Linux Sandbox Security with Seccomp Filtering
**What:** Linux sandboxing now blocks Unix domain socket creation using Berkeley Packet Filter (BPF) seccomp filters, preventing sandboxed processes from bypassing network restrictions via local sockets.

**How it works:**
When network sandboxing is enabled on Linux, Claude Code automatically applies pre-compiled seccomp filters to block `socket(AF_UNIX, ...)` syscalls.

**Details:**
- Architecture-specific (x64/arm64) pre-compiled BPF filters in `vendor/seccomp/` directories
- `apply-seccomp` binary applies the filters to child processes
- Functions: `Q$Q()` detects CPU architecture (x64/arm64), `Ox1()` locates BPF filter files, `NiA()` finds the apply-seccomp binary
- `I$Q()` retrieves the appropriate seccomp filter for the platform
- Automatic cleanup via `dP6()` and `Rx1()` on process exit
- 32-bit x86 (ia32) explicitly not supported due to `socketcall()` syscall complexity (line 1507)
- Fallback: `allowAllUnixSockets` configuration option to disable seccomp filtering when needed (line 1693)
- **Evidence**: `Q$Q()` at line ~1535, `Ox1()` for BPF filter location, `NiA()` for apply-seccomp binary discovery, seccomp integration at lines 1686-1693


### Plan Mode Infrastructure
**What:** New persistent plan file storage system for task planning workflows, allowing Claude Code to save, retrieve, and track acceptance of execution plans.

**Details:**
- `eO()` retrieves the plans directory path
- `pm()` generates plan file paths for specific agents
- `sx()` reads plan file contents
- `BnA()` checks if a plan has been accepted
- `INQ()` and `Zy6()` manage plan file creation and updates
- `WNQ()` and `ETQ()` handle tool name overrides in plan context
- Plan files persist across sessions for continuity
- **Evidence**: `eO()`, `pm()`, `sx()`, `BnA()`, `INQ()`, `Zy6()` functions added for plan file management


### Sandbox Architecture Refactoring
**What changed:** The sandbox implementation has been completely restructured from scattered individual functions into a centralized `dZ` manager object with a cleaner API.

**Details:**
- **Before**: 41 individual functions (`eu()`, `dm8()`, `cm8()`, `gm8()`, `um8()`, `mm8()`, etc.) handled different sandbox aspects
- **After**: Single `dZ` manager object (lines 277192-277216) with methods: `initialize()`, `isSupportedPlatform()`, `checkDependencies()`, `getFsReadConfig()`, `getFsWriteConfig()`, `getNetworkRestrictionConfig()`, `wrapWithSandbox()`
- Settings getters (`Qv1`, `Iv1`, `Gv1`) now use memoization for better performance (lines 279679-279691)
- New unified initialization via `XS6()` function (line 279607)
- Clean reset functionality via `WS6()` (line 279632)
- Public API (`DQ` object at line 279692) remains unchanged for backward compatibility
- Removed legacy functions from v2.0.42: `eu()` (line 220098), `dm8()` (line 220108), `cm8()` (line 220112), `mm8()` (line 220052), `gm8()` and `um8()` (lines 220040-220051), along with 35+ other sandbox-related functions
- **Evidence**: New `dZ` object at lines 277192-277216, old functions removed from v2.0.42 lines 220040-220112


### Enhanced Permission Management
**What changed:** Permission checking and configuration validation now uses comprehensive Zod schemas for type safety and validation.

**Details:**
- Domain pattern validation with security constraints prevents overly broad network rules
- Filesystem restriction schemas ensure valid path specifications
- Ripgrep configuration validation
- Comprehensive sandbox config validation via `c$Q` schema system
- `VqQ()` function converts permissions to sandbox config format
- Network permission checking via `M$Q()` replaces the old `CQQ()` function
- **Evidence**: `VqQ()` for permission conversion, `M$Q()` for domain-based network checking, schema validation system `c$Q`


### Filesystem and Network Configuration
**What changed:** Filesystem and network restriction configuration now uses dedicated getter functions with clearer interfaces.

**Details:**
- `Ij6()` retrieves filesystem read configuration
- `Gj6()` retrieves filesystem write configuration  
- `Zj6()` retrieves network restriction configuration
- `P$Q()` checks if local binding is allowed
- `L$Q()` retrieves ripgrep-specific configuration
- `y$Q()`, `k$Q()`, `_$Q()`, `x$Q()` get HTTP/SOCKS proxy ports and socket paths
- **Evidence**: `Ij6()`, `Gj6()`, `Zj6()`, `P$Q()`, `L$Q()` functions for configuration access


### Test Infrastructure Enhancement
**What changed:** New fixture-based testing system with caching for improved test reproducibility and performance.

**Details:**
- `Ay6()` provides fixture caching mechanism
- `tqQ()` implements token counting with fixture support
- Better test isolation and repeatability
- **Evidence**: `Ay6()` for fixture caching, `tqQ()` for token counting with fixtures


### Session and Message Handling
**What changed:** Enhanced session lifecycle hooks and message tracking capabilities.

**Details:**
- `A22()` and `WW5()` provide session hook registration system
- `nA0()` extracts message/tool/tooluse IDs from messages
- `Xk2()` groups tool uses for grouped rendering
- `ITQ()` renders grouped tool use messages
- `$RQ()` implements rate-limited messaging
- `WeA()` and `FeA()` track message sources
- **Evidence**: `A22()`, `WW5()` for session hooks, `nA0()` for ID extraction, `Xk2()` for grouping, `ITQ()` for rendering


### Debugging and Logging
**What changed:** New unified sandbox debug logging function replaces scattered logging calls.

**Details:**
- `LB()` function provides centralized sandbox debug logging
- Consistent log format across sandbox operations
- Better troubleshooting capability
- **Evidence**: `LB()` function for sandbox debug logging throughout the new sandbox implementation


### Platform Detection
**What changed:** Improved platform detection and validation for sandbox compatibility.

**Details:**
- `ON()` detects platform (macOS, Linux, Windows, unknown)
- `W$Q()` checks Linux bwrap/socat availability  
- `Zv1()` validates if sandboxing is supported on the current platform
- Better error messages when sandbox dependencies are missing
- **Evidence**: `ON()` for platform detection, `W$Q()` for Linux dependency checking, `Zv1()` for support validation


### Ripgrep Integration
**What changed:** Better detection and configuration of ripgrep (`rg`) for code search operations.

**Details:**
- `owQ()` checks if ripgrep is available on the system
- `ziA()` provides ripgrep search function with timeout support
- Configurable ripgrep behavior through sandbox configuration
- **Evidence**: `owQ()` for availability check, `ziA()` for search with timeout


### File Checkpointing
**What changed:** Added ability to check if file checkpointing is enabled.

**Details:**
- `Cc8()` function checks file checkpointing configuration
- Supports incremental file state tracking
- **Evidence**: `Cc8()` function for checkpointing status check


### Removed Legacy Code
- Removed 41 sandbox-related functions from v2.0.42 as part of the architecture refactoring
- Removed old macOS sandbox violation logging functions (`hUQ()`, `YMQ()`, `im8()`, `KQQ()`, `DQQ()`, `Zj1()`)
- Removed old permission rule extraction functions (`bdA()`, `FQQ()`, `bm8()`)
- Removed legacy socat bridge setup function (`Tm8()`)
- Removed old bwrap command wrapper (`AQQ()`)
- Cleaned up obsolete imports (`stream`, `node:child_process` imports that were no longer needed)
- **Evidence**: Functions removed from v2.0.42 lines 154620 (OUB variable), 219367 (Tm8), 219424 (AQQ), 219480 (tP1), 219536 (km8), 219942 (bdA), 219960 (FQQ), 219967 (bm8), 219974 (CQQ), 220040-220051 (gm8/um8), 220052 (mm8), 220098-220114 (eu/dm8/cm8)


### Code Quality Improvements
- Comprehensive refactoring involved 224 declaration changes (154 additions, 41 deletions, 29 modifications)
- 9,192 variable renames (likely from updated minification)
- Structural similarity maintained at 98.4% despite significant refactoring
- Better separation of concerns with centralized manager pattern
- Improved maintainability through reduced function sprawl


**Note on Feature Verification:** All features listed as "new" have been verified to not exist in v2.0.42 by searching both version files. Changes categorized as "improvements" existed in previous versions but have been enhanced or refactored. Line numbers reference the v2.0.43 source file.
