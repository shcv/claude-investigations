# Changelog for version 2.1.37


## Summary

This is a maintenance release with internal performance optimizations for Fast mode. There are no user-facing feature changes.

### Fast Mode Status Caching

The fast mode status check now caches results for 30 seconds to reduce redundant API calls. When you rapidly toggle fast mode or navigate between sessions, the CLI will reuse recent status checks rather than querying the server each time.

**Evidence**: Prefetch debouncing with 30-second interval (search for `"Skipping penguin mode prefetch, fetched recently"`)

### Fast Mode Command Responsiveness

The `/fast` command now includes a 300ms timeout for the status prefetch, ensuring the command remains responsive even when the API is slow.

**Evidence**: Timeout with telemetry tracking (search for `"tengu_fast_mode_prefetch_timeout"`)
