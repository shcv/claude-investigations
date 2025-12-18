# Changelog for version 2.0.49

## 🎯 Highlights

Version 2.0.49 introduces significant infrastructure improvements including a new GrowthBook feature flag system for dynamic feature control, unrestricted model access for Foundry users, and enhanced terminal rendering for emoji and Unicode characters.

## 🚀 New Features

### GrowthBook Feature Flag Integration
**What:** Complete integration of GrowthBook SDK (v1.6.1) for remote feature management and A/B testing
**How to use:**
```bash
# Enable GrowthBook integration
export CLAUDE_CODE_ENABLE_GROWTHBOOK=true
claude
```
**Details:**
- Enables Anthropic to dynamically control features without CLI updates
- Supports real-time feature flag updates via Server-Sent Events (SSE)
- Implements intelligent caching with 60-second stale TTL and 4-hour max age
- Includes automatic retry logic with exponential backoff
- Features pause when browser tab is hidden to save resources
- **Evidence**: `bn2()` at line 447290, `z31` class at line 448817, SDK key `CO0` at line 35311

### GitHub Repository Path Tracking
**What:** New system to track which local directories correspond to which GitHub repositories
**How to use:**
This feature works automatically when you work with GitHub repositories. It enables repository-aware context switching and settings.
**Details:**
- Automatically tracks repo-to-directory mappings in settings
- Enables better multi-repository workflow support
- Stored in `githubRepoPaths` field in user settings
- **Evidence**: `lX9()` at line 507265, `iX9()` at line 507276

## ⚡ Improvements

### Unrestricted Model Access for Foundry Users
**What:** Foundry deployment users now have access to all Claude models without version restrictions
**Details:**
Previously, Foundry users had the same model restrictions as first-party users (excluding claude-3-* models). Now Foundry users can access all available models including legacy versions.
- **Evidence**: `Ez4()` at line 86189 vs `dC4()` at line 86088 in v2.0.47

### Enhanced Terminal Text Rendering for Emoji and Unicode
**What:** Significantly improved display width calculation for emoji, flag characters, and complex Unicode scripts
**Details:**
- Adds fast-path optimization for ASCII strings (performance improvement)
- Correctly handles Regional Indicator flag emojis (🇺🇸, 🇬🇧)
- Proper width calculation for keycap sequences (1️⃣, 2️⃣)
- Better support for zero-width characters in Indic, Arabic, and Hebrew scripts
- Prevents terminal misalignment issues with emoji-containing content
- **Evidence**: `N94()` at line 61894, `q94()` at line 61905, `_g0()` at line 61921

### Improved HTTPS Proxy Compatibility
**What:** Enhanced proxy agent with DNS address family normalization
**Details:**
- Adds custom DNS lookup callback for better proxy compatibility
- Normalizes IPv4/IPv6 address family specifications
- Prevents connection failures with proxies sensitive to address family format
- Maintains existing mTLS certificate support
- **Evidence**: `WhQ()` at line 146672, `N$8()` at line 146623

### Enhanced Settings File Security Isolation
**What:** Improved protection against accidental modification of parent workspace settings
**Details:**
When working in a subdirectory, Claude Code now denies write access to parent workspace `.claude/settings.json` and `.claude/settings.local.json` files. This prevents unintended configuration changes when working in nested directories.
- **Evidence**: `oA2()` function sandbox configuration (diff line 5527-5531)

### Improved Tool Schema Validation
**What:** VerifyResult tool now includes JSON Schema in addition to Zod schema
**Details:**
- Provides dual validation formats for better compatibility
- Enables clearer error messages when tool is used incorrectly
- Supports both `inputSchema` (Zod) and `inputJSONSchema` (JSON Schema)
- **Evidence**: `UM3()` at line 497621 vs `r$3()` at line 494892 in v2.0.47

## 🔧 Technical Changes

### Code Organization
- Refactored text segmentation functions for better emoji handling (`y44()` at line 76651, `k44()` at line 76643)
- Consolidated import statements for better module organization
- Updated internal function names for consistency (147 functions added, 22 removed)

### Infrastructure
- Added support for dynamic feature rollouts via remote configuration
- Implemented stale-while-revalidate caching strategy for feature flags
- Enhanced analytics tracking for feature evaluation and experiment participation
