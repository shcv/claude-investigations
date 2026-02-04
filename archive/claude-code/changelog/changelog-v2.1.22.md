# Changelog for version 2.1.22


## Summary

This is a maintenance release with no user-facing changes. The update consists solely of version number increments and build metadata updates.

## Analysis

After thorough examination of the diff between v2.1.21 and v2.1.22, all changes fall into these categories:

1. **Version string updates**: All instances of `VERSION: "2.1.21"` changed to `VERSION: "2.1.22"`
2. **Build timestamp updates**: `BUILD_TIME` changed from `"2026-01-28T01:36:50Z"` to `"2026-01-28T06:33:34Z"`
3. **Build path updates**: Internal build paths updated from `claude-cli-external-build-2146` to `claude-cli-external-build-2154`

There is one minor code change at lines 694-707 in the diff:

```javascript
// Added line:
(_A = null),

// Modified condition:
// Old: if (!HA || e.length === 0)
// New: if (!HA || (e.length === 0 && !_A))
```

**Evidence**: Query handler at approximately line 528104-528305 (API request streaming logic)

This appears to be an internal state management fix related to the API query handling—specifically ensuring a variable `_A` is reset and checked during stream event processing. This is an internal implementation detail with no direct user-facing impact.

## Notes

This release was built approximately 5 hours after v2.1.21 (01:36 → 06:33 UTC on 2026-01-28), suggesting it may be a quick follow-up fix or scheduled rebuild. The internal code change to the streaming logic may address an edge case in API response handling, but without additional context (such as a related bug report), the specific issue being addressed cannot be determined from the diff alone.
