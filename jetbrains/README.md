# Guttenbergovitz for JetBrains IDEs

> "It's not the notes you play, it's the notes you don't play." - Miles Davis

A warm, vintage-inspired theme for JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, GoLand, PhpStorm, etc.), matching the Guttenbergovitz color scheme.

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

1. Download the theme file:
```bash
curl -o Guttenbergovitz.icls https://raw.githubusercontent.com/guttenbergovitz/guttenbergovitz-theme/main/jetbrains/Guttenbergovitz.icls
```

2. In your JetBrains IDE:
   - Go to `Settings/Preferences` (`Cmd + ,` on macOS, `Ctrl + Alt + S` on Windows/Linux)
   - Navigate to `Editor → Color Scheme`
   - Click the gear icon next to the scheme selector
   - Select `Import Scheme`
   - Choose the downloaded `Guttenbergovitz.icls` file

### Manual Installation (Alternative)

1. Clone this repository:
```bash
git clone https://github.com/guttenbergovitz/guttenbergovitz-theme.git
```

2. Copy the theme file to your IDE's color schemes directory:
   - macOS: `~/Library/Application Support/JetBrains/<IDE><version>/colors/`
   - Linux: `~/.<IDE><version>/config/colors/`
   - Windows: `%USERPROFILE%\.<IDE><version>\config\colors\`

   Replace `<IDE>` with your IDE name (IntelliJ, PyCharm, WebStorm, GoLand, etc.)
   Replace `<version>` with your IDE version (e.g., 2023.3)

3. Restart your IDE

4. Select the theme in `Settings/Preferences → Editor → Color Scheme`

## Supported IDEs

This theme works with all JetBrains IDEs, including:
- IntelliJ IDEA - Java, Kotlin, and more
- PyCharm - Python development
- WebStorm - JavaScript, TypeScript, and web development
- GoLand - Go development
- PhpStorm - PHP development
- RubyMine - Ruby and Rails development
- CLion - C/C++ development
- Rider - .NET development
- DataGrip - Database tools
- Android Studio - Android development

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
- Gutter: `#232326`
- Indent Guide: `#3a3a3d`
- Caret Row: `#2a2a2d`

### Version Control
- Added: `#89a87d`
- Modified: `#d79969`
- Deleted: `#a96b69`
- Conflict: `#a96b69`

## Language-specific Highlights

The theme uses JetBrains' default token mapping system, which means it will automatically adapt to different programming languages while maintaining consistency. For example:

- **Java/Kotlin**: Classes and interfaces use type colors, annotations use keyword colors
- **Python**: Decorators use function colors, self/cls uses keyword colors
- **JavaScript/TypeScript**: JSX/TSX tags use keyword colors, template literals use string colors
- **Go**: Struct fields use variable colors, interfaces use type colors
- **PHP**: Magic methods use function colors, type hints use type colors
- **Ruby**: Symbols use constant colors, blocks use keyword colors

## Contributing

Feel free to open an issue or submit a pull request on our [GitHub repository](https://github.com/guttenbergovitz/guttenbergovitz-theme).

## License

This theme is released under the MIT License. See the [LICENSE](../LICENSE) file for more details. 