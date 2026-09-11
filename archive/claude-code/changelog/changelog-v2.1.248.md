# Changelog for version 2.1.248

## Summary

This release adds a fully enabled `--restricted` mode to confine Claude Code’s file access to the working directory. It also ships gated infrastructure for keeping a local checkout synchronized with a cloud session, plus a once-weekly session-limit reset that is not yet broadly enabled.

## New Features

### Restricted CLI mode

What: Run Claude Code with `--restricted` to prevent its file tools and attachments from accessing paths outside the working directory.

Usage:

```bash
claude --restricted
```

Details:

- Requests targeting paths outside the working directory are denied.
- Attachments outside that directory are rejected.
- Restricted mode cannot be used for cloud, remote-environment, or SSH sessions, because those environments cannot enforce the local path boundary.
- Cloud sessions also cannot be created from a restricted session.

Evidence: Restricted-path enforcement (search for `"--restricted confines the file tools to the working directory"` and `"Cloud sessions cannot be created from a --restricted session"`).


### Artifact working-copy synchronization

What: Claude can now synchronize a local working copy of an already-published Artifact page: pushing local edits live and pulling collaborators’ changes back into the file.

Usage: Ask Claude to sync an Artifact working copy after editing the associated local file.

Details:

- Sync targets an existing published Artifact page.
- The push makes local edits live immediately.
- The operation also pulls changes made by others into the local working copy.
- This is an Artifact-tool capability, not a standalone terminal subcommand.

Evidence: New Artifact `sync` action (search for `"Push the edits made to the working copy of an already-published artifact page to the page"`).


## Improvements

### Auto mode now clearly conflicts with Fast mode

Auto mode now reports that it is unavailable while Fast mode is enabled and tells users how to resolve the conflict.

Evidence: Fast-mode guard (search for `"auto mode unavailable while fast mode is on · run /fast off"`).


## In Development

Features with infrastructure added but not yet enabled. These are shipped dark and may become available in future versions.


### Cloud-session directory synchronization [In Development]

What: A cloud session can receive a synchronized copy of the local project and return changes to the local checkout.

Status: Feature-flagged

Details:

- Claude Code can offer a `container_sync` mode for eligible Git repositories.
- It tracks upload, download, conflict, oversized-checkout, and unavailable-service states, with explicit messages when files are not current.
- The implementation is gated by the server-controlled `tengu_violin_wood` flag; when the flag is off, file sync is not offered.
- `CLAUDE_CODE_DIR_SYNC_ENGINE` can disable sync locally; `none` turns it off for that machine.

Evidence: Directory-sync gate and mode (search for `"tengu_violin_wood"`, `"container_sync"`, and `"CLAUDE_CODE_DIR_SYNC_ENGINE"`).


### Session-limit reset [In Development]

What: Eligible users can reset their current session limit and continue working once per week, while still consuming their weekly allowance.

Usage:

```text
/limit-reset
```

Status: Feature-flagged

Details:

- The command is hidden unless the account is eligible and the server configuration enables it.
- A successful reset reports the next available reset date and preserves the weekly limit.

Evidence: Hidden `limit-reset` command (search for `"Reset your session limit now"` and `"tengu_nifty_lemur"`).

## Notes

- `--restricted` is intended for local CLI use; it cannot be enforced in cloud, remote-environment, or SSH sessions.


Generated with:
- tool: `harness-investigations@1a8fc5b-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.248.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.248.txt`
- source modules: `archive/claude-code/original/cli-v2.1.248.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
