# Changelog for version 1.0.47


### Changed
- **Optimized Node.js module imports** - The codebase now uses more specific imports instead of importing entire modules:
  - `node:process` - Now imports only the `cwd` function instead of the entire module
  - `node:stream` and `stream` - Now imports only the `PassThrough` class instead of the entire module
  
### Technical Details
- Replaced default imports with named imports for better tree-shaking and reduced memory footprint:
  - `import mu2 from "node:process"` → `import { cwd as RLA } from "node:process"`
  - `import wMA from "node:stream"` → `import { PassThrough as XvQ } from "node:stream"`
  - `import NRB from "stream"` → `import { PassThrough as Yy6 } from "stream"`

### Performance Impact
This change reduces the application's memory usage by only importing the specific functions and classes needed rather than loading entire Node.js modules. Users may experience slightly faster startup times and reduced memory consumption, though the impact will likely be minimal in typical usage scenarios.

### Additional Notes
- The update includes 154 internal renames, likely due to the minification process adjusting variable names
- No functionality changes - this is purely an optimization update
- The structural similarity remains at 100%, confirming no architectural changes
