# Changelog for version 0.2.59

# Claude Code v0.2.59 Changelog


### ️ Copy+paste images directly into your prompt
You can now paste images (JPEG, PNG, GIF, WebP) directly into the chat interface. Claude will automatically detect and process these images, making it easier to share screenshots, diagrams, or other visual content without having to save and reference files.


### Improved progress indicators for bash and fetch tools
The CLI now provides better visual feedback when running bash commands or fetching web content, giving you clearer indication of long-running operations.


### Bugfixes for non-interactive mode (-p)
Fixed several issues that affected the non-interactive prompt mode (`claude -p`), making it more reliable for scripted usage.


### Enhanced Onboarding Experience
The getting started tips now track completion status with checkmarks (✓) for completed items:
- Workspace setup
- CLAUDE.md file creation  
- Terminal integration setup


### Better Image Handling
Added dedicated image MIME type detection and processing for:
- `image/jpeg`
- `image/png`
- `image/gif`
- `image/webp`


### Animation Configuration
New character animation setting added to the configuration system, allowing customization of text rendering animations.


### Stream Event Processing
Improved handling of streaming responses with better support for:
- Text deltas
- JSON deltas
- Thinking mode deltas
