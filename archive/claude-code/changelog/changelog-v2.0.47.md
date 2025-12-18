# Changelog for version 2.0.47

## 🎯 Highlights

Version 2.0.47 introduces remote environment configuration for Teleport users, implements intelligent plan mode parallelism based on subscription tier, and adds automatic image compression to prevent API errors from oversized images.

## 🚀 New Features

### Remote Environment Configuration
**What:** New CLI command to configure default remote development environments for Teleport sessions

**How to use:**
```bash
# Launch interactive environment selector
claude remote-env
```

**Details:**
- Interactive UI displays all available remote environments
- Selected environment is saved to local settings as the default
- Configuration persists across sessions
- Environments can also be managed at https://claude.ai/code
- Stores selection in `settings.local.json` under `remote.defaultEnvironmentId`
- **Evidence**: `EZ9()` at line 489948, `zZ9()` at line 489984, command registration at line 490139

### Automatic Image Compression
**What:** Images in conversation context are now automatically compressed when they exceed size limits

**How it works:**
- Automatically detects base64-encoded images larger than ~3.9MB
- Compresses using JPEG format via Sharp library
- Preserves original media type metadata
- Prevents API errors from oversized content

**Details:**
- Maximum uncompressed image size: 3,932,160 bytes (~3.9MB)
- Compression threshold: 8,192 bytes
- Only applies to images in conversation context, not uploaded files
- Transparent to users - happens automatically during content processing
- **Evidence**: `egQ()` at line 155776, called from content truncation at line 502920

### Plan Mode Exit State Tracking
**What:** Internal state management to track when users have exited plan mode

**Details:**
- Prevents re-prompting about plan mode after explicit exit
- Improves workflow continuity in long sessions
- State persists for the duration of the current session
- **Evidence**: `qV0()` getter at line 2315, `og()` setter at line 2318

## ⚡ Behavior Changes

### Plan Mode Parallelism Now Tier-Based
**What changed:** Plan mode now adjusts parallel agent count based on subscription tier instead of using a fixed default

**Previous behavior:** All users got 4 parallel agents in plan mode (unless overridden by environment variable)

**New behavior:**
- **Free tier:** 1 parallel agent (75% reduction)
- **Team/Enterprise tier:** 3 parallel agents (25% reduction)
- **Max subscription with 20x model:** 3 parallel agents
- **Environment variable override:** Still available via `CLAUDE_CODE_PLAN_V2_AGENT_COUNT` (1-10)

**Impact:**
- Free tier users will experience slower plan mode execution
- Premium users retain better parallelism
- Change encourages upgrade to paid tiers for better performance
- **Evidence**: `JQ2()` at line 315736 (was `v62()` at line 316064 in v2.0.46)

## 🐛 Bug Fixes

None identified in this release.

## 🔧 Technical Improvements

### OpenTelemetry Queue Configuration
- Added explicit max queue size constant (8,192) for telemetry batching
- Improves observability infrastructure stability
- No user-facing impact
