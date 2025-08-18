# Guttenbergovitz for Helix

> "It's not the notes you play, it's the notes you don't play." - Miles Davis

A warm, vintage-inspired theme for [Helix](https://helix-editor.com/), matching the Guttenbergovitz color scheme.

## About

Guttenbergovitz was conceived during a deep dive into jazz history, evolving from a discussion about the parallels between music evolution and code aesthetics. Just as Miles Davis stripped jazz to its essence in "Kind of Blue", this theme aims to reduce visual noise while maintaining depth and character.

## Philosophy

Drawing inspiration from both old European printing traditions and modern color science, Guttenbergovitz combines the warmth of vintage manuscripts with contemporary minimalist design principles. It's like a well-aged whiskey - complex but not overwhelming.

## Design Principles

- Less blue light, more warmth
- Minimal but meaningful syntax highlighting
- Focus on readability and reduced eye strain
- Inspired by vintage book printing
- Professional without being corporate
- Like Count Basie's orchestra: elegant, precise, and purposeful

## Installation

### Manual Installation

1. Create the themes directory for Helix (if it doesn't exist):
```bash
mkdir -p ~/.config/helix/themes
```

2. Download the theme file:
```bash
curl -o ~/.config/helix/themes/guttenbergovitz.toml https://raw.githubusercontent.com/guttenbergovitz/guttenbergovitz-theme/main/helix/guttenbergovitz.toml
```

### Manual Installation (Alternative)

1. Clone this repository:
```bash
git clone https://github.com/guttenbergovitz/guttenbergovitz-theme.git
```

2. Create the themes directory for Helix:
```bash
mkdir -p ~/.config/helix/themes
```

3. Copy the theme file:
```bash
cp guttenbergovitz-theme/helix/guttenbergovitz.toml ~/.config/helix/themes/
```

## Activation

To use the theme, you need to specify it in your Helix config file (`~/.config/helix/config.toml`):

```toml
theme = "guttenbergovitz"
```

## Color Palette

The theme uses a carefully curated palette inspired by vintage printing and jazz aesthetics:

### Base Colors
- Background: `#232326`
- Foreground: `#d4be98`
- Black: `#1d1d20`
- Red: `#a96b69`
- Green: `#89a87d`
- Yellow: `#d6b986`
- Blue: `#d79969`
- Magenta: `#a96b69`
- Cyan: `#89a87d`
- Orange: `#d79969`

### UI Elements
- Background (darker): `#1d1d20`
- Background (lighter): `#2a2a2d`
- Selection: `#3a3a3d`
- Comments: `#7c7c7c`

## Contributing

Feel free to open an issue or submit a pull request on our [GitHub repository](https://github.com/guttenbergovitz/guttenbergovitz-theme).

## License

This theme is released under the MIT License. See the [LICENSE](../LICENSE) file for more details. 
## Design Notes

- Warm-first: prefer orange/brown over blue to keep the UI cozy and reduce blue light.
- Intentional ANSI remap in terminals: blue→`#d79969`, magenta→`#a96b69`, cyan→`#89a87d`.
- Comments: italics by default for readability; tweak if your font/terminal renders italics poorly.
