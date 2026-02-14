# Changelog for version 1.0.30

# Claude Code v1.0.30 Changelog


### Theme System Overhaul
- **New theme management system**: Claude Code now supports dynamic theme switching through a new theme context provider
- **New `theme` command-line argument**: Users can now set the theme when launching Claude Code
  ```bash
  claude --theme dark
  claude --theme light
  ```
- **Live theme switching**: The application now supports changing themes while running, with all components updating in real-time


### Enhanced Color System
- **Simplified color API**: Color properties have been flattened from nested structures (e.g., `diff.added` → `diffAdded`)
- **New `inverseText` color**: Added support for inverse text colors that automatically adjust based on the theme
- **New `P` component**: Replaces the `S` component with a more flexible color system that uses color names instead of direct color values


### Transcript Mode Timestamps
- **New timestamp display**: When in transcript mode, assistant messages now show timestamps in 24-hour format (HH:MM)
- **Example**: Assistant responses will show `14:35` next to messages when transcript mode is enabled


### Better Tool Execution Status Colors
- Tool execution status indicators now use semantic color names instead of hardcoded RGB values
- Status colors are now consistent across all themes:
  - `pending`/`queued`: warning (yellow)
  - `in_progress`: permission (blue)  
  - `completed`: success (green)
  - `failed`: error (red)
  - `cancelled`: secondaryText (gray)
  - `timed_out`: autoAccept (purple)


### Cleaner Codebase
- Removed unused color conversion functions (`LQ`, `W_2`)
- Removed deprecated theme hooks (`OP2`)
- Consolidated imports and removed duplicate process imports
- Better separation of concerns with dedicated theme management


### Dialog Color Consistency
- Fixed hardcoded colors in various dialogs (bypass permissions, MCP server, external includes)
- All dialogs now properly respect the current theme
- Border colors and text colors in dialogs now use semantic color names


### Welcome Message Styling
- The welcome message now uses the proper theme-aware color system
- The Claude star icon (`✻`) properly inherits the claude brand color


### For Theme/Plugin Developers
- Color object structure has changed - nested `diff` object properties are now flat
- `S` component replaced with `P` component - update any custom components
- Direct color value access (e.g., `X1().error`) replaced with color name strings (e.g., `"error"`)


### New Theme Context
The theme system now uses React context for global theme state:
```javascript
// Setting theme programmatically
const [theme, setTheme] = useTheme();
setTheme('dark'); // or 'light', 'system', etc.
```


### Color Property Changes
Old structure:
```javascript
{
  diff: {
    added: "rgb(105,219,124)",
    removed: "rgb(255,168,180)"
  }
}
```

New structure:
```javascript
{
  diffAdded: "rgb(105,219,124)",
  diffRemoved: "rgb(255,168,180)"
}
```

This release focuses on improving the theming system and user experience with better color management and real-time theme switching capabilities.
