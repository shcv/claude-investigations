# Changelog for version 0.2.38

## Overview
This release introduces XML/DOM parsing capabilities and makes minor adjustments to the conversation compacting feature. The structural similarity between versions is 98.9%, with 64 additions, 21 deletions, and 6 modifications.


### XML/DOM Support
- **Added XML parsing and serialization capabilities**
  - New `DOMParser` class for parsing XML/HTML strings into DOM documents
  - New `XMLSerializer` class for converting DOM documents back to strings
  - Support for various XML MIME types including:
    - `text/html`
    - `application/xml`
    - `text/xml` 
    - `application/xhtml+xml`
    - `image/svg+xml`
  
  These features enable Claude Code to work with structured XML/HTML content internally, though they appear to be used for internal processing rather than exposed as user-facing commands.


### Conversation Compacting Enhancement
- **Modified the conversation compacting function signature** to accept an additional parameter
  - The compacting function now takes 7 parameters instead of 6
  - This suggests enhanced flexibility in how conversation history is compacted
  - The user-facing behavior remains the same - you'll still see:
    - "Compacting conversation history…" message during the process
    - "Conversation successfully compacted! ✨" upon completion
    - Error messages for various failure scenarios (no summary, API error, prompt too long)


### Code Cleanup
- Removed several unused utility functions related to:
  - Array manipulation (`md0`)
  - Brace expansion parsing (`hd0`)
  - File pattern matching (`rd0` - minimatch functionality)
  - Various deprecated dependencies


### Dependency Updates
- Updated internal libraries for:
  - AWS SDK components
  - HTTP request/response handling
  - Cryptographic operations
  - UUID generation


### New XML/DOM Implementation
The added XML functionality provides:
- Full DOM node type support (Element, Attribute, Text, CDATA, etc.)
- Namespace handling for HTML, SVG, and XML
- Proper serialization with support for various node types
- Error handling for malformed XML


### Usage Note
While the XML/DOM features are added in this version, they appear to be used internally by Claude Code for processing structured content. There are no new CLI commands or arguments exposed to users for direct XML manipulation.

## Compatibility
This update maintains backward compatibility with existing Claude Code workflows. No changes to command-line arguments or interactive features are required.
