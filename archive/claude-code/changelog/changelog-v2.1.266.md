# Changelog for version 2.1.266

## Summary

This is a narrowly focused maintenance release. The only verified user-facing change simplifies the sign-in error shown when Cloud gateway authentication is unavailable.

## Improvements


### Clearer Cloud gateway sign-in guidance

When Claude Code cannot authenticate to the Cloud gateway, it now tells you to sign in with `/login` without also suggesting manual gateway environment-variable setup.

Usage:

```bash
/login
```

Details:

- The error now reads: `Not signed in to the Cloud gateway — run /login.`
- `CLAUDE_CODE_USE_GATEWAY`, `ANTHROPIC_BASE_URL`, and `ANTHROPIC_AUTH_TOKEN` configuration remains supported and is still separately validated.
- No new commands, flags, or settings were added in this release.

Evidence: Cloud gateway authentication error (search for `"Not signed in to the Cloud gateway — run /login."`); gateway configuration validation remains present (search for `"CLAUDE_CODE_USE_GATEWAY is set but"`).

## Notes

No migration is required.


Generated with:
- tool: `harness-investigations@5a7f523-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.266.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.266.txt`
- source modules: `archive/claude-code/original/cli-v2.1.266.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
