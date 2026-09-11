# Changelog for version 2.1.257

## Summary

This release adds Fable 5.1 and Mythos 5.1 model support, project-directory syncing for cloud sessions, and controls for preserving a system prompt across resumes. It also adds stricter optional read boundaries and configurable clock formatting in the terminal UI.

## New Features


### Fable 5.1 and Mythos 5.1 model support

What: Claude Code recognizes the new `claude-fable-5-1` and `claude-mythos-5-1` models.

Usage:

```bash
claude --model claude-fable-5-1
```

Details:

- Fable 5.1 becomes the default `fable` alias where the provider supports it.
- Mythos 5.1 is available as a first-party model identifier.
- Model availability still depends on your account, organization policy, and configured provider.

Evidence: Built-in catalog entries for `"Claude Fable 5.1"` and `"Claude Mythos 5.1"` (search for `"claude-fable-5-1"`).


### Cloud-session project sync

What: Remote-control sessions can ask to sync the current project directory into a cloud session so Claude can continue working there.

Usage:

```text
/remote-control
```

Details:

- When offered, choose “Yes, sync this project directory.”
- The consent text states that secrets, credentials, and gitignored files are excluded, and synced files are encrypted at rest.
- Changes made in the cloud are not automatically copied back to the local computer; the session reports work that could not reach the machine.

Evidence: Remote sync consent dialog (search for `"Sync this project directory to the cloud?"` and `"Allow Claude Code to sync files from this project directory into cloud sessions"`).


### System-prompt snapshots

What: You can explicitly control whether Claude Code records a system prompt once per conversation and reuses it on requests and resumes.

Usage:

```bash
claude --system-prompt-snapshot on
```

Details:

- `on` preserves the prompt snapshot for the conversation.
- `off` disables snapshotting.
- The built-in prompt defaults to snapshotting; supplying `--system-prompt` or `--append-system-prompt` otherwise makes the prompt apply freshly at launch.

Evidence: CLI option description (search for `"--system-prompt-snapshot <on|off>"`).


### Optional block on reads outside working directories

What: A new permissions setting can refuse Read, Grep, Glob, and LSP reads outside the session’s working directories.

Usage:

```json
{
  "permissions": {
    "blockReadsOutsideWorkingDirectories": true
  }
}
```

Details:

- Claude Code prompts users to add a needed path with `/add-dir` or remove the setting.
- The setting applies across permission modes; a `true` value from any settings source wins.
- Shell commands whose paths cannot be safely analyzed fail closed by asking rather than silently reading outside the boundary.

Evidence: Setting documentation (search for `"Refuse file-tool reads (Read, Grep, Glob, LSP) outside the working directories"`).


### Configurable terminal clock format and time zone

What: Two settings now control how times appear in the Claude Code UI.

Usage:

```json
{
  "timeFormat": "24-hour-utc",
  "timeZone": "UTC"
}
```

Details:

- `timeFormat` accepts `auto`, `12-hour`, `24-hour`, `24-hour-utc`, or a strftime-style format such as `%H:%M`.
- `timeZone` accepts an IANA zone such as `UTC` or `Europe/Dublin`; unknown values fall back to the system time zone.

Evidence: Settings help (search for `"Clock format for times shown in the UI"` and `"IANA time zone for times shown in the UI"`).


Generated with:
- tool: `harness-investigations@5a7f523-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.257.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.257.txt`
- source modules: `archive/claude-code/original/cli-v2.1.257.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
