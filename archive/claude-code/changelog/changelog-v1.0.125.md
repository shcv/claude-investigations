# Changelog for version 1.0.125

## Highlights
Version 1.0.125 enhances sandbox security and usability with selective command exemptions, improved macOS compatibility for temp folder access, better npm installation detection, and real-time visibility into blocked operations.


### Sandbox Command Exemptions
**What:** Configure specific commands to always bypass the sandbox, even when sandbox mode is enabled.

**How to use:**
Add an `unsandboxedCommands` array to your sandbox configuration in `.clauderc`:
```json
{
  "sandbox": {
    "unsandboxedCommands": ["git", "docker", "gcloud", "aws"]
  }
}
```

**Details:**
- Commands in this list will never run in the sandbox environment
- Matching uses smart logic: matches both exact command names and commands with arguments (e.g., `"git"` matches both `git` and `git push`)
- Useful for commands that require unrestricted filesystem or socket access
- Bypasses sandbox restrictions while still enforcing permission checks
- **Evidence**: `qu2()` at line 383844, schema at line 363385, integration in `Eu2()` at line 383855


### Resume Session at Specific Message
**What:** Resume a conversation from a specific assistant message instead of from the end.

**How to use:**
```bash
claude --resume conversation.jsonl --resume-session-at msg_abc123
```

**Details:**
- Requires `--resume` flag to be set
- Provide an assistant message ID to start from that point in the conversation
- Returns error if the specified message ID is not found
- Useful for branching conversations or exploring alternative response paths
- **Evidence**: Validation at line 446036, message filtering at line 446470, configuration at line 448508


### Sandbox Violation Notifications
**What:** Real-time status bar notifications when the sandbox blocks operations.

**How it works:**
- Displays "⧈ Sandbox blocked N operation(s) (ctrl+s to see logs)" in the status bar
- Shows count of newly blocked operations
- Auto-hides after 5 seconds
- Press Ctrl+S to view detailed violation logs

**Details:**
- Only appears when sandboxing is enabled
- Provides immediate feedback without interrupting workflow
- Helps diagnose permission issues during development
- Uses existing sandbox violation store infrastructure (added in v1.0.122)
- **Evidence**: `bMB()` component at line 428661, rendered at line 428869


### macOS Temp Folder Sandbox Support
**What:** Automatic sandbox permissions for macOS system temp directories.

**Details:**
- Detects macOS temp folders at `/var/folders/XX/YYYYYYYY/T/`
- Automatically allows write access to detected temp directories
- Handles both `/var/folders/` and `/private/var/folders/` paths (symlink variants)
- Enables seamless screenshot workflows where macOS saves screenshots to temp folders
- No user configuration required - works automatically when `TMPDIR` environment variable is set
- **Evidence**: `y19()` detection function at line 363940, integrated into `j19()` at line 363726


### Localhost Binding Control
**What:** New sandbox configuration option to allow processes to bind to localhost network addresses.

**How to use:**
```json
{
  "sandbox": {
    "network": {
      "allowLocalBinding": true
    }
  }
}
```

**Details:**
- Defaults to `false` for security
- When enabled, allows sandboxed processes to:
  - Bind to localhost ports
  - Accept inbound connections on localhost
  - Make outbound connections to localhost
- Useful for development servers, local APIs, and inter-process communication
- Only affects localhost (`127.0.0.1`), not external network access
- **Evidence**: Schema at line 363371, `getAllowLocalBinding()` export at line 364464, sandbox profile generation at line 363908


### Better npm Global Installation Detection
**What:** Enhanced detection of npm global installations using `npm config get prefix`.

**Details:**
- Adds synchronous `npm config get prefix` command execution as a fallback
- Detects npm installations in custom prefix locations
- More reliable than hardcoded path matching alone
- Handles non-standard npm configurations
- Improves accuracy of installation type reporting and upgrade suggestions
- **Evidence**: `G$()` function at line 375878, specifically lines 375897-375898


### CLAUDE.md Flat Display Mode (Infrastructure)
**What:** Alternative compact display format for CLAUDE.md sources.

**Details:**
- Adds `flat` parameter to CLAUDE.md display component
- When enabled, shows entries inline: `user (.claude/CLAUDE.md), project (CLAUDE.md)`
- Traditional vertical tree view preserved as default
- Infrastructure added but not yet activated in UI
- Prepares for future compact display options in constrained spaces
- **Evidence**: `n$0({ context, flat })` at line 402096, flat rendering at lines 402107-402123


### Removed Sandbox Bypass Shortcut
**What:** Eliminated ability to bypass permission checks via sandbox flag.

**Details:**
- Previous versions allowed `sandbox: true` parameter to skip all permission validation
- This escape hatch has been removed for security
- All commands now go through proper read-only and permission validation
- Tightens sandbox security by closing potential bypass mechanism
- **Evidence**: Code removed from `Uj2()` at line 380133 in v1.0.124, absent in `Lj2()` at line 380187 in v1.0.125

## Internal Changes

The following changes are primarily internal refactoring with minimal user impact:

- Added `cwd` import from `node:process` (line 357186)
- Added `Mi4()` helper function (line 377386)
- Added context provider `fj7` for React components (line 402093)
- Multiple module reorganizations and minifier renamings
- Removed unused stream and process imports


**Note**: Line numbers reference the prettified v1.0.125.js source file for verification purposes.
