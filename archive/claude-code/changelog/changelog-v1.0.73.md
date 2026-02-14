# Changelog for version 1.0.73

## Highlights
Version 1.0.73 improves permission transparency with clearer approval messages, refactors command safety checks for better maintainability, and lays the groundwork for intelligent bash output management with automatic file saving capabilities.


### Bash Output File Saving (Preview)
**What:** Automatically saves all bash command outputs to files for future reference
**How to use:**
```bash
# When you run any bash command, outputs are automatically saved
claude "npm test"
# Outputs saved to bash-outputs/ directory with timestamp-based filenames
```
**Details:**
- All command outputs (stdout and stderr) are preserved in `bash-outputs/` directory
- Files are named with timestamps and command hashes for uniqueness
- Infrastructure for AI-powered output summarization is included but currently disabled
- Future releases will enable intelligent summarization of verbose outputs (>5000 chars)


### Enhanced Permission Messages
**What:** More informative and specific permission approval messages
**How to use:**
```bash
# You'll now see specific reasons why permission is needed
# Instead of: "Claude requested permissions to use Bash"
# You'll see: "Permission rule 'npm-*' from project settings requires approval for this Bash command"
```
**Details:**
- Messages now show which rule, hook, or mode triggered the permission request
- Clear attribution of permission rules to their source (local settings, project settings, etc.)
- Multi-command operations show which specific parts need approval
- New hook system allows external tools to provide custom permission feedback


### Refactored Command Safety System
**What changed:** Command injection and safety checks reorganized into modular architecture
**Impact:** Same security coverage with better performance and maintainability - no change in user-facing behavior, but more accurate detection with fewer false positives


### Better Permission Rule Management
**What changed:** New functions for tracking and managing "always ask" permission rules across different sources
**Impact:** More granular control over which operations require approval, with clearer visibility into rule sources


### Code Cleanup
**What changed:** Removed 17 unused utility functions (lodash-like implementations)
**Impact:** Smaller bundle size and cleaner codebase - no functional changes for users


### Fixed: Permission Decision Tracking
- **Issue:** Permission decisions weren't clearly showing their source
- **Cause:** Decision reasons were stored as plain strings without context
- **Resolution:** Now uses structured objects with type information and source attribution


### Fixed: Command Safety False Positives
- **Issue:** Some safe commands with quotes were incorrectly flagged as dangerous
- **Cause:** Quote parsing didn't properly distinguish between quoted and unquoted content
- **Resolution:** Enhanced parsing system better understands quote contexts
