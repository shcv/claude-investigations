# Changelog for version 2.1.28

## Summary

Version 2.1.28 is a maintenance release with one internal refactoring change: the removal of the `saved_hook_context` session persistence layer. No new features, commands, flags, settings, or feature flags were added. The 252,000-line diff is almost entirely minifier variable renaming.

### Simplified Hook Context Session Persistence

The internal mechanism for persisting hook additional context to session logs has been simplified. Previously, `hook_additional_context` attachment messages were serialized into a special `saved_hook_context` format when writing to the session log, then deserialized back when loading a session. This intermediate format has been removed; hook context messages now follow the same persistence path as all other messages.

As part of this change, the message filter applied before saving was also simplified. For non-Anthropic internal users, all attachment-type messages (including hook additional context) are now filtered out before being written to the session log. Previously, hook additional context was explicitly preserved while other attachment types were filtered.

In practice, this means hook context injected by hooks (e.g., from `SessionStart`, `PreToolUse`, `PostToolUse` hooks) is no longer persisted across session resume for external users. This is unlikely to affect most users, as hook context is primarily relevant within a single session.

Evidence: Removal of `saved_hook_context` serialization layer (search for `"saved_hook_context"` in v2.1.27 -- absent from v2.1.28). Message filter simplification visible in the function that previously checked `q.attachment.type === "hook_additional_context"` (search for `"hook_additional_context"` in the session persistence area around line ~513044 in v2.1.28).

## Notes

**Build Information:**
- Version: 2.1.27 -> 2.1.28
- Build Time: 2026-01-30T19:50:44Z -> 2026-01-31T18:41:01Z
- Build Number: 2130 -> 2223

**Technical Details:**

The diff consists of:
1. Version string and build timestamp updates
2. Removal of `saved_hook_context` save/load code (~64 net lines removed)
3. Approximately 52,000 lines of minifier variable/function identifier renames

No new `tengu_*` feature flags, `CLAUDE_CODE_*` environment variables, `.describe()` settings, slash commands, CLI flags, or user-facing string literals were added. Users upgrading from 2.1.27 to 2.1.28 will experience no observable behavioral differences in normal usage.
