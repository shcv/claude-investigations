# Changelog for version 1.0.42

Based on my analysis of the diff for version 1.0.42, here's the detailed changelog:

# Claude Code v1.0.42 Changelog


### Enhanced Configuration File Locking
- **Improved multi-instance handling**: Added file locking mechanism when saving configuration to prevent conflicts between multiple Claude instances
  - Automatically acquires a lock on the config file (`config.json.lock`) before modifications
  - Displays warning if lock acquisition takes longer than 100ms: "Lock acquisition took longer than expected - another Claude instance may be running"
  - Shows process ID (PID) when acquiring locks for better debugging
  

### Configuration Backup System
- **Automatic config backups**: Creates a backup of the configuration file before making changes
  - Provides safety net for configuration modifications
  - Debug messages indicate when backups are created


### Improved Symlink Support
- **Better symlink handling**: Enhanced detection and handling of symbolic links in file paths
  - Shows where symlinks point to in debug messages
  - More robust handling of symlinked configuration files


### Enhanced URL and URLSearchParams Implementation
- **Standards-compliant URL handling**: Updated internal URL and URLSearchParams implementations
  - Better error messages for invalid arguments (e.g., "Failed to execute 'append' on 'URLSearchParams': 2 arguments required")
  - Improved validation for URL operations
  - Enhanced Unicode domain name handling with proper `xn--` prefix support


### Better Error Handling
- **More descriptive errors**: Enhanced error messages throughout the codebase
  - Type validation errors now provide clearer context
  - Better BigInt conversion error messages
  - Improved range enforcement for numeric values


### Debug Logging Enhancements
- **More detailed debug output**: Added comprehensive debug logging for configuration operations
  - Shows lock acquisition timing
  - Indicates when config is re-read after acquiring lock
  - Logs atomic write operations for configuration files


### Working with Multiple Instances
If you're running multiple Claude Code instances, you'll now see helpful debug messages:
```
Acquiring lock on /path/to/config.json.lock for config save (PID: 12345)
Lock acquired successfully after 150ms
Lock acquisition took longer than expected - another Claude instance may be running
```


### Configuration Safety
The new backup system automatically protects your configuration:
```
Creating backup of config at /path/to/config.json.backup
Backup created successfully
Writing config to /path/to/config.json atomically
Config written successfully
```

## Notes
- This update focuses on improving reliability when multiple Claude instances are running simultaneously
- Configuration operations are now atomic and protected by file locking
- Enhanced internal URL handling provides better standards compliance
- Debug messages provide more visibility into configuration operations (visible when debug mode is enabled)
