# Changelog for version 2.1.49


## Summary

This is a minor maintenance release that temporarily disables HTTP hooks functionality. Users who have configured HTTP hooks in their Claude Code settings will see those hooks return "not yet supported" instead of executing. Bash hooks remain fully functional.

### HTTP Hooks Temporarily Disabled

What: HTTP hooks defined in your configuration will no longer execute. Instead, they return immediately with a "HTTP hooks are not yet supported" message.

Impact:
- If you have configured HTTP hooks (using `type: "http"` in your hooks configuration), they will not execute in this version
- The hook will be skipped rather than failing the operation—your workflow will continue without the HTTP call
- Bash hooks (`type: "bash"`) continue to work normally

Example log output when an HTTP hook is encountered:
```
Hooks: skipping HTTP hook https://example.com/hook — HTTP hooks are not yet supported
```

Workaround: If you rely on HTTP hooks, you can convert them to bash hooks that use `curl` to make the HTTP request:

```json
{
  "type": "bash",
  "command": "curl -X POST -H 'Content-Type: application/json' -d '$HOOK_PAYLOAD' https://example.com/hook"
}
```

Evidence: Hook execution skips HTTP hooks with message (search for `"HTTP hooks are not yet supported"`)

## Notes

This appears to be a temporary change—the HTTP hook schema and configuration parsing remain intact, only the execution is disabled. The previous implementation supported POST requests with configurable headers and environment variable substitution in header values. This functionality may return in a future release once stability or security concerns are addressed.
