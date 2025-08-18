# Guttenbergovitz iTerm Theme

A minimalist, ergonomic terminal theme for iTerm2 inspired by vintage printing and jazz aesthetics.

## Features

- **Warm color palette** - Less blue light, more warmth for reduced eye strain
- **Minimal syntax highlighting** - Focus on readability
- **Vintage-inspired** - Colors reminiscent of vintage book printing
- **Professional aesthetic** - Clean without being corporate

## Installation

### Option 1: Double-click Installation

1. Download the `Guttenbergovitz.itermcolors` file
2. Double-click the file to import it into iTerm2
3. The theme will be automatically added to your color presets

### Option 2: Manual Installation

1. Open iTerm2
2. Go to `iTerm2 → Preferences` (or press `Cmd + ,`)
3. Navigate to `Profiles → Colors`
4. Click the `Color Presets...` dropdown in the bottom right
5. Select `Import...`
6. Navigate to and select the `Guttenbergovitz.itermcolors` file
7. The theme will be added to your presets

## Applying the Theme

1. In iTerm2 Preferences, go to `Profiles → Colors`
2. Select your profile from the left sidebar
3. Click the `Color Presets...` dropdown
4. Select `Guttenbergovitz` from the list

## Color Palette

The theme uses a consistent color palette:

- **Background**: `#232326` (main) / `#1d1d20` (darker)
- **Foreground**: `#d4be98` (warm beige)
- **Selection**: `#3a3a3d` (subtle gray)
- **Cursor**: `#d4be98` (matches foreground)

### ANSI Colors

- **Black**: `#1d1d20` / `#7c7c7c` (bright)
- **Red**: `#a96b69` / `#cc6666` (bright)
- **Green**: `#89a87d` / `#b5bd68` (bright)
- **Yellow**: `#d6b986` / `#f0c674` (bright)
- **Blue**: `#d79969` / `#d79969` (bright)
- **Magenta**: `#a96b69` / `#a96b69` (bright)
- **Cyan**: `#89a87d` / `#89a87d` (bright)
- **White**: `#d4be98` / `#e0d2a6` (bright)

## Design Notes

- Warm-first palette; ANSI blue intentionally mapped to orange (`#d79969`).
- If imported colors deviate, re-export `.itermcolors` from the shared palette.

## Generate from Palette

You can regenerate the `.itermcolors` file from the central palette:

```bash
make gen.iterm
```

This writes `iterm/Guttenbergovitz.itermcolors` using `palette.json`.

## Compatibility

- iTerm2 version 3.0 and later
- macOS 10.12 and later

## Related Themes

This theme is part of the Guttenbergovitz theme collection, also available for:

- [Neovim](../lua/guttenbergovitz/)
- [VS Code](../vscode/)
- [Helix](../helix/)
- [Kitty](../kitty/)
- [Warp](../warp/)
- [Zed](../zed/)
- [JetBrains IDEs](../jetbrains/)

## License

MIT License - see the root directory for details.
