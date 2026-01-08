# Changelog for version 2.1.1


## Summary

This is a patch release that fixes a potential crash when loading release notes from a corrupted or unreadable changelog cache file.

## Bug Fixes

- Fixed crash when changelog cache file is corrupted or unreadable. The release notes loader (`de2()` at line 460474) now catches exceptions during changelog parsing and gracefully returns an empty result instead of crashing. This prevents startup failures when the `~/.claude/cache/changelog.md` file is malformed.

**Evidence**: `de2()` at line 460474 (release notes loader, reads from `"cache", "changelog.md"`)

**Before (v2.1.0)**:
```javascript
function de2(A) {
  let Q = k6A();
  if (!Q) return [];
  let B = eH1(Q),  // Could throw if file is corrupted
    G = [],
    ...
}
```

**After (v2.1.1)**:
```javascript
function de2(A) {
  let Q = k6A();
  if (!Q) return [];
  let B;
  try {
    B = eH1(Q);
  } catch {
    return [];  // Gracefully handle corrupted changelog
  }
  let G = [],
  ...
}
```
