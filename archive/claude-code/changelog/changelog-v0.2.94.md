# Changelog for version 0.2.94

# Claude Code v0.2.94 Changelog

## Import Optimizations

This release focuses on optimizing module imports for better performance and cleaner code structure.

### Changes

#### **Improved Import Specificity**
The CLI now uses more targeted imports instead of importing entire modules:

- **Process Module**: Instead of importing the entire `node:process` module, the CLI now imports only the `cwd` function directly:
  ```javascript
  // Before: import YP6 from "node:process"
  // After:  import { cwd as Ti0 } from "node:process"
  ```
  This change reduces memory footprint by only loading the specific functionality needed for getting the current working directory.

- **Stream Module**: Similarly, the stream module import has been optimized to import only the `PassThrough` class:
  ```javascript
  // Before: import Uz4 from "stream"
  // After:  import { PassThrough as MW8 } from "stream"
  ```
  The `PassThrough` stream is used internally for piping data between different parts of the CLI without transformation.

### Technical Details

- **Bundle Size**: These targeted imports help reduce the overall bundle size and improve startup performance
- **No Functional Changes**: This update maintains 100% structural similarity with the previous version - all functionality remains identical
- **Internal Refactoring**: 138 internal variable renames were performed as part of the build process (standard minification behavior)

### Summary

Version 0.2.94 is a performance-focused release that optimizes how the CLI loads Node.js built-in modules. Users won't notice any behavioral changes, but the CLI should have slightly improved startup times and reduced memory usage due to more efficient module loading.
