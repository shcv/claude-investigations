# Changelog for version 0.2.97

# Claude Code v0.2.97 Changelog

## Import Optimizations

This release includes minor internal optimizations to how modules are imported:

### Changed Imports

- **Process module**: Now imports only the `cwd` function directly from `node:process` instead of importing the entire module
  - This change improves efficiency by only loading the specific function needed for getting the current working directory
  
- **Stream module**: Now imports only the `PassThrough` class directly from the `stream` module instead of importing the entire module
  - PassThrough streams are used internally for data flow management

### Technical Details

These changes represent a shift from default imports to named imports for better tree-shaking and reduced memory footprint:

```javascript
// Before (v0.2.96)
import process from "node:process";
import stream from "stream";

// After (v0.2.97)
import { cwd } from "node:process";
import { PassThrough } from "stream";
```

### Impact

- No user-facing changes or new features
- Internal performance optimization only
- All existing functionality remains unchanged
- No breaking changes

This is a maintenance release focused on code optimization with no changes to CLI commands, arguments, or interactive behavior.
