# Changelog for version 1.0.29

# Claude Code v1.0.29 Changelog


### Enhanced OAuth Security
- **OAuth State Parameter**: Added CSRF protection to OAuth flows by implementing state parameter validation. The CLI now generates a secure random state value during OAuth authentication and validates it on callback to prevent cross-site request forgery attacks.


### Improved Spinner Messages
- **Expanded Word List**: The loading spinner now includes many more delightful verb options (88 total, up from 56), including whimsical additions like:
  - "Booping", "Combobulating", "Discombobulating"
  - "Flibbertigibbeting", "Philosophising", "Spelunking"
  - "Channelling", "Divining", "Enchanting"
  - "Germinating", "Incubating", "Meandering"
  - "Scheming", "Shimmying", "Sussing"
  - "Unfurling", "Unravelling", "Wandering"
  - "Whirring", "Wibbling", "Wizarding", "Wrangling"

- **Enhanced Exclusion List**: Expanded the list of words to avoid in status messages (now 99 terms) to prevent concerning or technical-looking status messages. Added common development terms like:
  - Authentication/authorization terms
  - Development operations (bootstrapping, containerizing, dockerizing)
  - Build processes (bundling, compiling, transpiling)
  - Version control operations (branching, committing, merging)
  - Deployment terms (deploying, provisioning, scaling)


### Text Rendering Improvements
- **Unicode Support**: Enhanced support for complex Unicode characters and emoji in terminal output
  - Added proper display width calculations for multi-byte characters
  - Improved text wrapping for languages with complex scripts
  - Better handling of grapheme clusters (e.g., emoji with modifiers)


### VS Code Extension Detection
- **New Function**: Added ability to detect if Claude Code is running as a VS Code extension and retrieve its version number. This enables better integration when running within VS Code.

## Technical Improvements

- **Process Import Changes**: Switched from importing entire `node:process` module to importing specific functions (`cwd`), improving module loading efficiency
- **Stream Handling**: Added `PassThrough` stream import for improved data streaming capabilities
- **Code Organization**: Minor refactoring and renaming of internal variables and functions

## Bug Fixes

- Fixed potential issues with text measurement and wrapping for complex Unicode sequences
- Improved accuracy of cursor positioning in wrapped text containing emoji or other wide characters
