# Changelog for version 2.1.44


## Summary

This release improves OAuth token handling by adding automatic token recovery when tokens are revoked. Previously, users with revoked OAuth tokens would see authentication failures; now the CLI automatically detects revoked tokens and refreshes them transparently.

### Automatic Recovery from Revoked OAuth Tokens

OAuth tokens can be revoked server-side (e.g., when users revoke access from their Claude.ai account settings). Previously, this would cause authentication failures in various API calls. This release adds automatic token refresh when a revoked token is detected across multiple code paths:

- Fast mode prefetch (checking if your organization has fast mode enabled)
- Metrics opt-out status checks
- General API retry logic

The CLI now catches HTTP 403 responses containing "OAuth token has been revoked" and automatically refreshes the token before retrying the request.

Evidence: OAuth token revocation check helper (search for `"OAuth token has been revoked"`) — `GOA()` at line ~211503; token refresh function `Ju()` at line ~114161

## Notes

- Import style refactoring: Several Node.js imports changed from default imports to named imports (e.g., `import { spawn } from "child_process"` instead of `import child_process from "child_process"`). This is an internal refactoring with no user-facing impact.
- The verbose logging message "Metrics opt-out check failed: {error}" was removed; auth errors are now handled via the standard recovery flow rather than being logged separately.
