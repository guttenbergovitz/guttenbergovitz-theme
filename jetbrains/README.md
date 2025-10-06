# Guttenbergovitz for JetBrains IDEs

> "It's not the notes you play, it's the notes you don't play." - Miles Davis

A warm, vintage-inspired theme for JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, GoLand, PhpStorm, etc.), matching the Guttenbergovitz color scheme.

## Quick Start

**What you get:**
- ✅ **Editor Color Scheme** (`.icls`) - Easy to install, most users need only this
- 🔧 **UI Theme Plugin** (`.jar`) - Optional, for complete IDE theming (requires plugin installation)

**For most users:** Just install the Editor Color Scheme below. It's simple and gives you the beautiful Guttenbergovitz colors in your code editor!

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

### Understanding JetBrains Theming System

JetBrains IDEs use **two separate theming systems**:

1. **Editor Color Scheme** (`.icls` file) - Easy to install ✅
   - Colors the **editor only** (code syntax, gutter, selections)
   - Install via: `Settings → Editor → Color Scheme → Import Scheme`
   - **This is what most users need!**

2. **UI Theme** (plugin with `.theme.json`) - Requires plugin installation
   - Colors the **entire IDE interface** (tool windows, tabs, menus, dialogs)
   - Requires building and installing as a plugin
   - Optional - use with Darcula/New UI if you prefer

**Quick Start:** Just install the Editor Color Scheme below. The UI theme is optional!

---

### Installing Editor Color Scheme (Recommended)

**Method 1: Direct Download**

1. Download the color scheme:
```bash
curl -o Guttenbergovitz.icls https://raw.githubusercontent.com/guttenbergovitz/guttenbergovitz-theme/main/jetbrains/Guttenbergovitz.icls
```

2. In your JetBrains IDE:
   - Go to `Settings/Preferences` (`Cmd + ,` on macOS, `Ctrl + Alt + S` on Windows/Linux)
   - Navigate to `Editor → Color Scheme`
   - Click the gear icon ⚙️ next to the scheme selector
   - Select `Import Scheme → IntelliJ IDEA color scheme (.icls)`
   - Choose the downloaded `Guttenbergovitz.icls` file
   - Select `Guttenbergovitz` from the scheme dropdown

**Method 2: Manual Copy**

1. Clone this repository:
```bash
git clone https://github.com/guttenbergovitz/guttenbergovitz-theme.git
```

2. Copy the theme file to your IDE's color schemes directory:
   - **macOS**: `~/Library/Application Support/JetBrains/<IDE><version>/colors/`
   - **Linux**: `~/.<IDE><version>/config/colors/`
   - **Windows**: `%USERPROFILE%\.<IDE><version>\config\colors\`

   Replace `<IDE>` with your IDE name (IntelliJ, PyCharm, WebStorm, GoLand, etc.)
   Replace `<version>` with your IDE version (e.g., 2023.3)

3. Restart your IDE

4. Select the theme in `Settings → Editor → Color Scheme → Guttenbergovitz`

**You're done!** The editor will now use Guttenbergovitz colors. The IDE UI will use your current theme (Darcula, New UI, etc.).

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

---

## Optional: UI Theme Plugin (Advanced)

### What's the Difference?

- **Editor Color Scheme** (`.icls` - installed above): Colors your **code editor**
- **UI Theme Plugin** (`.jar` - optional): Colors the **entire IDE interface**

**Most users only need the Editor Color Scheme!** The UI theme is for users who want the complete Guttenbergovitz experience throughout the entire IDE interface.

### UI Theme Features

If you want to theme the **entire IDE** (not just the editor), you can install the UI Theme Plugin:

**What it themes:**
- Tool windows, tabs, and headers
- Status bar, navigation bar, menu bar
- Popups, dialogs, and notifications
- Lists, trees, and tables
- Buttons, inputs, and controls
- Welcome screen and search everywhere
- Progress bars and scrollbars
- Version control UI
- And much more (56+ components!)

**Full support for:**
- New UI (JetBrains 2023.3+)
- All JetBrains IDEs (IntelliJ, PyCharm, WebStorm, etc.)

### Installing UI Theme Plugin

**Important:** This requires building and installing a plugin. It's more complex than the color scheme!

**Step 1: Build the plugin**

```bash
# From repository root
make zip.jetbrains-ui

# Or manually
cd jetbrains/ui-theme/resources
zip -r ../guttenbergovitz-ui-theme.jar META-INF themes
```

**Step 2: Install the plugin**

1. Open your IDE
2. Go to `Settings → Plugins`
3. Click the gear icon ⚙️ → `Install Plugin from Disk...`
4. Select the generated `.jar` file (e.g., `guttenbergovitz-ui-theme.jar`)
5. Click OK
6. **Restart your IDE** (required!)

**Step 3: Activate the UI theme**

1. Go to `Settings → Appearance & Behavior → Appearance`
2. In the "Theme" dropdown, select `Guttenbergovitz UI`
3. The editor will automatically use the matching color scheme

**Done!** Now your entire IDE uses Guttenbergovitz colors.

### Alternative: Mix and Match

You can also:
- Use **Guttenbergovitz editor scheme** + **Darcula/New UI** for the interface
- Use **any editor scheme** + **Guttenbergovitz UI theme** (though not recommended)
- Set accent color to `#d79969` in Appearance settings for best consistency

### Version Compatibility

- **JetBrains IDEs 2023.3+**: Full support including New UI
- **JetBrains IDEs 2022.x - 2023.2**: Compatible

### Technical Details

**Editor Color Scheme:**
- File: `Guttenbergovitz.icls` (~600 lines)
- Format: XML-based color scheme
- Installation: Import directly via Color Scheme settings
- Scope: Editor only

**UI Theme Plugin:**
- Files: `plugin.xml` + `Guttenbergovitz.theme.json` (582 lines)
- Format: JetBrains plugin with JSON theme
- Installation: Plugin installation from disk
- Scope: Entire IDE interface
- Components: 56+ UI elements

### Color Consistency

All colors are sourced from `palette.json`, ensuring perfect consistency across:
- Editor syntax highlighting
- IDE user interface
- All other Guttenbergovitz implementations (VS Code, Neovim, terminals, etc.)

Run `make validate` from repository root to verify color consistency.
