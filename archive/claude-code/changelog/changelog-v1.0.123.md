# Changelog for version 1.0.123


## Highlights

This release contains internal code optimizations with no user-visible changes. The codebase has been refactored to use more specific imports for better tree-shaking and bundle optimization.


### Code Optimization
**What:** Refactored module imports to use named exports instead of namespace imports

**Details:**
- Changed `import OFQ from "stream"` to `import { PassThrough as so5 } from "stream"` at line 444692
- Changed `import $9Q from "node:process"` to `import { cwd as $7A } from "node:process"` at line 357152
- These changes improve bundle optimization and tree-shaking by importing only the specific functions needed rather than entire modules
- No functional changes to the CLI behavior or available commands
- **Evidence**: Import refactoring at lines 357152 and 444692

**Impact:** This is purely an internal optimization that may slightly reduce the CLI's memory footprint and startup time, but users will not notice any behavioral differences.
