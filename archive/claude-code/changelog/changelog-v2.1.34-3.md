# Changelog for version 2.1.34


## Summary

This is a minor maintenance release with internal improvements to telemetry tracking and code organization. There are no new user-facing features in this version.


### Enhanced Telemetry with Rate Limit Tier Tracking

The analytics system now captures the user's rate limit tier alongside existing subscription information. This provides Anthropic with better visibility into usage patterns across different account types.

Evidence: Rate limit tier addition to analytics payload (search for `"rateLimitTier"`)


### Refactored Inbox Polling Logic

The inbox polling system (used for processing queued messages when the session becomes available) has been refactored to accept an explicit `enabled` parameter. This improves control flow by allowing the polling behavior to be conditionally disabled rather than relying on implicit checks throughout the function.

Evidence: Inbox poller function signature change — `ijq()` at line ~547956 (search for `"[InboxPoller]"`)


### Sandboxed Bash Auto-Allow Refinement

The logic for automatically allowing Bash commands when sandboxing is enabled now includes an additional validation check. This ensures the auto-allow behavior only applies when specific conditions are met.

Evidence: Auto-allow condition tightening — `b3z()` at line ~514497 (search for `"isAutoAllowBashIfSandboxedEnabled"`)

## Bug Fixes

None identified in this release.

## Notes

This release contains primarily internal refactoring and telemetry improvements. Users should not notice any behavioral changes. The structural similarity between versions is 99.9%, indicating minimal code changes.
