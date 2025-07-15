# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the Guttenbergovitz theme - a minimalist, ergonomic theme collection inspired by vintage printing and jazz aesthetics. The theme is available for multiple editors and terminals, each maintained in its own subdirectory.

## Theme Philosophy

The Guttenbergovitz theme follows these design principles:
- Less blue light, more warmth
- Minimal but meaningful syntax highlighting  
- Focus on readability and reduced eye strain
- Inspired by vintage book printing
- Professional without being corporate

## Repository Structure

The repository is organized as a monorepo with separate implementations for each platform:

- `colors/` - Neovim colorscheme entry point (legacy vim colorscheme format)
- `lua/guttenbergovitz/` - Main Neovim theme implementation
- `vscode/` - VS Code theme extension
- `helix/` - Helix editor theme
- `kitty/` - Kitty terminal theme
- `zellij/` - Zellij terminal multiplexer theme
- `warp/` - Warp terminal theme
- `zed/` - Zed editor theme
- `jetbrains/` - JetBrains IDEs theme
- `ghostty/` - Ghostty terminal theme

## Common Development Commands

### VS Code Extension
```bash
cd vscode/
npm run package  # Creates .vsix file for distribution
```

### Neovim Theme
The Neovim theme is implemented in `lua/guttenbergovitz/init.lua` and uses the colors defined in that file. No build process is required - it's a pure Lua implementation.

### Testing Changes
Each platform has its own installation and testing process documented in their respective README files.

## Core Architecture

### Color Palette
The theme uses a consistent color palette across all platforms:
- **Background**: `#232326` (main) / `#1d1d20` (darker)
- **Foreground**: `#d4be98` (main) / `#7c7c7c` (dimmed)
- **Accent Colors**: 
  - Red: `#a96b69`
  - Green: `#89a87d`
  - Yellow: `#d6b986`
  - Blue/Orange: `#d79969`
  - Selection: `#3a3a3d`

### Neovim Implementation
The Neovim theme (`lua/guttenbergovitz/init.lua`) contains:
- Comprehensive color palette definition in `M.colors` with terminal colors
- Extensive highlight groups mapping in `M.groups` including:
  - All TreeSitter `@` groups for modern syntax highlighting
  - LSP diagnostic and semantic token support
  - Modern UI elements (floats, completion menus)
  - Plugin support for 15+ popular Neovim plugins
- Setup function with error handling and version compatibility checks
- Terminal color support (16 ANSI colors)
- Graceful fallback for older Neovim versions

### Vim Implementation  
The Vim theme (`vim/colors/guttenbergovitz.vim`) provides:
- Vim 8+ compatibility with version checks
- Pure Vimscript implementation using helper functions
- Complete color palette matching the Neovim version
- Comprehensive syntax highlighting for all standard Vim groups
- Plugin support for popular Vim plugins (vim-airline, NERDTree, fzf, etc.)
- Language-specific highlighting for HTML, CSS, JavaScript, Python, Ruby, PHP, Markdown, Git, and Vim script
- True color support with fallback to 256 color mode
- Terminal color support where available

### VS Code Implementation
The VS Code theme (`vscode/themes/guttenbergovitz-color-theme.json`) follows the standard VS Code theme format with:
- UI color definitions for editor, sidebar, status bar, etc.
- Token color rules for syntax highlighting
- Semantic token color overrides

## File Organization

Each platform directory contains:
- Implementation files (theme definitions)
- `README.md` with installation instructions
- Platform-specific assets (icons, metadata files)

## Development Notes

- The theme maintains visual consistency across platforms while adapting to each platform's specific capabilities
- Color values are kept consistent but may be adapted for platform-specific requirements
- The Neovim implementation serves as the reference for color definitions
- All implementations support the same core syntax highlighting patterns

## Status

This is a work-in-progress theme that continues to evolve. Each platform implementation may be at different stages of completeness.