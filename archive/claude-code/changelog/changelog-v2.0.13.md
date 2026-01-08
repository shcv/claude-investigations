# Changelog for version 2.0.13

## Highlights

This is a maintenance release focused on internal code organization and optimization. There are no user-visible changes, new features, or bug fixes in this version.

### Import Statement Optimization

This release refactors how Node.js built-in modules are imported throughout the codebase:

- **stream module**: Changed from default import (`import us from "stream"`) to named import (`import { PassThrough as Xz8 } from "stream"`) at line 457820
- **node:child_process**: Changed from default import (`import cB0 from "node:child_process"`) to named imports (`import { execSync as F7B, spawn as Lk6 } from "node:child_process"`) at line 276288
- **node:process**: Changed from default import (`import cNQ from "node:process"`) to named import (`import { cwd as nUA } from "node:process"`) at line 70245

**Technical details**: These changes optimize the module loading by importing only the specific functions needed rather than entire module namespaces. The functionality remains identical - all three modules (`stream`, `node:child_process`, and `node:process`) are still used in exactly the same way, just with more precise imports.

**User impact**: None. This is purely an internal code quality improvement with no behavioral changes.
