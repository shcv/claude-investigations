# Changelog for version 1.0.118

## 🎯 Highlights
This version temporarily disables the sandbox security system while adding SOCKS5 proxy infrastructure and fixing a symlink resolution bug in CLAUDE.md file processing.

## 🚨 Critical Changes

### Sandbox System Temporarily Disabled
**What:** The entire sandbox wrapping system has been disabled, causing all commands to run without filesystem or network restrictions.

**Details:**
- The sandbox wrapper function `nx6()` at line 375662 now returns early, bypassing all sandbox logic
- Both macOS (`sandbox-exec`) and Linux (`bwrap`) sandboxing are non-functional
- Commands execute with full system access instead of isolated environments
- This appears to be a temporary disable, likely for debugging or testing purposes
- **Evidence**: `nx6()` at line 375662 returns input unchanged, making all subsequent sandbox code unreachable

**Impact:** Users expecting sandboxed execution will have NO security isolation in this version. Commands run with full system privileges.

## 🐛 Bug Fixes

### Fixed Symlink Resolution in CLAUDE.md Processing
**What:** CLAUDE.md files accessed through symbolic links are now properly resolved to their real paths.

**Details:**
- The `rd()` function at line 399923 now resolves symlinks before processing CLAUDE.md files
- Both the symlink path and resolved real path are tracked to prevent infinite loops
- Import paths within CLAUDE.md files are correctly resolved relative to the real file location
- Prevents circular symlink issues and incorrect file path resolution
- **Evidence**: `rd()` at line 399923 uses `uJ()` to resolve symlinks and tracks both paths in the visited set (lines 399947-399959)

**Impact:** Users with symlinked CLAUDE.md files will no longer encounter incorrect behavior or infinite loops during file processing.

## 🔧 Internal Improvements

### SOCKS5 Proxy Support Infrastructure Added
**What:** Linux network bridge now supports both HTTP and SOCKS5 proxy ports for future sandbox use.

**Details:**
- Function `gBB()` at line 375277 now accepts both HTTP and SOCKS proxy port parameters
- Returns both `httpProxyPort` and `socksProxyPort` in the bridge configuration (lines 375327-375328)
- Environment variables configured for gRPC, Docker, and Cloud SDK to use SOCKS proxies
- Infrastructure is in place but not active due to sandbox being disabled
- **Evidence**: `gBB()` signature changed from `(A)` to `(A, B)` at line 375277, with new return structure including both ports

**Note:** This enhancement will only be effective when the sandbox system is re-enabled.

### Improved Async Cleanup for Proxy Servers
**What:** Proxy server cleanup is now properly awaited and handles both HTTP and SOCKS5 proxies.

**Details:**
- Function `YC0()` at line 375687 now uses `Promise.all()` to wait for all proxies to shut down
- HTTP proxy cleanup properly awaited instead of fire-and-forget
- SOCKS proxy cleanup added for the new proxy type (lines 375714-375722)
- Both proxies shut down in parallel for faster cleanup
- Prevents race conditions and leaked proxy processes during shutdown
- **Evidence**: `YC0()` at line 375687 changed from synchronous to async with Promise-based cleanup

**Impact:** More reliable shutdown process with no leaked background processes.

## 📦 Dependency Updates

### AWS Bedrock SDK Updated
**What:** Internal AWS Bedrock SDK dependencies refreshed with updated function identifiers.

**Details:**
- Approximately 8,498 function names were renamed due to bundler minification changes
- No functional changes to AWS SDK behavior
- Removed variables `Hl1`, `if0`, `trA` and added equivalents `Nl1`, `af0`, `prA`
- All AWS Bedrock command classes and serialization functions updated
- **Evidence**: Variables at lines 5314-5390 show minified name changes

**Impact:** No user-visible changes; internal dependency maintenance only.
