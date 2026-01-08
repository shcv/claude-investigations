# Changelog for version 0.2.84

### Technical Updates

#### Import Refactoring
- **Updated stream import**: Changed from importing the entire `stream` module to importing only the `PassThrough` class using destructuring syntax
  - Before: `import XG9 from "stream"`
  - After: `import { PassThrough as zl9 } from "stream"`
  
- **Updated process import**: Changed from importing the entire `node:process` module to importing only the `cwd` function using destructuring syntax
  - Before: `import mA6 from "node:process"`
  - After: `import { cwd as hz2 } from "node:process"`

### Summary
This version contains minor technical improvements focused on optimizing imports. The changes reduce the bundle size by importing only the specific functions needed (`PassThrough` from stream and `cwd` from process) rather than entire modules. This is a performance optimization that should have no impact on functionality from the user's perspective.

The structural similarity remains at 100%, indicating no changes to the overall architecture or feature set of Claude Code.
