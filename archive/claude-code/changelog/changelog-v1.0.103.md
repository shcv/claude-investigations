# Changelog for version 1.0.103

## 🎯 Highlights
This release introduces npm plugin support, allowing users to install and use Claude plugins directly from npm packages. It also enhances file security by expanding protection to include IDE configurations and shell files beyond just Git files.

## 🚀 New Features

### npm Plugin Support
**What:** Claude Code now supports loading plugins directly from npm packages using the `npm:` prefix in repository names

**How to use:**
```bash
# In your settings.json, add npm packages as plugin repositories
{
  "enabledPlugins": {
    "npm:@claude/example-plugin": true,
    "npm:claude-dev-tools": ["specific-command"]
  }
}
```

**Details:**
- Package names must follow npm naming conventions (alphanumeric, hyphens, periods, underscores)
- Supports both regular and scoped npm packages (e.g., `@org/package-name`)
- Automatically resolves packages from `node_modules` directory
- Validates plugin structure (requires `commands/`, `agents/`, `plugin.json`, or `hooks/` directories)
- **Evidence**: `jF5() at line 395289`, `RF5() at line 395212`, `qS at line 395336`

### Enhanced File Security Protection
**What:** Expanded file filtering now protects IDE configurations and shell files in addition to Git files

**Details:**
- **Protected directories**: `.git`, `.vscode`, `.idea` (anywhere in file path)
- **Protected files**: `.gitconfig`, `.bashrc`, `.bash_profile`, `.zshrc`, `.zprofile`, `.profile`
- Claude will now request permission before editing these sensitive files
- Consolidated security logic provides consistent protection across file types
- **Evidence**: `UW9() at line 352933`

## Other changes

### Plugin Loading Architecture
Refactored plugin discovery system with improved error handling and conflict detection. Plugin names must now be unique across all repositories, with clear error messages for conflicts.

### Todo Display Integration
Added keyboard shortcut integration hook for todo toggle functionality, improving the user experience when managing todos during Claude sessions.
**Evidence**: `ylB() at line 430535`
