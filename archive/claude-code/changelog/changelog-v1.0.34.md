# Changelog for version 1.0.34

Based on my analysis of the diff, here's the changelog for Claude Code version 1.0.34:

## Claude Code v1.0.34 Changelog

### New Features

#### Improved Shell Alias Setup
The CLI now provides better shell configuration guidance when setting up the `claude` command alias. When running the setup, users will see:
- Automatic detection and replacement of existing claude aliases in shell configuration files
- Clear instructions tailored to the user's specific shell (bash, zsh, etc.)
- Confirmation messages when aliases are successfully added or replaced
- Example output: `✓ Replaced old claude alias in ~/.bashrc`

### Technical Updates

#### WebIDL and URL Parsing Library Updates
- Replaced internal WebIDL type conversion library with a newer, more standards-compliant implementation
- Updated URL parsing module to align with the latest WHATWG URL Standard
- Enhanced type validation for WebIDL conversions with more descriptive error messages

#### Stream Processing Improvements  
- Updated stream imports to use more specific named imports (`PassThrough` from `stream`)
- Changed process imports to use the `node:` protocol prefix for better Node.js compatibility

### Code Quality Improvements

#### Type Conversion Functions
The new WebIDL implementation includes more robust type conversion with better error handling:
- Integer conversions now properly handle edge cases for signed/unsigned values
- Improved handling of `enforceRange` and `clamp` options
- More descriptive TypeError messages when conversions fail

Example of improved error messages:
- Old: Generic conversion errors
- New: `"Argument is not a finite number"` or `"Argument is not in byte range"`

### Internal Changes

- Structural similarity with previous version: 99.7%
- 16 new function declarations added
- 22 legacy function declarations removed  
- Maintained backward compatibility for all user-facing features

### Summary

This release focuses on internal improvements to standards compliance and code quality. Users will notice better shell setup guidance, while the underlying URL parsing and type conversion systems have been modernized to follow the latest web standards. All existing commands and features continue to work as before.
