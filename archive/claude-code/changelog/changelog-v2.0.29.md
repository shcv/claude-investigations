# Changelog for version 2.0.29

## Highlights
Version 2.0.29 optimizes the trust validation system to respect the global bypass permissions setting, reducing unnecessary directory traversal when users have already accepted bypass permissions mode.

### Enhanced Trust Validation Logic
**What:** The workspace trust check now respects the global bypass permissions setting more efficiently. When users have accepted bypass permissions mode (via `--dangerously-skip-permissions` or `--allow-dangerously-skip-permissions` flags), the trust validation immediately returns true without checking individual directory trust settings.

**How it works:**
```bash
# Enable bypass permissions mode (shows one-time warning dialog)
claude --dangerously-skip-permissions

# Or make it available as an option
claude --allow-dangerously-skip-permissions
```

**Details:**
- Previously, bypass permissions mode existed but trust checks were independent operations
- Now, accepting bypass permissions mode acts as a global trust override for all workspace trust dialogs
- Eliminates redundant directory traversal when bypass mode is already active
- The bypass permissions feature requires explicit user consent via an interactive warning dialog
- Designed for sandboxed/containerized environments with restricted internet access
- **Evidence**: Enhanced check in `rJ()` at line 468251 in v2.0.29

**Technical changes:**
- Added early-return check for `bypassPermissionsModeAccepted` flag before performing directory-specific trust validation
- Reduces unnecessary computation when global bypass is enabled
- No change to the security model—only optimization of the existing trust system

### Import Statement Refactoring
Modernized Node.js module imports to use more specific named imports instead of default imports, improving code clarity and enabling better tree-shaking:

- `stream` module: Changed to named import of `PassThrough`
- `node:child_process`: Changed to named imports of `execSync` and `spawn`
- `node:os`: Changed to named import of `homedir`
- `node:process`: Changed to named import of `cwd`

These changes have no user-visible impact but improve code maintainability and bundle optimization.
