# Changelog for version 2.1.55


## Summary

This is a small maintenance release focused on internal reliability improvements. File operations have been simplified to remove overly restrictive `O_NOFOLLOW` flags that could cause issues on setups with symbolic links, and session ID generation has been streamlined to use UUID-based identifiers.

### Simplified file open operations for better symlink compatibility

File operations for log files and session tracking previously used low-level POSIX flags including `O_NOFOLLOW`, which prevents opening files through symbolic links. This has been replaced with standard file mode strings (`"a"` for append, `"w"` for write). Users whose `~/.claude` directory or log paths involve symbolic links (e.g., pointing to a different disk or partition) should experience fewer file operation errors.

Evidence: Removal of `O_NOFOLLOW` flag usage — previously set via `R46.O_NOFOLLOW ?? 0` in the old version; zero occurrences remain in v2.1.55. Affects the log writer class (search for `"local_bash"`) and session file creation.


### Streamlined session ID generation

Internal session identifiers (used for log files and remote agent tracking) now use UUID-based generation instead of custom random-byte character sampling. IDs are slightly shorter (6 hex characters from a UUID vs 8 base-36 characters from random bytes). Remote agent sessions now derive their ID directly from the parent session ID (search for `"remote_agent"`) rather than generating an independent random ID, which improves traceability during debugging.

Evidence: Removed charset `"0123456789abcdefghijklmnopqrstuvwxyz"` (2 of 4 instances removed), replaced with `randomUUID` substring approach (search for `replace(/-/g, "").substring(0, 6)`).

## Notes

- No new features, CLI flags, slash commands, environment variables, or feature flags were added in this release.
- No breaking changes. All improvements are backward-compatible internal refinements.
- Build number changed from 2160 to 2171.
