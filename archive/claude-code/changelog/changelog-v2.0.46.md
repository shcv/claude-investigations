# Changelog for version 2.0.46

## Highlights
Version 2.0.46 introduces **effort level configuration** - a new feature that allows users to control Claude's reasoning intensity through CLI flags, environment variables, or settings files. This release also includes internal improvements to image compression reliability and code modernization.

### Effort Level Configuration
**What:** Control Claude's reasoning effort/intensity for tasks through multiple configuration methods

**How to use:**
```bash
# Via environment variable
export CLAUDE_CODE_EFFORT_LEVEL=high
claude

# Supported values: "low", "medium", "high", or numeric values
export CLAUDE_CODE_EFFORT_LEVEL=75
claude

# Disable with "unset"
export CLAUDE_CODE_EFFORT_LEVEL=unset
claude
```

**Details:**
- Configuration priority: CLI flags (highest) → environment variable → settings file (lowest)
- Set via `CLAUDE_CODE_EFFORT_LEVEL` environment variable
- Configure in settings file with `effortLevel` field
- Supports string presets: "low", "medium", "high"
- Supports numeric values (integers)
- Use "unset" to explicitly disable effort configuration
- Integrates with Claude API's `output_config.effort` parameter using beta flag `effort-2025-11-24`
- **Evidence**: New function `a10() at line 341081` retrieves configuration from multiple sources; function `nR3() at line 491217` sets API parameters; replaces empty stub `uR3() at line 491090` from v2.0.45

### Enhanced Image Compression Format Handling
**What:** Image compression now explicitly passes the original file's media type to prevent format detection failures

**Details:**
- Caller (`Fw5()` at line 315499) now extracts file extension and constructs media type string before compression
- Function `kiQ() at line 156042` (renamed from `TiQ`) accepts new media type parameter and forwards to compression handler
- Prevents incorrect format handling when Sharp's automatic detection fails (e.g., PNG images incorrectly treated as JPEG)
- No user-facing API changes - internal reliability improvement
- **Evidence**: Function signature changed from `TiQ(A, Q) at line 156040` in v2.0.45 to `kiQ(A, Q, B) at line 156042` in v2.0.46

### Date Format Token Validation
**What:** Implemented validation for deprecated uppercase date format tokens

**Details:**
- Function `vB9() at line 458852` now validates year tokens (Y, YY, YYYY)
- Warns users when using deprecated uppercase tokens that should be lowercase
- Prevents confusion between ISO week-numbering years (Y) and calendar years (y)
- Previously stubbed in v2.0.45 (`vB9 = () => {} at line 458887`), now fully implemented
- Part of date-fns Unicode token validation system
- **Evidence**: Implementation added at `vB9() at line 458852`, used in format validation at line 458914

### Import Statement Modernization
- Migrated from default imports to named imports in multiple modules for better tree-shaking
- Examples: `import { Transform as Xw6 } from "node:stream"` at line 225107, `import { spawn as WH5, spawnSync as XH5 } from "child_process"` at line 303217
- No new module dependencies added - all imports from existing Node.js standard library
- Both import styles coexist during transition period

### Code Refactoring
- Renamed function `HG1()` to `EG1() at line 494207` for global hooks configuration getter
- Various internal identifier changes due to minification/obfuscation updates
- No functional behavior changes from refactoring
