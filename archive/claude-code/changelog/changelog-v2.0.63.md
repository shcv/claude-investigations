# Changelog for version 2.0.63

## Highlights

This release introduces performance monitoring infrastructure to detect slow filesystem and shell operations, adds automatic retry logic for ripgrep EAGAIN errors, and optimizes settings writes to avoid unnecessary disk I/O.


### Slow Operation Detection

**What:** New performance monitoring that detects and logs slow filesystem and shell command operations.

**How it works:**
- All synchronous filesystem operations (20 in total) are now wrapped with timing instrumentation
- Shell command executions via `execSyncWithDefaults` are similarly monitored
- Operations exceeding 5ms are logged to debug output with the operation name and duration

**Details:**
- Log format: `[SLOW OPERATION DETECTED] fs.readFileSync (12.3ms)` or `[SLOW OPERATION DETECTED] execSyncWithDefaults (156.7ms): git status...`
- Monitored fs operations include: `existsSync`, `statSync`, `readFileSync`, `writeFileSync`, `appendFileSync`, `copyFileSync`, `unlinkSync`, `renameSync`, `readdirSync`, `mkdirSync`, `rmdirSync`, `rmSync`, and others
- For shell commands, the first 100 characters of the command are included in the log
- Logs are written to debug output (controlled by `CLAUDE_CODE_DEBUG_LOGS_DIR` environment variable)
- **Evidence:** `XX()` wrapper function at line 554, threshold `Zl2 = 5` at line 605, shell monitoring in `MG()` at line 16934


### Ripgrep EAGAIN Error Auto-Retry

**What:** Automatic retry mechanism when ripgrep encounters "Resource temporarily unavailable" (EAGAIN/error 11) errors.

**How it works:**
When ripgrep fails with an EAGAIN error (common in high-concurrency environments), Claude Code now:
1. Detects the error from stderr output
2. Logs a debug message
3. Retries the search with single-threaded mode (`-j 1`)
4. Sets a global flag to use single-threaded mode for all subsequent ripgrep calls

**Details:**
- Error detection function `lJ9()` checks for "os error 11" or "Resource temporarily unavailable" strings
- Only retries once to prevent infinite loops
- Telemetry event `tengu_ripgrep_eagain_retry` is logged when this occurs
- **Evidence:** `lJ9()` function at line 17125, retry logic at lines 17163-17178


### Optimized OAuth Account Settings Writes

**What:** Settings are now only written to disk when OAuth account information actually changes.

**How it works:**
- Previously, every call to update OAuth account settings triggered a disk write
- Now, all five account fields (accountUuid, emailAddress, organizationUuid, displayName, hasExtraUsageEnabled) are compared before writing
- If all fields match the existing stored values, the write is skipped

**Details:**
- Reduces unnecessary disk I/O during token refresh operations
- Uses strict equality checks with optional chaining for safety
- **Evidence:** `HW1()` function at line 74155 with comparison at lines 74170-74176, compared to old unconditional `G$1()` function


### Increased Startup Performance Telemetry Sampling

**What:** Startup performance telemetry sampling rate increased from 0.1% to 0.5% of CLI invocations.

**Details:**
- Constant changed from `OP9 = 0.001` to `Xa2 = 0.005`
- Provides 5x more data points for analyzing real-world startup performance
- Can still be forced on with `CLAUDE_CODE_PROFILE_STARTUP=1` environment variable
- **Evidence:** `Xa2 = 0.005` at line 2661, sampling logic at line 2674


### Registered Hooks State Management

**What:** Added functions to get and set registered hooks in the global state.

**Details:**
- New `kTA()` function to set registered hooks (line 2395)
- New `vTA()` function to get registered hooks (line 2398)
- New `jJA()` function to access plan slug cache (line 2401)
- **Evidence:** Functions at lines 2395-2401


### Internal Refactoring

- AWS SDK dependencies restructured with consolidated module patterns
- Import changes for `child_process` module (now uses named imports for `spawn` and `spawnSync`)
- Various internal variable and function renames consistent with minification changes
