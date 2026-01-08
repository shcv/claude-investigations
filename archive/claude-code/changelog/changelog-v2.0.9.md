# Changelog for version 2.0.9

## Highlights

Version 2.0.9 introduces Skills support for the plugin system, allowing developers to create reusable AI behaviors. Additionally, post-tool-hook feedback is now properly surfaced to the AI model as user messages, improving context awareness and response quality.

### Skills Support for Plugins

**What:** Plugins can now include "skills" - reusable AI behaviors defined in markdown files that can be loaded and executed by Claude Code.

**How to use:**
```bash
# Create a skills directory in your plugin
~/.claude/plugins/my-plugin/skills/my-skill/SKILL.md

# Or specify custom paths in your plugin manifest
{
  "name": "my-plugin",
  "skills": ["custom-skills-dir", "another-skills-dir"]
}
```

**Details:**
- Skills are loaded from subdirectories containing `SKILL.md` files
- By default, looks for a `skills/` directory in your plugin root
- Custom paths can be specified in the plugin manifest using the `skills` field (single path or array)
- Each skill directory should contain a `SKILL.md` file with frontmatter and content
- Skills are processed similarly to commands and agents but with `isSkillMode: true`
- **Evidence**: `hMB() at line 422839`, `skillsPath property at line 377365`, `isSkillMode flag at line 422855`

### API Client Fetch Override

**What:** Internal enhancement allowing custom fetch implementations to be injected into the API client for testing or custom network handling.

**Details:**
- The API client factory function (`fF()`) now accepts an optional `fetchOverride` parameter
- Replaces previous hardcoded fetch selection logic
- Primarily used internally but enables advanced customization scenarios
- **Evidence**: `fF() at line 376120`, fetch override usage at lines 411360 and 432771

### Enhanced Post-Tool-Hook Feedback Handling

**What:** Feedback from post-tool-use hooks is now properly converted to user messages, making it visible to the AI model for improved context awareness.

**How it works now:**
- Post-tool-hook feedback creates messages with subtype `"post_tool_hook_feedback"`
- These messages are automatically converted to user messages during processing
- The AI model can now reference and build upon hook outputs in subsequent responses

**Details:**
- Previously, hook feedback was treated as generic "informational" system messages
- New dedicated functions: `eb1()` creates the feedback messages, `fPB()` identifies them
- Conversion happens in message processing pipeline via `AD5()` function
- Includes dedicated UI rendering function `h2B()` for displaying feedback
- **Evidence**: `fPB() at line 436505`, `eb1() at line 437160`, conversion logic at line 436513, `h2B() rendering at line 405844`

### Grove Notice Grace Period Enforcement

**What:** The Grove climate contribution notice display logic now respects a grace period flag, allowing more persistent display of important notices.

**How it works:**
- When `notice_is_grace_period` is `false`, notices are shown regardless of previous user dismissals
- Grace period defaults to `true`, maintaining existing behavior
- After grace period ends, users see notices even if previously dismissed

**Details:**
- Affects the timing of when Grove-related notices appear in the CLI
- Allows for more aggressive communication of important announcements after initial grace period
- **Evidence**: `GBB() at line 407802` (previously `m2B() at line 407357` in v2.0.8), new grace period check at line 407805

## Internal Changes

- Updated AWS Bedrock SDK client code with new type definitions
- Refactored helper functions including `DFB()` (replaces `tXB()`) for local command message checking
- Function renames: `vF()` → `fF()`, `m2B()` → `GBB()`, `HH5()` → `AD5()`
