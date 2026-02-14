# Changelog for version 2.0.2

## Highlights
Version 2.0.2 focuses on security improvements, AWS Marketplace support, and bug fixes. Key changes include new workspace trust checks for AWS credential operations, billing type detection for AWS Marketplace customers, improved error handling for API concurrency issues, and a fix for stale credential caching.


### AWS Credential Workspace Trust Checks
**What:** Added security checks to prevent AWS credential operations before workspace trust is confirmed

**Details:**
- Both `awsAuthRefresh` and `awsCredentialExport` settings now verify workspace trust before execution
- When these settings come from project or local configuration files, the system checks if the workspace has been explicitly trusted by the user
- If executed before trust confirmation, the system logs a security warning and reports telemetry
- Non-interactive sessions (`-p` mode) bypass these checks as they don't have interactive trust dialogs
- **Evidence**: Security check implementation at `oH5() at line 438469` and `tH5() at line 438512`

**Why this matters:** Prevents malicious projects from triggering AWS credential refresh or export commands that could exfiltrate credentials before the user has reviewed and trusted the workspace.


### AWS Marketplace Billing Detection
**What:** Added support for detecting AWS Marketplace billing and restricting features accordingly

**How it works:**
- The OAuth profile API now returns an `organization.billing_type` field
- This value is stored as `organizationBillingType` in the user's config
- When billing type is `"aws_marketplace"`, certain features are restricted

**Details:**
- AWS Marketplace customers are excluded from Opus model access, regardless of subscription tier
- The `VD()` function at line 438734 implements the gating logic
- Billing type is fetched from `/api/oauth/profile` and persisted across sessions
- **Evidence**: Field extraction at `pC0() at line 397362`, feature gating at `VD() at line 438734`

**Limitations:** AWS Marketplace customers cannot select the Opus model even with Pro/Max/Enterprise subscriptions.


### Tool Use Concurrency Error Handler
**What:** New error handler for API 400 errors caused by tool use concurrency issues

**How to recover:**
When you encounter this error, the system will display:
```
API Error: 400 due to tool use concurrency issues. Run /rewind to recover the conversation.
```

**Details:**
- Detects when `tool_use` IDs are found without immediately following `tool_result` blocks
- Provides clear recovery instructions using the existing `/rewind` command
- The `/rewind` command restores both code state and conversation to a previous checkpoint
- **Evidence**: Error handler at `bk1() at line 385221`

**Why this matters:** Provides users with actionable recovery steps instead of a generic API error message when tool execution gets out of sync.


### Fixed Stale Credential Cache
**What:** Removed memoization from credential storage `read()` methods to prevent stale data

**Details:**
- Previously, credentials were cached indefinitely using `t0()` wrapper (lodash memoize)
- After updating credentials, the cache could return old values
- Now every `read()` call executes fresh credential retrieval
- Affects both macOS Keychain and plaintext storage backends
- All manual `cache.clear?.()` calls were removed as they're no longer needed
- **Evidence**: Keychain changes at `ly2.read() at line 378584`, plaintext changes at `PV0.read() at line 378624`

**Why this matters:** Credential updates and deletions now work correctly without returning stale cached values that could cause authentication failures.


### Improved Session Persistence Reliability
**What:** Removed client-side duplicate UUID checking in favor of server-side validation

**Details:**
- Previously, the client would skip uploading session entries if their UUID was already fetched
- This client-side cache could become stale in multi-client scenarios
- Now all entries are uploaded, and the server handles deduplication via `Last-Uuid` headers and 409 conflict detection
- Simplifies retry logic and handles partial fetches more robustly
- **Evidence**: Function refactor from `V8B() at line 397227` to `ZPB() at line 436288`

**Why this matters:** Session persistence is more reliable when multiple processes or partial fetch operations are involved.


### Removed Rate Limit Display from Model Selection
**What:** Model selection UI no longer shows rate limit fallback status or reset times

**Details:**
- Previously displayed "(currently Sonnet)" when users were in rate-limited fallback mode
- Previously showed "Resets at [time]" information
- Function simplified from `D3B(model, fallbackActive, resetsAt)` to `xs2(model)`
- The underlying rate limit tracking (`maxRateLimitFallbackActive`) still exists but is no longer displayed in this UI
- **Evidence**: Function simplified from `D3B() at line 401267` to `xs2() at line 392676`


### Terminal Rendering Refactor
Extracted terminal resize detection logic into dedicated `p3A()` helper function at line 358129. Frame objects now track terminal dimensions (`rows`, `columns`) enabling automatic resize detection without explicit boolean parameters. No user-facing changes.


**Note:** Many variable and function names changed due to minification (approximately 8,390 renames). This is normal for bundled releases and doesn't affect functionality.
