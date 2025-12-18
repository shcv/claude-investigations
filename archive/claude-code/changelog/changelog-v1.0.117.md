# Changelog for version 1.0.117

Based on my analysis of the diff and verification of both versions, I can see that version 1.0.117 contains only internal import restructuring changes with no user-facing impact. The changes are:

1. **Removed**: `import YJQ from "stream"` - The full default import of the stream module
2. **Added**: `import { PassThrough as Jn5 } from "stream"` - A named import for just PassThrough

3. **Removed**: `import oAQ from "node:process"` - The full default import of node:process
4. **Added**: `import { cwd as fNA } from "node:process"` - A named import for just the cwd function

These are purely code optimization changes - moving from importing entire modules to importing only the specific exports needed. The functionality remains identical.

# Changelog for version 1.0.117

## 🎯 Highlights

Version 1.0.117 contains internal code optimizations with no user-visible changes or new features. This is a maintenance release focused on improving the efficiency of module imports.

## Internal Changes

### Import Optimization

The codebase has been refactored to use more specific ES6 named imports instead of default module imports, reducing the amount of code loaded at runtime. This is an internal optimization with no functional impact on CLI behavior or features.

**Technical details:**
- Replaced `import YJQ from "stream"` with `import { PassThrough as Jn5 } from "stream"` at line 442149
- Replaced `import oAQ from "node:process"` with `import { cwd as fNA } from "node:process"` at line 361348
- The `Transform` class continues to be imported from stream (via `YJQ.Transform` at line 337901)
- The `PassThrough` class usage at line 442326 now uses the named import `Jn5`
- The `cwd` function usage at lines 361467 and 361469 now uses the named import `fNA`

**Impact:** None. This is purely an internal refactoring that improves code organization and potentially reduces memory footprint, but does not change any CLI functionality, commands, flags, or user-facing behavior.
