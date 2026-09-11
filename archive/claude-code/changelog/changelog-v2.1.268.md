# Changelog for version 2.1.268

## Summary

This release adds two administrator/operator controls: stricter Cloud gateway sign-in scoping for managed deployments, and optional cleanup of completed self-hosted runner sessions. It also improves plugin reload flow and gives Claude substantially more actionable diagnostics when Chrome browser-tool calls fail.

## New Features


### Restrict Cloud gateway login to declared internal networks

What: Administrators can limit managed Cloud gateway sign-in to specific public IPv4 CIDR blocks with the new `gatewayInternalNetworks` setting.

Usage:

```json
{
  "gatewayInternalNetworks": ["203.0.113.0/24"]
}
```

Details:

- This setting is honored only from administrator-controlled managed settings, policy helpers, or MDM; user, project, and remotely delivered settings cannot enable it.
- `/login` accepts a gateway in a declared block only over a direct connection when the machine itself is also in that block.
- The setting accepts up to four non-overlapping `/8`–`/32` public IPv4 CIDRs. Private ranges, proxies, VPN pools, NAT segments, and invalid values are refused.
- An invalid managed value now prevents the governed gateway sign-in rather than being silently accepted.

Evidence: Managed setting `gatewayInternalNetworks` (search for `"gatewayInternalNetworks"` and `"gateway login: invalid gatewayInternalNetworks"`).


### Optional self-hosted runner session-state cleanup

What: Self-hosted runner operators can now remove a completed session’s runner-local state automatically.

Usage:

```bash
claude self-hosted-runner --remove-session-state
```

Or set:

```bash
SELF_HOSTED_RUNNER_REMOVE_SESSION_STATE=1 claude self-hosted-runner
```

Details:

- Cleanup removes the session’s local Claude configuration, transcript copy, shell snapshots, session environment, file history, debug log, staged uploads, per-session Git configuration, and session work directory beneath the runner base directory.
- The option is best-effort: a runner killed before cleanup can leave state behind, and canonical clones or files written outside the session state are not removed.
- It defaults to off, preserving the previous behavior. Operators who retain debug logs should copy them in a post-session hook before enabling cleanup.

Evidence: New `--remove-session-state` option and `SELF_HOSTED_RUNNER_REMOVE_SESSION_STATE` environment variable (search for `"Remove a session's per-session state"`).


## Improvements


### Plugin changes can queue a reload after the current response

What: Changes made through the plugin UI can queue `/reload-plugins` automatically once the current response finishes, instead of requiring the user to manually run it afterward.

Details:

- The queued command avoids changing the active tool list in the middle of a response.
- **[Gradual Rollout]** This behavior is gated by `tengu_plugin_menu_close_reload`.

Evidence: Plugin notification `"Plugin changes apply when the current response finishes (/reload-plugins is queued)."` and feature flag `tengu_plugin_menu_close_reload`.


### More useful Chrome browser-tool failure messages

What: Claude now distinguishes several Chrome-extension failure modes and recommends safer recovery steps.

Details:

- A call that never reached Chrome identifies an offline/asleep computer or closed Chrome, rather than suggesting a permissions issue.
- A timeout explains that the page may be loading, unresponsive, or awaiting an extension-side-panel permission prompt, and suggests a lighter operation such as `get_page_text`.
- A superseded call warns that the action may already have occurred and recommends checking page state before retrying.
- Mid-operation extension disconnects are identified as typically transient and safe to retry after a short delay.

Evidence: Chrome tool diagnostic `"call was never delivered to the Chrome extension"` and state-check recommendation `"get_page_text"`.


### Stronger validation for managed sandbox AWS credential rewriting

What: Managed sandbox configuration now validates explicit AWS credential-pair definitions used for SigV4 re-signing.

Details:

- Each declared AWS credential variable must correspond to a whole-value masked `credentials.envVars` entry.
- A variable cannot appear in more than one credential-pair slot.
- Configurations using extraction or decoding for a paired value are rejected because the signer requires the complete real credential value.

Evidence: Validation message `"does not reference a credentials.envVars entry with mode \"mask\""` and setting `awsPairs`.


Generated with:
- tool: `harness-investigations@5a7f523-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.268.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.268.txt`
- source modules: `archive/claude-code/original/cli-v2.1.268.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
