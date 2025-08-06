# Changelog for version 1.0.15

# Claude Code v1.0.15 Changelog

## Import Changes

### Removed Imports
- **Removed direct `stream` import** - Previously imported the entire `stream` module
- **Removed direct `node:process` import** - Previously imported the entire `node:process` module

### Added Imports
- **Added named import from `node:process`** - Now imports only the `cwd` function as `bI0`
- **Added named import from `stream`** - Now imports only the `PassThrough` class as `bK5`

This change represents a shift from importing entire modules to importing only the specific functions/classes needed, which is a best practice for reducing bundle size and improving code clarity.

## New Features

### Close All Diff Tabs Function
A new function `Tr0` has been added that allows closing all diff tabs:

```javascript
async function Tr0(A) {
  await yN("closeAllDiffTabs", {}, A, !1);
}
```

This appears to be a utility function that sends a "closeAllDiffTabs" command, likely used when working with file diffs in the Claude Code interface. Users would benefit from this when they have multiple diff views open and want to close them all at once, helping to clean up their workspace.

## Summary

Version 1.0.15 is a minor update that:
1. Optimizes imports by switching from whole module imports to named imports for `stream` and `node:process` modules
2. Adds functionality to close all diff tabs at once, improving workspace management when reviewing multiple file changes

The structural similarity remains at 100%, indicating these are targeted improvements rather than major architectural changes.
