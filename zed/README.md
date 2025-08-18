# Guttenbergovitz for Zed

> "It's not the notes you play, it's the notes you don't play." - Miles Davis

A warm, vintage-inspired theme for [Zed](https://zed.dev/), matching the Guttenbergovitz color scheme.

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

1. Create the themes directory for Zed (if it doesn't exist):
```bash
mkdir -p ~/.config/zed/themes
```

2. Download the theme file:
```bash
curl -o ~/.config/zed/themes/guttenbergovitz.json https://raw.githubusercontent.com/guttenbergovitz/guttenbergovitz-theme/main/zed/guttenbergovitz.json
```

### Manual Installation (Alternative)

1. Clone this repository:
```bash
git clone https://github.com/guttenbergovitz/guttenbergovitz-theme.git
```

2. Create the themes directory for Zed:
```bash
mkdir -p ~/.config/zed/themes
```

3. Copy the theme file:
```bash
cp guttenbergovitz-theme/zed/guttenbergovitz.json ~/.config/zed/themes/
```

## Activation

1. Open Zed
2. Open Settings (`Cmd + ,` on macOS)
3. Navigate to "Themes"
4. Select "Guttenbergovitz" from the list

## Color Palette

The theme uses a carefully curated palette inspired by vintage printing and jazz aesthetics:

### Base Colors
- Background: `#232326`
- Foreground: `#d4be98`
- Selection: `#3a3a3d`
- Line Numbers: `#7c7c7c`

### Syntax Colors
- Comments: `#7c7c7c`
- Keywords: `#a96b69`
- Functions: `#d79969`
- Strings: `#89a87d`
- Types: `#d6b986`
- Variables: `#d4be98`

### UI Elements
- Background (darker): `#1d1d20`
- Border: `#3a3a3d`
- Disabled Text: `#7c7c7c`

## Design Notes

- Warm-first palette; avoid cold blues in favor of orange/brown.
- Intentional ANSI remap for terminals: blue→`#d79969`, magenta→`#a96b69`, cyan→`#89a87d`.
- Comments often italicized to improve hierarchy; disable in settings if preferred.

## Contributing

Feel free to open an issue or submit a pull request on our [GitHub repository](https://github.com/guttenbergovitz/guttenbergovitz-theme).

## License

This theme is released under the MIT License. See the [LICENSE](../LICENSE) file for more details. 
