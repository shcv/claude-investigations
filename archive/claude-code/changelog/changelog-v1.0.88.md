# Changelog for version 1.0.88

## Highlights
Version 1.0.88 fixes a cache management issue that could cause stale authentication states and inconsistent feature access after login/logout operations. This maintenance release improves the reliability of account switching and feature flag updates.

### Fixed: Authentication cache inconsistency during login/logout
- **Issue:** Beta feature flags were not being properly cleared during authentication changes, potentially causing users to see incorrect features after logging in/out or switching accounts
- **Cause:** Only one of three related beta feature caches was being cleared, leaving stale data in the other two caches
- **Resolution:** Added a new `oV1()` function that clears all three beta feature caches (`_p1`, `Aw`, and `xp1`) during login and logout operations
- **Affected versions:** 1.0.87 and earlier
- **Impact:** Users should no longer experience issues where:
  - Features remain accessible after logging out
  - Features don't appear after logging into an entitled account
  - Stale feature states persist when switching between accounts
