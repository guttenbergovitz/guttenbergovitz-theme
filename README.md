# Guttenbergovitz Theme

> "It's not the notes you play, it's the notes you don't play." - Miles Davis

A warm, low-contrast theme inspired by vintage printing and the aesthetics of well-worn books. Dark and light variants. Less blue light, more character.

## Contents

- [Ports](#ports)
- [Install](#install)
- [Palette](#palette)
- [Language Support](#language-support)
- [Design Notes](#design-notes)
- [Credits](#credits)
- [About](#about)

## Ports

| Editors | Terminals | Multiplexers | AI Tools |
|---------|-----------|--------------|----------|
| [VS Code](vscode/README.md) | [Kitty](kitty/README.md) | [tmux](tmux/README.md) | [Claude Code](claude-code/README.md) |
| [Neovim](nvim/README.md) | [iTerm](iterm/README.md) | [Zellij](zellij/README.md) | [Pi](pi/README.md) |
| [Vim](vim/README.md) | [Ghostty](ghostty/README.md) | | [Herdr](herdr/README.md) |
| [Helix](helix/README.md) | [Warp](warp/README.md) | | [OpenCode](opencode/README.md) |
| [Zed](zed/README.md) | | | |
| [JetBrains](jetbrains/README.md) | | | |

## Install

```bash
make install
```

Interactive installer for Helix, Zed, Ghostty, Kitty, Zellij, Vim, and Neovim.

## Palette

### Dark (default)

| Color | Hex | Role |
|-------|-----|------|
| ![#232326](https://placehold.co/16x16/232326/232326.png) | `#232326` | Background |
| ![#d4be98](https://placehold.co/16x16/d4be98/d4be98.png) | `#d4be98` | Foreground |
| ![#a96b69](https://placehold.co/16x16/a96b69/a96b69.png) | `#a96b69` | Keywords |
| ![#89a87d](https://placehold.co/16x16/89a87d/89a87d.png) | `#89a87d` | Strings |
| ![#d6b986](https://placehold.co/16x16/d6b986/d6b986.png) | `#d6b986` | Types, constants |
| ![#d79969](https://placehold.co/16x16/d79969/d79969.png) | `#d79969` | Functions |
| ![#b194a3](https://placehold.co/16x16/b194a3/b194a3.png) | `#b194a3` | Attributes, decorators |
| ![#89b4ac](https://placehold.co/16x16/89b4ac/89b4ac.png) | `#89b4ac` | Macros, regex |

### Light

| Color | Hex | Role |
|-------|-----|------|
| ![#f5f3f0](https://placehold.co/16x16/f5f3f0/f5f3f0.png) | `#f5f3f0` | Background |
| ![#5a4a3a](https://placehold.co/16x16/5a4a3a/5a4a3a.png) | `#5a4a3a` | Foreground |
| ![#8b4c4a](https://placehold.co/16x16/8b4c4a/8b4c4a.png) | `#8b4c4a` | Keywords |
| ![#6b8860](https://placehold.co/16x16/6b8860/6b8860.png) | `#6b8860` | Strings |
| ![#b8995a](https://placehold.co/16x16/b8995a/b8995a.png) | `#b8995a` | Types, constants |
| ![#b8784c](https://placehold.co/16x16/b8784c/b8784c.png) | `#b8784c` | Functions |
| ![#956d7e](https://placehold.co/16x16/956d7e/956d7e.png) | `#956d7e` | Attributes, decorators |
| ![#6b958f](https://placehold.co/16x16/6b958f/6b958f.png) | `#6b958f` | Macros, regex |

## Language Support

Rust, Go, Python, Ruby, PHP, Java, C#, TypeScript, Lua, Shell, YAML, JSON, TOML, CSS, Regex — with language-specific highlighting across all editor ports.

## Design Notes

**Warm ANSI remap** (dark theme only): Traditional blue/magenta/cyan feel cold here. We remap: blue→orange, magenta→red, cyan→green. Light theme keeps standard mappings.

**Italics**: Comments use italics. Neovim: `vim.g.guttenbergovitz_italics = true` to enable.

**Cross-platform**: All ports stay in sync. Change one, update all.

## Credits

Built on ideas from [Nord](https://www.nordtheme.com/), [Gruvbox](https://github.com/morhetz/gruvbox), [Poimandres](https://github.com/drcmda/poimandres-theme), and [Everforest](https://github.com/sainnhe/everforest).

## About

"Guttenbergovitz" — Gutenberg's printing heritage meets Eastern European craft tradition. The theme was born from late-night discussions about code aesthetics, vintage typography, and why most themes have too much blue.

---

*"Make it simple, but significant"*
