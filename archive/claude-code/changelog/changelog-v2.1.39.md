# Changelog for version 2.1.39


## Summary

This release introduces a keyboard shortcut for toggling fast mode, adds an intelligent skill improvement system that learns from user feedback during skill execution, and enhances security checks for git commands in sandboxed environments. Plan mode now supports auto-approval with intervention capability.


### Fast Mode Keyboard Toggle

What: Toggle fast mode directly from the chat interface using a keyboard shortcut.

Usage:
- Press `Alt+O` (or `Option+O` on macOS) to toggle fast mode on/off
- A visual indicator shows the current fast mode state in the status bar

Details:
- Works only when fast mode is available for your account
- Displays "Model set to [model] · Fast mode OFF" when switching models turns off fast mode
- Keybinding identifier: `chat:fastMode`

Evidence: New keybinding and UI element (search for `"chat:fastMode"`, `"to toggle fast mode"`)


### Skill Improvement System

What: Claude Code now detects preferences and improvements you mention during skill execution and can automatically update skill definitions to remember them for future runs.

Usage:
When running a skill, if you make requests like:
- "Can you also ask me about X?"
- "Please use a more casual tone"
- "Don't do Z next time"

Claude Code will offer to apply these improvements to the skill definition file.

Details:
- Analyzes conversation for generalizable preferences vs one-time requests
- Shows a prompt asking if you want to apply detected improvements
- Updates the `SKILL.md` file in `~/.claude/skills/<skill-name>/`
- Displays "Skill [name] updated with improvements" when applied

Evidence: Skill improvement detection and application (search for `"Skill improvement"`, `"tengu_skill_improvement_detected"`, `"updated with improvements"`)


### Plan Mode Auto-Approval with Intervention

What: Plan mode can auto-approve after a countdown, with the ability to intervene by pressing any key.

Usage:
When plan mode shows an approval prompt:
- A countdown appears: "Auto-approving in Xs... Press any key to intervene."
- Press any key to stop auto-approval and manually review
- Let the countdown complete to auto-approve

Details:
- Also applies to question auto-selection: "Auto-selecting in Xs..."
- Provides a grace period for review while enabling unattended workflows

Evidence: New auto-approval UI (search for `"Auto-approving in"`, `"Auto-selecting in"`, `"Press any key to intervene"`)


### Enhanced Git Security Checks

Additional security validations for git commands when sandbox mode is enabled:

- **Compound commands**: Git commands combined with file-creating operations now require explicit permission
- **Bare repositories**: Git commands in directories with bare repository structure require permission
- **Outside working directory**: Git commands targeting directories outside the original working directory require permission when sandbox is enabled

Evidence: New security check messages (search for `"Compound commands that create git"`, `"Git commands outside the original working directory"`)


### SDK Client App Identification

The SDK now supports a `CLAUDE_AGENT_SDK_CLIENT_APP` environment variable, allowing client applications built on the SDK to identify themselves in API requests.

Evidence: New client-app identifier support (search for `"client-app/"`, `"CLAUDE_AGENT_SDK_CLIENT_APP"`)


### Terminology Update: Penguin Mode → Fast Mode

Internal references to "penguin mode" have been renamed to "fast mode" for consistency with user-facing terminology.

Evidence: Renamed status messages (search for `"Org fast mode:"` vs old `"Org penguin mode:"`)


### Enhanced Concise Output Mode [Feature-Flagged]

What: A new system prompt mode that instructs Claude to produce more polished, concise output without filler words or restating what the user said.

Status: Feature-flagged via `tengu_bergotte_lantern` (defaults to off)

Details:
- When enabled, adds: "Your output to the user should be concise and polished. Avoid using filler words, repetition, or restating what the user has already said..."
- Falls back to "Your responses should be short and concise" when disabled
- Does not apply to code or tool calls

Evidence: New output style prompt (search for `"tengu_bergotte_lantern"`, `"concise and polished"`)
