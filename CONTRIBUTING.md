# Contributing to Guttenbergovitz Theme

Thank you for your interest in contributing to the Guttenbergovitz theme! This guide will help you maintain color consistency across all platforms.

## Color Consistency Guarantee

All Guttenbergovitz theme implementations are validated against a single source of truth to ensure identical colors across all platforms. The **VSCode theme** serves as the reference implementation, with all colors defined in `palette.json`.

## Making Changes to Colors

### 1. Edit `palette.json`
**This is the only file you need to edit for color changes.**

The palette is structured as follows:
```json
{
  "dark": {
    "base": {          // Background and foreground colors
      "bg": "#232326",
      "fg": "#d4be98"
      // ...
    },
    "accents": {       // Syntax highlighting colors
      "red": "#a96b69",
      "green": "#89a87d"
      // ...
    },
    "semantic": {      // Language element mappings
      "keyword": "#a96b69",
      "function": "#d79969"
      // ...
    }
  }
}
```

### 2. Update Theme Implementations
After editing `palette.json`, update the corresponding theme files:

- **VSCode**: `vscode/themes/guttenbergovitz-color-theme.json`
- **Neovim**: `lua/guttenbergovitz/init.lua`
- **Vim**: `vim/colors/guttenbergovitz.vim`
- **Helix**: `helix/guttenbergovitz.toml`
- **Kitty**: `kitty/guttenbergovitz.conf`
- **Warp**: `warp/guttenbergovitz.yaml`
- **Ghostty**: `ghostty/guttenbergovitz`
- **Zed**: `zed/guttenbergovitz.json`

### 3. Validate Your Changes
Run the validation script to ensure consistency:

```bash
make validate
```

This will check all implementations against the reference palette and report any inconsistencies.

### 4. Test Locally
Install and test your changes in at least one editor/terminal to verify the colors look correct.

## Adding a New Platform

To add support for a new editor or terminal:

1. **Create the theme file** in a new directory (e.g., `alacritty/`)
2. **Use colors from `palette.json`** as your reference
3. **Add validation** to `scripts/validate_consistency.py`:
   ```python
   def validate_newplatform(self) -> bool:
       """Validate NewPlatform theme against palette"""
       # Implementation
   ```
4. **Test with `make validate`**
5. **Update documentation** (README.md, this file)

## Project Structure

```
guttenbergovitz-theme/
├── palette.json              # Source of truth for all colors
├── scripts/
│   ├── validate_consistency.py   # Validation script
│   └── check_palette.py          # Additional checks
├── Makefile                  # Build and validation commands
└── [platform]/               # Platform-specific implementations
```

## Available Commands

```bash
make help           # Show all available commands
make validate       # Validate color consistency
make check.palette  # Check palette usage
```

## Validation in CI/CD

All pull requests automatically run color consistency validation via GitHub Actions. Your PR must pass this check before merging.

The workflow checks:
- ✅ All theme files match the reference palette
- ✅ No unauthorized color values are used
- ✅ All required colors are present

## Color Philosophy

When proposing color changes, keep in mind the Guttenbergovitz design principles:

- **Less blue light, more warmth** - Prefer warm tones
- **Minimal but meaningful** - Only essential syntax highlighting
- **Readability first** - High contrast where it matters
- **Vintage aesthetic** - Inspired by book printing and jazz

## Review Process

1. **Open a PR** with your changes
2. **CI validation** runs automatically
3. **Maintainer review** for aesthetic and functional aspects
4. **Merge** when approved and all checks pass

## Questions?

- Open an issue for general questions
- Check existing documentation in `CLAUDE.md` and `README.md`

## Code of Conduct

Please be respectful and constructive in all interactions. We're building this theme together!

---

Thank you for contributing to Guttenbergovitz! 🎨
