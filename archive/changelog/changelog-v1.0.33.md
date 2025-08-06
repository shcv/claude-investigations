# Changelog for version 1.0.33

## Claude Code v1.0.33 Changelog

### 🆕 New Features

#### **Enhanced Installation Diagnostics**
- Added comprehensive installation diagnostic system that provides detailed information about your Claude installation
- Run diagnostics to see:
  - Current installation type (npm-local, npm-global, native, development)
  - Installation path and invoked binary location
  - Auto-update capability status
  - Configuration settings
  - Multiple installation detection
  - Specific warnings and recommended fixes

#### **Improved Auto-Update Configuration**
- Replaced the legacy `autoUpdaterStatus` configuration with clearer `installMethod` and `autoUpdates` settings
- The system now explicitly tracks:
  - `installMethod`: How Claude is installed (local, global, native, unknown)
  - `autoUpdates`: Whether auto-updates are enabled (true/false)

#### **Shell Alias Detection**
- New functionality to detect existing Claude aliases in shell configuration files
- Automatically checks common shell configs (.bashrc, .zshrc, etc.) for Claude aliases
- Provides smart recommendations when PATH conflicts are detected

### 🔧 Improvements

#### **Better Installation Type Detection**
- More robust detection of installation methods:
  - **npm-local**: Installed in ~/.claude/local
  - **npm-global**: Installed via global npm
  - **native**: Platform-specific installation
  - **development**: Running from development build

#### **Enhanced Permission Checking**
- Improved detection of npm permission issues for global installations
- Better recommendations for fixing permission problems
- Clearer messaging about when to use `claude migrate-installer`

#### **Smarter Configuration Migration**
- Automatic migration from old `autoUpdaterStatus` to new `installMethod`/`autoUpdates` format
- Handles legacy configurations gracefully:
  - `"migrated"` → `installMethod: "local"`
  - `"installed"` → `installMethod: "native"`
  - `"disabled"` → `autoUpdates: false`

### 🐛 Bug Fixes

#### **Input History Buffer with Debouncing**
- Added new `Xk2` function that provides an input history buffer with debouncing
- Prevents excessive history entries when typing quickly
- Configurable buffer size and debounce delay

### 💡 Usage Examples

#### Check Installation Status
The diagnostic system automatically runs when needed and provides actionable recommendations:

```
Claude CLI Diagnostic

Currently running: npm-local (1.0.33)
Path: /home/user/.claude/local/node_modules/.bin/claude
Auto-updates: Yes
Config install method: local
Config auto-updates: true
```

#### Fixing Common Issues

**Issue: Multiple installations detected**
```
Warning: Multiple installations found
- npm-local at /home/user/.claude/local
- npm-global at /usr/local/bin/claude

Fix: Create alias to override: alias claude="~/.claude/local/node_modules/.bin/claude"
```

**Issue: Permission problems with global installation**
```
Warning: Insufficient permissions for auto-updates
Fix: Run: sudo chown -R $USER:$(id -gn) $(npm -g config get prefix)
or use `claude migrate-installer` to migrate to local installation
```

### 🔄 Migration Notes

- The configuration system has been updated. Old configurations will be automatically migrated
- If you have custom scripts that check `autoUpdaterStatus`, update them to use `installMethod` and `autoUpdates` instead
- The `/migrate-installer` command is now the recommended way to switch from global to local installation
