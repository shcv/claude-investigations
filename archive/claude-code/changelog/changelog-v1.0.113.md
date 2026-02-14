# Changelog for version 1.0.113

## Highlights
Version 1.0.113 enhances security with workspace trust validation for OpenTelemetry helpers, improves prompt caching with per-model control via new environment variables, and refines user experience by filtering out error sessions and improving alias detection to preserve custom configurations.


### Per-Model Prompt Caching Control
**What:** Fine-grained control over prompt caching for individual model families
**How to use:**
```bash
# Disable caching for Haiku models only
export DISABLE_PROMPT_CACHING_HAIKU=true

# Disable caching for Sonnet models only
export DISABLE_PROMPT_CACHING_SONNET=true

# Disable caching for Opus models only
export DISABLE_PROMPT_CACHING_OPUS=true

# Or disable globally for all models (existing behavior)
export DISABLE_PROMPT_CACHING=true
```
**Details:**
- Allows optimization strategies per model tier (e.g., disable for cheaper Haiku, enable for expensive Opus)
- The global `DISABLE_PROMPT_CACHING` variable still works as before
- Enables cost and performance tuning based on your specific use cases
- **Evidence**: `Sd(A)` function at line 395280 replaces `Pd()` at line 394932 in v1.0.112


### Sessions API Support (Feature-Flagged)
**What:** New v1 Sessions API endpoint alongside existing OAuth API
**Details:**
- New endpoint: `/v1/sessions/organizations/${orgUUID}/sessions` via `mzB()` at line 412649
- Legacy endpoint: `/api/oauth/organizations/${orgUUID}/code/sessions` via `dzB()` at line 412690
- Currently defaults to legacy API (feature flag `o45()` at line 412718 returns false)
- Provides foundation for future migration to new API
- **Evidence**: Split from single function `TzB()` at line 412258 in v1.0.112


### Cache Warming Infrastructure (Disabled by Default)
**What:** Background cache warming to maintain cache freshness during idle periods
**Details:**
- Replays previous API requests after 4 minutes of idle time
- Sends minimal requests (max 10 tokens) to keep cache warm
- Reports telemetry via `tengu_cache_warming_request` event
- Currently disabled (`enabled: false` in `ql5()` configuration at line 437674)
- Configuration includes idle threshold (240s) and warmup intervals (300s)
- **Evidence**: Functions `ql5()` and `Z0Q()` at lines 437674 and 437683, not present in v1.0.112


### Automatic Trailing Whitespace Removal
**What:** All file writes and edits now automatically remove trailing whitespace from each line
**Details:**
- Applies to Write tool operations (line 394194)
- Applies to Edit tool operations (line 386716)
- Preserves line endings while cleaning trailing spaces
- Ensures cleaner, more consistent code formatting
- **Evidence**: `hC0()` function at line 386524, not present in v1.0.112


### Enhanced Usage Statistics Merging
**What:** Improved usage tracking with support for ephemeral cache tiers
**Details:**
- Tracks `ephemeral_1h_input_tokens` and `ephemeral_5m_input_tokens` separately
- Properly merges cache creation statistics across streaming events
- Used when combining usage stats from multiple API responses
- **Evidence**: `hYB()` function at line 395825 with `cache_creation` object structure


### Workspace Trust Validation for OpenTelemetry Helpers
**What changed:** OpenTelemetry headers from project/local settings now require workspace trust
**Why it matters:** Prevents arbitrary code execution from untrusted project configurations
**Details:**
- New function `CZ1()` at line 371858 detects if otelHeadersHelper comes from project/local settings
- Function `ph2()` at line 371865 checks workspace trust via `mx(!0)` before executing helpers
- Returns empty headers instead of executing untrusted code
- Part of broader security hardening effort
- **Evidence**: Replaces simpler `bh2()` at line 371852 in v1.0.112


### Improved Alias Detection Logic
**What changed:** Shell alias detection now preserves custom user configurations
**How it works:**
- Only removes/replaces aliases pointing to the default Claude installation path
- Preserves custom aliases pointing to other locations
- Shows "Custom claude alias found" message when detected
- Displays "Keeping your existing alias configuration" to inform users
**Details:**
- Enhanced regex pattern allows flexible whitespace: `/^\s*alias\s+claude\s*=/` (line 377702)
- Function `jk1()` at line 377711 parses alias values and compares against default path
- Previous version `V11()` at line 377695 in v1.0.112 removed all claude aliases indiscriminately
- **Evidence**: Compares alias target against `zv` (default path) at line 377718


### Error Session Filtering
**What changed:** Session list now excludes sessions that start with API errors
**Details:**
- Filters out sessions where `firstPrompt` starts with "API Error"
- Filters out sessions where `summary` starts with "API Error"
- Improves UI cleanliness by hiding failed/error sessions
- **Evidence**: `YA1()` function at lines 428269-428270, enhanced from `QA1()` at line 428139 in v1.0.112


### Improved Slash Command Validation
**What changed:** Character-level validation replaced path-prefix checking
**Details:**
- New `NZ5()` function at line 421329 validates command names contain only alphanumeric characters, colons, hyphens, and underscores
- Replaces previous logic that checked for `/var`, `/tmp`, `/private` path prefixes
- Provides more precise security validation
- **Evidence**: Used at line 421356 instead of path checks at line 421220 in v1.0.112


### Conditional Telemetry Initialization
**What changed:** Telemetry initialization can be deferred based on workspace trust
**Details:**
- New flag `Fy0` at line 429230 tracks initialization state
- Initialization deferred when otelHeadersHelper is configured but trust not established
- Function `NtB()` at line 429241 allows manual initialization when conditions are met
- Prevents sensitive telemetry from initializing in untrusted workspaces
- **Evidence**: `EtB` variable at line 429231 with conditional logic, replacing direct initialization in `VtB` at line 429100 in v1.0.112


### Hotkey Change for Expand/Collapse
**What changed:** Expand/collapse hotkey changed from Ctrl+R to Ctrl+O
**Details:**
- Affects transcript/prompt view toggle in interactive mode
- Shows in UI hints as "(ctrl+o to expand)" instead of "(ctrl+r to expand)"
- Note: Ctrl+R still used for error retry functionality (separate feature)
- **Evidence**: Variable `F2B` at line 372920 replaces `B2B` at line 372904 in v1.0.112


### Refactored Authentication Helper
- New `uzB()` function at line 412641 extracts common authentication logic
- Consolidates access token and organization UUID retrieval
- Used by both `dzB()` and `mzB()` session fetching functions
- Improves code reusability and maintainability


### Enhanced Prompt Caching Function Signatures
- Functions now accept model parameter for per-model cache control
- `gYB()` at line 395982, `dt6()` at line 395373, `ct6()` at line 395400, `lt6()` at line 395849
- All call `Sd(model)` instead of `Pd()` for cache control decisions
- Enables the per-model caching feature described above


### Import Optimization
- Removed unused `stream` import (line 337903 in v1.0.112)
- Added `PassThrough` stream import as `ip5` (line 441307)
- Added `cwd` import from `node:process` as `ZNA` (line 361192)
- Streamlines dependencies and improves code clarity
