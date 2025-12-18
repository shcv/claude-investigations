# Changelog for version 0.2.80

## Claude Code v0.2.80 Changelog

### New Features

#### 🔐 OAuth Support for Claude.ai Pro/Team Users (`CLAUDE_MAX`)
- **New environment variable**: `CLAUDE_MAX` enables OAuth authentication for Claude.ai Pro/Team users
- When enabled, adds `user:inference` scope to OAuth permissions, allowing Claude Code to use your Claude.ai account for API access
- OAuth flow automatically handles token refresh when tokens are near expiration (within 5 minutes)
- Separate token storage for Claude.ai OAuth vs Console API keys

#### 🚫 Deny Rules for Tool Permissions
- **New permission behavior**: In addition to "allow" rules, you can now create "deny" rules
- Navigate between Allow/Deny modes using Tab or arrow keys in the permission rules interface
- Denied tools will be automatically rejected without prompting
- Example: Add a deny rule for `Bash` to prevent any shell command execution

#### 🏢 Managed Settings Support
- **Enterprise policy control**: System administrators can now configure tool permissions via managed settings
- Managed settings are loaded from system-level policy files:
  - macOS: `/Library/Application Support/ClaudeCode/policies.json`
  - Linux: `/etc/claude-code/policies.json`
- Managed permission rules cannot be modified or deleted by users
- Rules are displayed with a special indicator showing they're managed by your organization

#### 🔧 Tool Renaming
- **dispatch_agent** renamed to **AgentTool** for better clarity
- **ReadNotebook** renamed to **NotebookReadTool** for consistency
- **LS** renamed to **LSTool** for consistency

### Improvements

#### 🔒 Enhanced Security
- API key validation now ensures keys only contain alphanumeric characters, dashes, and underscores
- Improved error messages for invalid API key formats
- Better error handling for OAuth token refresh failures

#### 🔔 Terminal Bell Control (macOS)
- Automatically attempts to disable the audio bell in Terminal.app profiles
- Reduces notification noise during command execution

#### 📝 At-Mention Content Display
- New visual formatting for at-mention content in conversations
- Better handling of user-provided file references

#### ⚡ Performance Enhancements
- Prompt caching can now be disabled via `DISABLE_PROMPT_CACHING` environment variable
- Improved async handling for file operations and OAuth flows

### Usage Examples

#### Using OAuth with Claude.ai Account:
```bash
# Enable Claude.ai OAuth authentication
export CLAUDE_MAX=1
claude

# The OAuth flow will include user:inference scope
# Your Claude.ai Pro/Team account will be used for API access
```

#### Creating Deny Rules:
```
# In the permission rules interface:
1. Press Tab to switch to "Deny" mode
2. Select "Add a new rule..."
3. Enter the tool pattern (e.g., "Bash", "Write*", etc.)
4. The tool will be automatically denied without prompting
```

#### Managed Settings Example:
```json
// /Library/Application Support/ClaudeCode/policies.json
{
  "permissions": {
    "allow": ["Read*", "Grep", "LS"],
    "deny": ["Bash", "Write*", "Delete*"]
  }
}
```

### Bug Fixes

- Fixed potential race conditions in OAuth callback handling
- Improved error messages for port conflicts during OAuth flow
- Better handling of manual OAuth code entry
- Fixed issues with permission rule deletion
- Enhanced validation for tool permission contexts
