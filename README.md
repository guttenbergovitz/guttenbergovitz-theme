# Guttenbergovitz Theme

> "It's not the notes you play, it's the notes you don't play." - Miles Davis

## Available for:

- [VS Code](vscode/README.md) - A Visual Studio Code theme
- [Neovim](nvim/README.md) - A Neovim colorscheme
- [Kitty](kitty/README.md) - A Kitty terminal theme
- [Zellij](zellij/README.md) - A Zellij terminal multiplexer theme
- [Helix](helix/README.md) - A Helix editor theme
- [Warp](warp/README.md) - A Warp terminal theme
- [Zed](zed/README.md) - A Zed editor theme
- [JetBrains](jetbrains/README.md) - A theme for all JetBrains IDEs (IntelliJ, PyCharm, WebStorm, etc.)
- [Ghostty](ghostty/README.md) - A Ghostty terminal theme

## About

Guttenbergovitz was conceived during a deep dive into jazz history, evolving from a discussion about the parallels between music evolution and code aesthetics. Just as Miles Davis stripped jazz to its essence in "Kind of Blue", this theme aims to reduce visual noise while maintaining depth and character.

## Philosophy

Drawing inspiration from both old European printing traditions and modern color science, Guttenbergovitz combines the warmth of vintage manuscripts with contemporary minimalist design principles. It's like a well-aged whiskey - complex but not overwhelming.

## Credits & Inspiration

This theme stands on the shoulders of giants:
- Nord's minimalist philosophy
- Gruvbox's warm palette foundations
- Poimandres' approach to syntax highlighting
- EverForest's natural aesthetics

Each of these themes contributed to our understanding of what makes a great coding environment, much like how blues laid the foundation for jazz evolution.

## Design Principles

- Less blue light, more warmth
- Minimal but meaningful syntax highlighting
- Focus on readability and reduced eye strain
- Inspired by vintage book printing
- Professional without being corporate
- Like Count Basie's orchestra: elegant, precise, and purposeful

## Status

This is a Work in Progress (WIP). Like jazz itself, we believe in constant evolution and improvement.

## The Name

"Guttenbergovitz" merges Gutenberg's printing heritage with Eastern European craftsmanship tradition (-ovitz), reflecting our commitment to both historical respect and modern utility.

## Ghostty Terminal Theme

### Installation

#### Manual Installation

1. Create the themes directory for Ghostty (if it doesn't exist):
```bash
mkdir -p ~/.config/ghostty/themes
```

2. Download the theme file:
```bash
curl -o ~/.config/ghostty/themes/guttenbergovitz.conf https://raw.githubusercontent.com/guttenbergovitz/guttenbergovitz-theme/main/ghostty/guttenbergovitz.conf
```

#### Manual Installation (Alternative)

1. Clone this repository:
```bash
git clone https://github.com/guttenbergovitz/guttenbergovitz-theme.git
```

2. Create the themes directory for Ghostty:
```bash
mkdir -p ~/.config/ghostty/themes
```

3. Copy the theme file:
```bash
cp guttenbergovitz-theme/ghostty/guttenbergovitz.conf ~/.config/ghostty/themes/
```

### Activation

To use the theme, you need to specify it in your Ghostty config file (`~/.config/ghostty/config.conf`):

```conf
include themes/guttenbergovitz.conf
```

## Color Palette

The theme uses a carefully curated palette inspired by vintage printing and jazz aesthetics:

- Background: `#232326`
- Foreground: `#d4be98`
- Black: `#1d1d20`
- Red: `#a96b69`
- Green: `#89a87d`
- Yellow: `#d6b986`
- Blue: `#d79969`
- Magenta: `#a96b69`
- Cyan: `#89a87d`
- White: `#d4be98`

---

*"Make it simple, but significant"*
