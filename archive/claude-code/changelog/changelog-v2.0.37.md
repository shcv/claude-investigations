# Changelog for version 2.0.37

## 🎯 Highlights

Version 2.0.37 introduces user feedback for tool rejections, improves telemetry tracking with version normalization and feedback metrics, and enhances proxy support with client certificates for WebSocket connections. The release also includes security refinements for Windows path validation and better session data persistence on process exit.

## 🚀 New Features

### Tool Rejection Feedback
**What:** Users can now provide feedback text when rejecting a tool use, telling Claude what to do differently.

**How to use:**
When Claude requests permission to use a tool and you select "No", you'll see an input field with the placeholder "Tell Claude what to do differently". Your feedback is sent to Claude to guide its next action.

**Details:**
- Input field appears in tool permission prompts when rejecting
- Feedback is optional - you can still reject without providing a message
- Claude receives your feedback with context: "The user doesn't want to proceed with this tool use... To tell you how to proceed, the user said: [your message]"
- Telemetry tracks whether feedback was provided via new `hasFeedback` field
- **Evidence**: `FKA` constant at line 474090, `FJQ()` component at line 263860, `kd()` telemetry function at line 352977

### Tool Input Examples Beta (tool-examples-2025-10-29)
**What:** New beta feature enabling tool definitions to include example inputs.

**How to use:**
This feature is automatically enabled for first-party deployments when the `tool_use_examples` feature flag is active. Tool definitions can now include an `input_examples` field that gets passed to the Anthropic API.

**Details:**
- Beta flag: `tool-examples-2025-10-29`
- Only active when `tool_use_examples` feature flag is enabled
- Restricted to first-party deployments
- Helps Claude better understand tool usage through few-shot style examples
- **Evidence**: `dBQ` constant at line 216168, feature check in `FP1()` at line 216221-216222, implementation in `_aA()` at line 320476-320477

### Permission Bypass Notifications
**What:** User-visible notifications when bypass permissions mode is disabled by organization policy or settings.

**How to use:**
If you attempt to use `--dangerously-skip-permissions` or configure bypass permissions mode, and it's disabled by your organization or settings, you'll now see a high-priority notification explaining why.

**Details:**
- Two notification messages:
  - "Bypass permissions mode was disabled by your organization policy"
  - "Bypass permissions mode was disabled by settings"
- Notifications appear in the UI notification queue with high priority
- Previously only logged to console; now user-visible
- **Evidence**: `xs2()` function at line 472394, notification messages at lines 472411 and 472414, queue integration at lines 492477-492488

### Client Certificate Support for WebSocket Proxies
**What:** WebSocket connections now support HTTPS proxies with client certificate authentication (mTLS).

**How to use:**
Configure client certificates via environment variables:
```bash
export CLAUDE_CODE_CLIENT_CERT=/path/to/cert.pem
export CLAUDE_CODE_CLIENT_KEY=/path/to/key.pem
export CLAUDE_CODE_CLIENT_KEY_PASSPHRASE=optional_passphrase
```

**Details:**
- New `CFA()` function creates per-request proxy agents with certificate support
- Applies to both API requests and WebSocket connections
- Respects proxy bypass rules on a per-URL basis
- Replaces global proxy agent pattern with per-connection agents
- **Evidence**: `CFA()` function at line 151929, WebSocket usage at line 488707, API usage at lines 483464 and 483483

## ✨ Improvements

### Enhanced Telemetry System

**Version Base Tracking:**
- New `version_base` telemetry field normalizes version strings (e.g., "2.0.37-beta" → "2.0.37")
- Enables cleaner analytics aggregation across pre-release versions
- **Evidence**: `Jo5()` function at line 449429, `versionBase` mapping at line 449396

**Improved Batch Configuration:**
- Telemetry export interval increased from 5 seconds to 20 seconds (4x longer)
- New batch size limit of 200 events per export
- Remote configuration support via `tengu_1p_event_batch_config` dynamic config
- Reduces network overhead and improves performance
- **Evidence**: `xBI = 20000` and `vBI = 200` at lines 478225-478226, dynamic config in `er2()` at lines 478169-478173

**Rejection Feedback Tracking:**
- New `hasFeedback` field tracks whether users provided feedback when rejecting tools
- Enables analysis of feature adoption and user engagement
- **Evidence**: `QZ()` function at line 352406, `hasFeedback` parameter at lines 1000-1002

### Session Persistence Improvements

**Graceful Shutdown:**
- Session data now flushes completely before process exit
- Prevents data loss from in-flight writes during termination
- Write tracking system counts pending operations
- Process exit hook calls `flush()` to wait for completion
- **Evidence**: `flush()` method at line 474250, cleanup registration in `mw()` at lines 474210-474212, `trackWrite()` wrapper at line 474242

### Expanded Installation Check Control

**DISABLE_INSTALLATION_CHECKS Scope:**
- Environment variable now also disables install method mismatch warnings
- Skips checks for npm-local vs config mismatch and native vs config mismatch
- Previously only disabled some checks; now more comprehensive
- **Evidence**: Conditional check wrapping at line 373886 in `mZ5()` function

## 🔧 Other Changes

### Windows Path Security Refinement

**Simplified UNC Path Detection:**
The Windows UNC path detection was simplified from 8 security checks down to 1 basic pattern check. The new implementation removes specific checks for:
- IPv4 address-based UNC paths (e.g., `\\192.168.1.1\share`)
- IPv6 address-based UNC paths (e.g., `\\[fe80::1]\share`)
- WebDAV `DavWWWRoot` patterns
- SSL/port patterns like `@SSL@8080`

File operations no longer check for UNC paths at all, while bash command execution retains basic UNC path blocking. The security impact is reduced coverage for IP-based UNC paths and WebDAV-specific attacks.

**Evidence**: Old `mB1()` function at line 469909 (v2.0.36), new `i2Q()` function at line 222404, file path validation `Cr2()` at line 474880

### Proxy Bypass Architecture

Proxy bypass logic moved from axios interceptors to per-request agent creation via the new `CFA()` function, providing cleaner separation of concerns and more granular control.

**Evidence**: `CFA()` function at line 151929, proxy bypass check `QbA()` integration

---

**Note:** Line numbers reference `/home/shcv/projects/claude-investigations/archive/claude-code/pretty/pretty-v2.0.37.js` unless otherwise specified.
