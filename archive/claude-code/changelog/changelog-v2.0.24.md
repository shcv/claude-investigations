# Changelog for version 2.0.24

## Highlights

Version 2.0.24 introduces intelligent auto-approval for sandboxed bash commands, increases Haiku 4.5's output capacity from 8K to 32K tokens, and adds experimental model default configurations for Pro plan users. The release also includes keyboard event propagation control for better UI interactivity and several optimizations for SDK usage.


### Auto-Allow Bash Commands in Sandbox Mode
**What:** When sandboxing is enabled and you're in "accept edits" mode, safe bash commands now execute automatically without permission prompts.

**How to use:**
```bash
# Enable the sandbox with auto-allow feature
claude --configure
# Select "Sandbox BashTool, with auto-allow in accept edits mode"

# Now when you ask Claude to create files/directories, commands like
# mkdir, touch, mv, cp execute automatically when sandboxed
```

**Details:**
- Only activates when all conditions are met: sandbox enabled, auto-allow feature enabled, command is sandboxable, and user is in "acceptEdits" mode
- Safe commands like `mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, `sed` are pre-approved in acceptEdits mode
- User-defined deny/ask rules are still respected
- Commands can be excluded via `sandbox.excludedCommands` configuration
- Falls back to standard permission prompting if conditions aren't met
- **Evidence**: `hL0()` function at lines 206586-206604 and `TN6()` decision logic at line 206562 in pretty-v2.0.24.js


### Keyboard Event Propagation Control
**What:** Keyboard event handlers can now stop event propagation to other handlers using `event.stopImmediatePropagation()`.

**How to use:**
```javascript
// For developers building on Claude Code's UI framework
useInput((input, key, event) => {
  if (input === 'q' && shouldQuit) {
    event.stopImmediatePropagation();  // Prevent other handlers from running
    handleQuit();
  }
});
```

**Details:**
- Third parameter added to keyboard event handlers containing the event object
- Enables priority-based event handling for modal dialogs, focus management, and vim-mode implementations
- Backward compatible - existing handlers with 2 parameters continue to work
- Implements DOM-style event propagation patterns
- **Evidence**: New `VO1` event class at line 71066, `B11` base class with `stopImmediatePropagation()` at line 69922, and updated callback signature in `QT9()` at line 71693 in pretty-v2.0.24.js


### Automatic AWS Credential Initialization for Bedrock
**What:** When using AWS Bedrock, credentials are now validated and refreshed automatically at startup.

**How to use:**
```bash
# Configure custom AWS auth commands in ~/.claude.json
{
  "awsAuthRefresh": "aws sso login --profile my-profile",
  "awsCredentialExport": "aws configure export-credentials --profile my-profile"
}

# Or skip auto-initialization if not needed
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1
claude
```

**Details:**
- Runs at startup when `CLAUDE_CODE_USE_BEDROCK` is set and `CLAUDE_CODE_SKIP_BEDROCK_AUTH` is not set
- First attempts standard AWS SDK authentication via STS GetCallerIdentity
- Falls back to custom `awsAuthRefresh` or `awsCredentialExport` commands if needed
- Includes workspace trust checks before executing custom commands
- Provides visual authentication feedback
- **Evidence**: New `uhQ()` initialization function at line 465179, called during startup at line 475285 in pretty-v2.0.24.js


### Increased Haiku 4.5 Output Capacity
Haiku 4.5 (`claude-haiku-4-5-20251001`) can now generate responses up to 32,000 tokens instead of being capped at 8,192 tokens. Claude 3.5 Haiku remains at 8,192 tokens.

Evidence: Removed `if (A.includes("haiku")) return 8192;` from `ox0()` function at line 458119 in pretty-v2.0.24.js


### Optimized SDK Performance
Changelog fetching is now skipped in non-interactive sessions (SDK usage, `--print` mode, non-TTY environments), reducing unnecessary network traffic during programmatic usage.

Evidence: Added `if (I3()) return;` check in `zc0()` function at line 392135 in pretty-v2.0.24.js


### Enhanced Glob Pattern Support in Sandbox Configuration
Path resolution now correctly handles glob patterns (`*`, `?`, `[`, `]`) in sandbox file access rules, preventing errors when specifying pattern-based access controls.

Evidence: New `XP()` glob detector at line 206943 and early-return check in `IP()` at line 206957 in pretty-v2.0.24.js


### Experimental Model Defaults for Pro Plan
Pro plan users may be assigned to experiments that change default model selection:
- **Haiku default**: Some Pro users may see Haiku 4.5 as default instead of Sonnet 4.5 (cost optimization)
- **Sonnet 1M default**: Users with 1M context access may default to Sonnet 4.5 [1M] instead of [200K]

These are A/B tests controlled by feature flags and not visible to all users.

Evidence: New functions `r_1()` at line 144169 and `QH0()` at line 144180 in pretty-v2.0.24.js


### Enhanced Error Diagnostics
Added telemetry for tool_use/tool_result mismatch errors to help engineers debug message normalization issues. This internal tracking does not affect user experience but helps improve reliability.

Evidence: New `Uw6()` diagnostic function at line 203566 in pretty-v2.0.24.js
