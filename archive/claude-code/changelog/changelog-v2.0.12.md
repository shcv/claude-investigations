# Changelog for version 2.0.12

## 🎯 Highlights

Version 2.0.12 is a maintenance release focused on internal code reorganization and plugin system enhancements. The primary changes involve plugin command configuration improvements and minor UI refinements. Most of the 12,384-line increase is due to bundler regeneration with different variable names (~6,898 renames), not new functionality.

## 🚀 New Features

### Mode Commands System
**What:** Commands can now be designated as "mode commands" for specialized, multi-phase workflows

**How to use:**
Add `mode: true` to command frontmatter in your `.claude/commands/*.md` files:
```markdown
---
mode: true
description: Guided workflow for complex refactoring
---

Your command content here...
```

**Details:**
- Mode commands receive special priority in Claude's tool selection
- Display distinct permission UI titled "Use guided workflow" instead of "Slash command"
- Show message "Your request appears to match a specialized workflow"
- Intended for complex, multi-step tasks that benefit from structured guidance
- **Evidence**: `isModeCommand: K` at line 440835 in `loadCommands()` function, mode command filtering in `V6Q()` function

### Inline Plugin Commands
**What:** Plugin developers can now define commands directly in their manifest with inline markdown content

**How to use:**
In your plugin's `marketplace-manifest.json`:
```json
{
  "commands": {
    "hello": {
      "content": "---\ndescription: Say hello\n---\n\nGreet the user warmly!",
      "description": "Greet the user",
      "argumentHint": "[name]"
    },
    "status": {
      "source": "commands/status.md"
    }
  }
}
```

**Details:**
- Commands can now use object notation with `content` (inline) or `source` (file path) fields
- Cannot use both `content` and `source` - validation enforces one or the other
- Supports metadata overrides: `description`, `argumentHint`, `model`, `allowedTools`
- Reduces file clutter for simple commands
- Old array-of-paths format still supported for backward compatibility
- **Evidence**: Command schema with `content` field at lines 42750-42775 in schema definition, inline content processing in plugin loader at lines 48817-48850

## ✨ Improvements

### Enhanced Plugin Command Validation
Better error handling when plugin manifests contain invalid command entries. The system now:
- Validates that array-format commands contain only strings
- Logs descriptive errors for malformed entries: `"Unexpected command format in marketplace entry for {plugin-name}"`
- Skips invalid entries instead of crashing
- **Evidence**: Type validation in plugin loader at lines 72627-72633 in `loadPluginsFromMarketplace()` function

### Cleaner Slash Command Permission UI
The permission confirmation prompt for slash commands now displays more user-friendly information:
- Title changed from generic "Tool use" to specific "Slash command"
- Shows the actual command string instead of `SlashCommand(command-name)`
- Displays command description instead of technical `Execute slash command: /command`
- Includes command metadata for better context-aware routing
- **Evidence**: UI component changes at lines 72425-72430 in permission confirmation renderer, metadata addition at line 65680

### Internal Code Organization
Significant internal restructuring for improved maintainability:
- Ripgrep module relocated from line ~335k to line ~3.8k for faster loading in `--ripgrep` mode
- Entry point handling simplified with better separation of concerns
- Changed from `process.exit()` to `process.exitCode =` for more graceful shutdown
- ~6,898 variable renames throughout codebase (no functional impact)
- **Evidence**: Entry point refactoring at lines 461763-461773 in `az8()` function, ripgrep module relocation to lines 3856-3869

## 🔧 Technical Details

### Bundle Changes
- File size increased from 449,389 to 461,773 lines (+2.7%)
- Structural similarity: 75.0% (25% appears different due to variable renaming)
- Declaration changes: 1,207 additions, 2,304 deletions, 102 modifications, 6,898 renames
- No dependency version upgrades - all bundled libraries remain at same versions
- Bundler regeneration caused most of the diff (not actual code changes)

### What This Release Does NOT Include
- No new command-line flags or options
- No changes to debug flags (`--debug`, `-d`, `--debug-to-stderr`, `-d2e` remain identical)
- No ripgrep configuration changes (system vs builtin selection unchanged)
- No dependency upgrades (Axios, Zod, Fuse.js, LRU-cache, Minimatch, Lodash all unchanged)
- No new error handling or validation for end users
- No changes to core CLI functionality

## 📝 Notes for Plugin Developers

If you maintain Claude Code plugins, you can now:
1. Use `mode: true` frontmatter to designate workflow commands
2. Define simple commands inline in your manifest instead of creating separate `.md` files
3. Override command metadata (description, model, allowed tools) at the manifest level
4. Expect better validation errors if your manifest format is incorrect

The old plugin manifest formats remain fully supported - these are additions, not breaking changes.
