# Guttenbergovitz

> *"It's not the notes you play, it's the notes you don't play."* — Miles Davis

A warm, low-contrast color theme inspired by vintage book printing, aged paper, and late-night jazz aesthetics. Designed to cut harsh blue light and visual noise without sacrificing clarity — available in **Dark** and **Light** variants across 19 editors, terminals, multiplexers, browsers, and AI coding tools.

---

## Philosophy

- **Warmth over glare** — charcoal ink and aged parchment replace stark `#000`/`#fff` and cold blues.
- **Restrained syntax** — every color carries semantic weight; comments fade into the margin (`~2.4:1`, Nord-inspired) so your code stays in focus.
- **Single source of truth** — all ports are derived from and validated against [`palette.json`](palette.json) for consistent colors everywhere you work.

## Ports

| Editors | Terminals | Multiplexers | AI Tools | Browsers |
|---------|-----------|--------------|----------|----------|
| [VS Code](vscode/README.md) *(+ Cursor, Kiro)* | [Kitty](kitty/README.md) | [tmux](tmux/README.md) | [Claude Code](claude-code/README.md) | [Firefox](firefox/README.md) |
| [Neovim](nvim/README.md) | [iTerm2](iterm/README.md) | [Zellij](zellij/README.md) | [Pi](pi/README.md) | |
| [Vim](vim/README.md) | [Ghostty](ghostty/README.md) | | [Herdr](herdr/README.md) | |
| [Helix](helix/README.md) | [Warp](warp/README.md) | | [OpenCode](opencode/README.md) | |
| [Zed](zed/README.md) | | | | |
| [JetBrains](jetbrains/README.md) | | | | |

## Quick Install

```bash
git clone https://github.com/guttenbergovitz/guttenbergovitz-theme.git
cd guttenbergovitz-theme
make install
```

Interactive CLI installer supporting all 18 platforms. You can also target a single platform directly:

```bash
python3 scripts/install_theme.py neovim
python3 scripts/install_theme.py herdr light
```

## Palette

### Dark (default)

| Swatch | Hex | Role |
|--------|-----|------|
| ![#232326](https://placehold.co/16x16/232326/232326.png) | `#232326` | Background |
| ![#d4be98](https://placehold.co/16x16/d4be98/d4be98.png) | `#d4be98` | Foreground, variables, punctuation |
| ![#5e5e62](https://placehold.co/16x16/5e5e62/5e5e62.png) | `#5e5e62` | Comments, docstrings *(italic)* |
| ![#a96b69](https://placehold.co/16x16/a96b69/a96b69.png) | `#a96b69` | Keywords, operators, tags |
| ![#89a87d](https://placehold.co/16x16/89a87d/89a87d.png) | `#89a87d` | Strings |
| ![#d6b986](https://placehold.co/16x16/d6b986/d6b986.png) | `#d6b986` | Types, classes, constants, numbers |
| ![#d79969](https://placehold.co/16x16/d79969/d79969.png) | `#d79969` | Functions, methods |
| ![#b194a3](https://placehold.co/16x16/b194a3/b194a3.png) | `#b194a3` | Booleans, attributes, decorators |
| ![#89b4ac](https://placehold.co/16x16/89b4ac/89b4ac.png) | `#89b4ac` | Macros, regex |

### Light

| Swatch | Hex | Role |
|--------|-----|------|
| ![#f5f3f0](https://placehold.co/16x16/f5f3f0/f5f3f0.png) | `#f5f3f0` | Background |
| ![#5a4a3a](https://placehold.co/16x16/5a4a3a/5a4a3a.png) | `#5a4a3a` | Foreground, variables, punctuation |
| ![#a19f9e](https://placehold.co/16x16/a19f9e/a19f9e.png) | `#a19f9e` | Comments, docstrings *(italic)* |
| ![#8b4c4a](https://placehold.co/16x16/8b4c4a/8b4c4a.png) | `#8b4c4a` | Keywords, operators, tags |
| ![#6b8860](https://placehold.co/16x16/6b8860/6b8860.png) | `#6b8860` | Strings |
| ![#9c7d3e](https://placehold.co/16x16/9c7d3e/9c7d3e.png) | `#9c7d3e` | Types, classes, constants, numbers |
| ![#b8784c](https://placehold.co/16x16/b8784c/b8784c.png) | `#b8784c` | Functions, methods |
| ![#956d7e](https://placehold.co/16x16/956d7e/956d7e.png) | `#956d7e` | Booleans, attributes, decorators |
| ![#6b958f](https://placehold.co/16x16/6b958f/6b958f.png) | `#6b958f` | Macros, regex |

## Language & Semantic Support

First-class TextMate, Tree-sitter, and LSP semantic token rules for **Rust, Go, Python, Ruby, PHP, Java, C#, TypeScript/TSX, Lua, Shell, YAML, JSON, TOML, CSS, and Regex**.

- **Warm ANSI remap** *(dark variant only)*: blue → orange, magenta → red, cyan → green so terminal output stays warm and cohesive. Light keeps standard ANSI mappings.
- **Italics**: Comments and docstrings use italics across editors. In Neovim, set `vim.g.guttenbergovitz_italics = true` before `:colorscheme guttenbergovitz`.

## Development & Validation

```bash
make validate        # Verify color consistency across all 16 theme families
make check.palette   # Ensure all theme files only use palette.json colors
make gen.iterm       # Regenerate terminal, Zed, VS Code, and Firefox themes from palette.json
make package.firefox # Build Firefox .xpi packages (dark & light)
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding ports or modifying colors.

## Credits

Inspired by [Nord](https://www.nordtheme.com/), [Gruvbox](https://github.com/morhetz/gruvbox), [Poimandres](https://github.com/drcmda/poimandres-theme), and [Everforest](https://github.com/sainnhe/everforest).

---

*"Make it simple, but significant."*
