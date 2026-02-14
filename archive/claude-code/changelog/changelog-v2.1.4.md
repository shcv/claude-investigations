# Changelog for version 2.1.4


## Summary

This is a minor maintenance release that adds a new environment variable to disable background tasks and improves OAuth authentication reliability with automatic token refresh on 401 errors. The changes are primarily internal with one user-configurable option.


### Environment Variable to Disable Background Tasks

What: New `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` environment variable allows disabling the background task functionality.

Usage:
```bash
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1
claude
```

Details:
- When set, the `run_in_background` parameter documentation is hidden from tool descriptions
- The `ctrl+b` shortcut to background a task is disabled
- Background agent execution via `run_in_background` parameter is disabled
- Useful for environments where background task management is not desired or causes issues

Evidence: `Go8()` at line 280507 (background task doc generator, checks `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS`); `ifA` at line 447674 (Task agent parameter schema, gated by same env var)


### OAuth 401 Automatic Retry

Improved authentication reliability by automatically refreshing OAuth tokens when a 401 Unauthorized response is received from the API.

Details:
- When an API request fails with 401, the system now automatically refreshes the access token and retries the request
- Reduces authentication failures during long sessions where tokens may expire
- Telemetry event `tengu_grove_oauth_401_received` tracks when this occurs

Evidence: `GY1()` at line 317361 (OAuth retry wrapper, emits `"tengu_grove_oauth_401_received"` telemetry)

## Notes

- Build time updated from `2026-01-09T21:05:14Z` to `2026-01-10T22:23:05Z`
- High structural similarity (99.9%) indicates this is a minor patch release with targeted changes
