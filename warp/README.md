# Guttenbergovitz for Warp

> "It's not the notes you play, it's the notes you don't play." - Miles Davis

A warm, vintage-inspired theme for [Warp](https://www.warp.dev/), matching the Guttenbergovitz color scheme.

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

1. Create the themes directory for Warp (if it doesn't exist):
```bash
mkdir -p ~/.warp/themes
```

2. Download the theme file:
```bash
curl -o ~/.warp/themes/guttenbergovitz.yaml https://raw.githubusercontent.com/guttenbergovitz/guttenbergovitz-theme/main/warp/guttenbergovitz.yaml
```

### Manual Installation (Alternative)

1. Clone this repository:
```bash
git clone https://github.com/guttenbergovitz/guttenbergovitz-theme.git
```

2. Create the themes directory for Warp:
```bash
mkdir -p ~/.warp/themes
```

3. Copy the theme file:
```bash
cp guttenbergovitz-theme/warp/guttenbergovitz.yaml ~/.warp/themes/
```

## Activation

1. Open Warp
2. Press `Cmd + P` to open the command palette
3. Type "Open Theme Picker"
4. Select "Guttenbergovitz" from the list of themes

## Color Palette

The theme uses a carefully curated palette inspired by vintage printing and jazz aesthetics:

### Base Colors
- Background: `#232326`
- Foreground: `#d4be98`
- Accent: `#d79969`

### Terminal Colors
- Black: `#1d1d20`
- Red: `#a96b69`
- Green: `#89a87d`
- Yellow: `#d6b986`
- Blue: `#d79969`
- Magenta: `#a96b69`
- Cyan: `#89a87d`
- White: `#d4be98`

## Contributing

Feel free to open an issue or submit a pull request on our [GitHub repository](https://github.com/guttenbergovitz/guttenbergovitz-theme).

## License

This theme is released under the MIT License. See the [LICENSE](../LICENSE) file for more details. 
## Design Notes

- Warm-first palette; ANSI blue is intentionally mapped to orange (`#d79969`).
- Align any future palette tweaks across all ports and READMEs.
