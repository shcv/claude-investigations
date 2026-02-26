# Changelog for version 2.1.58


## Summary

A small maintenance release focused on infrastructure improvements. The main user-facing change is improved Windows path support when adding marketplace sources. Behind the scenes, the bridge polling mechanism for remote sessions has been reworked to be server-configurable.

### Windows path support for marketplace sources

What: On Windows, you can now use native Windows-style paths (backslash separators and drive letters) when adding a marketplace source via the interactive UI or CLI.

Usage:
```bash
# These now work on Windows (in addition to Unix-style paths):
claude marketplace add .\my-skills
claude marketplace add ..\shared-skills
claude marketplace add C:\Users\me\skills
```

Details:
- Adds recognition of `.\`, `..\`, and drive-letter paths (e.g., `C:\`) when `process.platform` is `"win32"`
- Unix-style paths (`./`, `../`, `/`, `~`) continue to work on all platforms
- The resolved path must point to a directory or a `.json` file (e.g., `marketplace.json`)

Evidence: Marketplace source parser (search for `startsWith(".\\")` and `[a-zA-Z]:[/\\]`) — `$v1()` at line ~472168


### Optimized bridge polling for remote sessions

What: The polling interval for the bridge connection (used in remote/cloud sessions) is now dynamically configurable from the server rather than being hardcoded.

Details:
- Poll interval is now controlled by the `tengu_bridge_poll_interval_ms` feature flag, with a default of 1000ms and a floor of 100ms
- The flag value is cached and refreshed every 5 minutes (300,000ms TTL)
- The `block_ms` parameter was removed from work-poll requests, simplifying the client-server protocol
- These changes allow Anthropic to tune remote session responsiveness server-side without requiring client updates

Evidence: New cached config reader `KL1()` at line ~532330 (search for `"tengu_bridge_poll_interval_ms"`)


### Updated Haiku model descriptions

What: The model picker descriptions for Haiku were reorganized internally. Both Haiku 3.5 and Haiku 4.5 remain available; the user-facing text ("Haiku 4.5 · Fastest for quick answers" and "Haiku 3.5 for simple tasks") is unchanged.

Evidence: Model option functions at lines ~530549 and ~530558 (search for `"Fastest for quick answers"`)

## Notes

This release also modernizes internal import style across the codebase, switching from default imports to named/destructured imports for Node.js built-in modules (`child_process`, `crypto`, `node:fs`, `node:path`, etc.). This is a purely internal refactoring with no behavior change.
