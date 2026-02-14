# Changelog for version 2.0.53

## Highlights

This is a maintenance release with internal code improvements. The primary user-facing change is improved handling of OAuth token expiration when fetching API usage data, which prevents unnecessary errors during token refresh periods.


### OAuth Token Expiration Handling for Usage Data
**What:** The API usage data fetcher now checks if the OAuth token is expiring before making API calls, gracefully falling back to cached data instead of throwing errors.

**Details:**
- Previously, the usage data fetch (`VPA()` at line 471623) would attempt API calls even with expiring tokens, potentially causing "Failed to load usage data" errors
- Now checks if token expires within 5 minutes and returns `null` immediately if so
- Falls back to cached usage data rather than displaying errors during token refresh windows
- **Evidence**: `VPA()` at line 471623-471636 in v2.0.53, new check using `W6()` (OAuth token getter at line 163812) and `Ym()` (expiration checker at line 67497)

**User impact:** Fewer transient error messages when viewing API usage near token expiration times.


### Import Statement Reorganization
The codebase underwent significant refactoring of import statements, moving from default imports to named imports for better tree-shaking and code organization. This affects ~16 import statements but has no user-facing impact.

Examples of changes:
- `import from "stream"` → `import { PassThrough } from "stream"` (line 514212)
- `import from "crypto"` → `import { createHash, randomBytes } from "crypto"` (line 323718)
- `import from "node:fs"` → `import { readFileSync, existsSync, mkdirSync, readdirSync } from "node:fs"` (line 232383)


### Variable Renaming
817 internal variable and function names were renamed as part of minification/obfuscation changes. No functional impact.


**Version Statistics:**
- Structural similarity to v2.0.52: 99.8%
- Matched declarations: 10273/10290
- Changes: 17 additions, 17 deletions, 1 modification, 817 renames
