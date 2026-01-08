# Changelog for version 1.0.77

## Highlights
Claude Code 1.0.77 introduces WebSocket support for real-time communication with Claude's SDK servers, enhanced permission explanations that show exactly why actions require confirmation, and improved security with sophisticated shell command escaping to prevent injection attacks.

### WebSocket Transport for SDK Communication
**What:** Added support for persistent WebSocket connections as an alternative to stdin/stdout communication
**How to use:**
```bash
# Connect to Claude's SDK server with WebSocket
export CLAUDE_CODE_SESSION_ACCESS_TOKEN="your-token-here"
claude --sdk-url=wss://api.claude.ai/sdk/v1/connect \
       --input-format=stream-json \
       --output-format=stream-json
```
**Details:**
- Automatic reconnection with exponential backoff (up to 5 attempts)
- Message buffering during disconnections (1000 message capacity)
- Request replay on reconnection to prevent message loss
- Support for both `ws://` and `wss://` protocols with Bearer token authentication
- Enables real-time bidirectional communication for streaming responses

### Permission Reasoning Display
**What:** New UI components that explain exactly why Claude needs permission for specific actions
**How to use:**
Permission explanations now appear automatically when confirmation is required:
```
Permission rule Edit(src/**) requires confirmation for this edit.
/permissions to update rules

Hook security-check requires confirmation for this command:
Accessing sensitive configuration files
/hooks to update
```
**Details:**
- Shows the specific permission rule or hook that triggered the request
- Provides custom reasoning from hooks when available
- Includes actionable guidance on how to modify permission settings
- Consistent display across all tool types (Edit, Command, WebFetch, etc.)

### Advanced Shell Command Escaping
**What:** Sophisticated detection and escaping of dangerous shell constructs like heredocs and multiline strings
**How to use:**
This protection is automatic when Claude executes shell commands. It prevents injection attacks in complex scenarios:
```bash
# Heredocs are now safely handled
cat << EOF
$(potentially_dangerous_command)
EOF

# Multiline strings are properly escaped
echo 'line1
line2'
```
**Details:**
- Detects heredoc patterns that could bypass normal escaping
- Identifies multiline strings that might hide malicious commands
- Applies context-aware escaping strategies
- Automatically adds stdin redirection (`< /dev/null`) to prevent interactive command exploitation
- Protects against arithmetic expansion and nested command substitution attacks

### Token-Aware Conversation Summarization
**What:** Intelligent conversation summarization that respects model token limits
**How to use:**
Conversation summaries are generated automatically when saving conversations. The system will indicate if summarizing partial conversations:
```
Summarizing last 5 of 10 messages (~2500 tokens)
```
**Details:**
- Dynamically calculates available tokens based on model context window
- Prioritizes recent messages when full conversation exceeds token budget
- Transparently indicates when summaries are based on partial context
- Uses efficient Haiku model with prompt caching for fast summarization
- Generates concise 5-10 word titles for easy conversation browsing

### Server-Delivered Spinner Tips
**What changed:** Spinner tips are now managed server-side instead of being fetched by the client
**Impact:** Eliminates network latency for tip loading, provides more contextual and personalized tips with sophisticated rotation logic to prevent repetition

### Simplified Trust Model
**What changed:** Removed separate trust dialogs for hooks and bash commands in favor of unified permission system
**Impact:** Cleaner configuration with single trust mechanism, reducing complexity while maintaining security

### Enhanced Connection Resilience
**What changed:** WebSocket transport includes automatic reconnection and message replay capabilities
**Impact:** More reliable real-time communication that can survive temporary network disruptions without losing messages or state

### Fixed: Permission Requests Lacking Context
- **Issue:** Users didn't understand why specific actions required permission
- **Cause:** Permission system only showed generic confirmation prompts
- **Resolution:** Added detailed reasoning display showing exact rules/hooks and custom explanations

### Fixed: Shell Command Injection Vulnerabilities
- **Issue:** Complex shell constructs like heredocs could bypass escaping
- **Cause:** Standard shell-quote libraries don't handle all edge cases
- **Resolution:** Implemented custom pattern detection and multi-layer escaping strategy

### Fixed: Conversation Summarization Token Overflows
- **Issue:** Long conversations could exceed model token limits during summarization
- **Cause:** No token budget management when generating summaries
- **Resolution:** Added token-aware truncation that prioritizes recent messages within available budget
