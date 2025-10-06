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

### New JetBrains UI Support

This theme fully supports the new JetBrains UI introduced in the 2023.3 release, including:
- Updated tool window styling
- New sidebar and navigation elements
- Tab underlines and indicators
- Breadcrumbs navigation
- Updated scrollbars
- Status bar styling

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

The theme includes enhanced syntax highlighting for various languages, with careful attention to language-specific constructs while maintaining consistency with the overall color palette:

### Web Development
- **HTML/XML**: Tags use keyword colors (red), attributes use type colors (yellow), and attribute values use string colors (green)
- **CSS/SCSS**: Properties use variable colors, values use string or constant colors, and selectors use keyword colors
- **JavaScript/TypeScript**: 
  - Classes and interfaces use type colors (yellow)
  - Functions and methods use function colors (orange)
  - JSX/TSX tags use keyword colors (red)
  - Template literals use string colors (green)
  - Regular expressions use string colors (green)

### Backend Development
- **Python**: 
  - Decorators use function colors (orange)
  - Self/cls parameters use keyword colors (red)
  - Predefined functions use function colors (orange)
- **Java/Kotlin**: 
  - Classes and interfaces use type colors (yellow)
  - Annotations use keyword colors (red)
  - Smart casts have subtle background highlighting
  - Named arguments use type colors (yellow)
- **Go**: 
  - Struct fields use variable colors (foreground)
  - Interfaces use type colors (yellow)
  - Method receivers use parameter colors
- **PHP**: 
  - Magic methods use function colors (orange)
  - Type hints use type colors (yellow)
  - Heredoc/nowdoc syntax uses string colors (green)
- **Ruby**: 
  - Symbols use constant colors (yellow)
  - Blocks use keyword colors (red)
  - Instance variables use variable colors (foreground)

### Markup and Data
- **Markdown**: 
  - Headings use function colors (orange) with bold styling
  - Links use string colors (green) with underline
  - Code blocks and spans have a darker background
  - Bold and italic text maintain foreground color with appropriate styling
- **JSON/YAML**: 
  - Keys use variable colors (foreground)
  - Values use appropriate type-based colors
  - Structural elements use punctuation colors

## Contributing

Feel free to open an issue or submit a pull request on our [GitHub repository](https://github.com/guttenbergovitz/guttenbergovitz-theme).

## License

This theme is released under the MIT License. See the [LICENSE](../LICENSE) file for more details. 

## UI Theme Support (Complete IDE Theming)

### Comprehensive UI Theme Plugin

The Guttenbergovitz theme includes a **complete UI theme plugin** that themes the entire IDE, not just the editor.

**What's Included:**

1. **Editor Color Scheme** (`Guttenbergovitz.icls`) - ~600 lines
   - Complete syntax highlighting for all languages
   - Git/VCS colors, diff colors, error/warning colors
   - Terminal colors

2. **UI Theme Plugin** (`ui-theme/`) - 500+ lines
   - Themes all IDE components outside the editor
   - Full support for New UI (JetBrains 2023.3+)
   - Includes tool windows, tabs, menus, popups, dialogs, and more

**Themed Components:**
Main window • Tool windows • Tabs • Status bar • Navigation bar • Menus and popups • Search everywhere • Welcome screen • Notifications • Lists and trees • Tables • Buttons and inputs • Progress bars • Scrollbars • Version control UI • And much more!

### Installation

**Build and Install UI Theme Plugin:**

```bash
# From repository root
make zip.jetbrains-ui

# Or manually
cd jetbrains/ui-theme/resources
zip -r ../guttenbergovitz-ui-theme.jar META-INF themes
```

Then in your IDE:
1. `Settings → Plugins → ⚙ → Install Plugin from Disk…`
2. Select the `.jar` file
3. Restart IDE
4. `Settings → Appearance → Theme: Guttenbergovitz UI`

**Alternative:** Use only the editor color scheme (`.icls`) with your current UI theme. Set accent color to `#d79969` in Appearance settings for best results.

### Version Compatibility

- **JetBrains IDEs 2023.3+** - Full support including New UI
- **JetBrains IDEs 2022.x - 2023.2** - Compatible

### Color Consistency

All colors are sourced from `palette.json`, ensuring perfect consistency across all Guttenbergovitz implementations (VS Code, Neovim, Vim, terminals, etc.). Run `make validate` from repository root to verify.
