# Changelog for version 1.0.24


### New Features

#### Tool Execution Hooks
Version 1.0.24 introduces a powerful hooks system that allows you to run custom commands before and after tool executions. This feature enables advanced workflows, custom validations, and integrations.

**Configuration:** Add hooks to your `~/.claude/claude.json` file:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "pre-edit-validator.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "log-bash-commands.sh"
          }
        ]
      }
    ]
  }
}
```

**Hook Types:**
- **PreToolUse**: Executes before a tool runs
  - Receives tool arguments as JSON input
  - Exit code 0: Continues normally (output not shown)
  - Exit code 2: Shows stderr to Claude and blocks the tool execution
  - Other exit codes: Shows stderr to user but continues
  
- **PostToolUse**: Executes after a tool completes
  - Receives JSON with "inputs" (tool arguments) and "response" (tool result)
  - Exit code 0: Output shown in transcript mode (Ctrl-R)
  - Exit code 2: Shows stderr to Claude immediately
  - Other exit codes: Shows stderr to user only

- **Notification**: Triggers when notifications are sent

**Example Use Cases:**
- Pre-commit hooks before file edits
- Security validation before running commands
- Logging and auditing tool usage
- Custom linting or formatting checks
- Integration with external systems

#### OAuth Flow Improvements
The OAuth authentication flow now provides better visibility into the authorization process:

- The authorization URL is now accessible programmatically during the flow
- Improved error handling for OAuth client configuration issues
- Better cleanup of invalid OAuth credentials when authentication fails


### Technical Changes

- Replaced direct stream imports with more specific imports (`PassThrough` from stream module)
- Updated process import to use named import (`cwd` from node:process)
- Enhanced OAuth flow to accept a callback for receiving the authorization URL
- Multiple new internal variables added for improved functionality


### Bug Fixes

- Fixed OAuth error handling to properly clean up invalid client credentials
- Improved error messages and logging throughout the OAuth flow

This release focuses on extensibility and developer experience, with the hooks system being the standout feature that enables powerful customization of Claude Code's behavior.
