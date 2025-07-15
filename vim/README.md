# Guttenbergovitz Theme for Vim

A minimalist, ergonomic theme for Vim 8+ inspired by vintage printing and jazz aesthetics.

## Features

- **Vim 8+ compatible** - Written in pure Vimscript
- **True color support** - Requires `termguicolors` or GUI support
- **Comprehensive syntax highlighting** - Supports all standard Vim syntax groups
- **Plugin support** - Includes highlights for popular plugins
- **Consistent color palette** - Matches other Guttenbergovitz implementations

## Requirements

- Vim 8.0 or higher
- Terminal with true color support (24-bit) or GUI Vim
- `termguicolors` option enabled

## Installation

### Using vim-plug

Add this to your `~/.vimrc`:

```vim
Plug 'guttenbergovitz/guttenbergovitz-theme'
```

Then run `:PlugInstall` and add to your `~/.vimrc`:

```vim
set termguicolors
colorscheme guttenbergovitz
```

### Using Vundle

Add this to your `~/.vimrc`:

```vim
Plugin 'guttenbergovitz/guttenbergovitz-theme'
```

Then run `:PluginInstall` and add to your `~/.vimrc`:

```vim
set termguicolors
colorscheme guttenbergovitz
```

### Manual Installation

1. Download the theme file:
   ```bash
   curl -o ~/.vim/colors/guttenbergovitz.vim https://raw.githubusercontent.com/guttenbergovitz/guttenbergovitz-theme/main/vim/colors/guttenbergovitz.vim
   ```

2. Add to your `~/.vimrc`:
   ```vim
   set termguicolors
   colorscheme guttenbergovitz
   ```

### Using with Pathogen

1. Clone the repository:
   ```bash
   cd ~/.vim/bundle
   git clone https://github.com/guttenbergovitz/guttenbergovitz-theme.git
   ```

2. Add to your `~/.vimrc`:
   ```vim
   set termguicolors
   colorscheme guttenbergovitz
   ```

## Configuration

### Basic Setup

```vim
\" Enable true color support
set termguicolors

\" Set the colorscheme
colorscheme guttenbergovitz
```

### Recommended Settings

For the best experience, consider these additional settings:

```vim
\" Enable syntax highlighting
syntax on

\" Show line numbers
set number

\" Highlight current line
set cursorline

\" Enable true color support
set termguicolors

\" Set the colorscheme
colorscheme guttenbergovitz

\" Optional: Set background (usually not needed)
\" set background=dark
```

## Plugin Support

The theme includes support for many popular Vim plugins:

- **vim-airline** - Status line theming
- **vim-gitgutter** - Git diff indicators
- **vim-signify** - VCS diff indicators
- **NERDTree** - File explorer
- **fzf** - Fuzzy finder
- **CtrlP** - File finder
- **vim-indent-guides** - Indentation guides
- **vim-startify** - Start screen
- **vim-fugitive** - Git integration
- **vim-which-key** - Key binding helper

## Color Palette

The theme uses a warm, low-contrast color palette inspired by vintage printing and jazz aesthetics:

### Base Colors
![#232326](https://via.placeholder.com/15/232326/000000?text=+) **Background**: `#232326` (main editor background)  
![#1d1d20](https://via.placeholder.com/15/1d1d20/000000?text=+) **Background Dark**: `#1d1d20` (darker UI elements)  
![#2a2a2d](https://via.placeholder.com/15/2a2a2d/000000?text=+) **Background Light**: `#2a2a2d` (lighter UI elements)  

![#d4be98](https://via.placeholder.com/15/d4be98/000000?text=+) **Foreground**: `#d4be98` (main text)  
![#7c7c7c](https://via.placeholder.com/15/7c7c7c/000000?text=+) **Foreground Dark**: `#7c7c7c` (dimmed text, comments)  
![#e0d2a6](https://via.placeholder.com/15/e0d2a6/000000?text=+) **Foreground Light**: `#e0d2a6` (highlighted text)  

### Accent Colors
![#a96b69](https://via.placeholder.com/15/a96b69/000000?text=+) **Red**: `#a96b69` (keywords, statements)  
![#89a87d](https://via.placeholder.com/15/89a87d/000000?text=+) **Green**: `#89a87d` (strings, success states)  
![#d6b986](https://via.placeholder.com/15/d6b986/000000?text=+) **Yellow**: `#d6b986` (constants, types)  
![#7a9ec2](https://via.placeholder.com/15/7a9ec2/000000?text=+) **Blue**: `#7a9ec2` (directories, links)  
![#d79969](https://via.placeholder.com/15/d79969/000000?text=+) **Orange**: `#d79969` (functions, titles)  
![#b194a3](https://via.placeholder.com/15/b194a3/000000?text=+) **Purple**: `#b194a3` (preprocessor, special)  
![#89b4ac](https://via.placeholder.com/15/89b4ac/000000?text=+) **Cyan**: `#89b4ac` (regex, references)  

### UI Colors
![#3a3a3d](https://via.placeholder.com/15/3a3a3d/000000?text=+) **Selection**: `#3a3a3d` (visual selection, current line)  
![#3a3a3d](https://via.placeholder.com/15/3a3a3d/000000?text=+) **Border**: `#3a3a3d` (window borders, separators)  

### Status Colors
![#cc6666](https://via.placeholder.com/15/cc6666/000000?text=+) **Error**: `#cc6666` (error messages, diagnostics)  
![#de935f](https://via.placeholder.com/15/de935f/000000?text=+) **Warning**: `#de935f` (warning messages)  
![#81a2be](https://via.placeholder.com/15/81a2be/000000?text=+) **Info**: `#81a2be` (info messages)  
![#8abeb7](https://via.placeholder.com/15/8abeb7/000000?text=+) **Hint**: `#8abeb7` (hint messages)  
![#b5bd68](https://via.placeholder.com/15/b5bd68/000000?text=+) **Success**: `#b5bd68` (success states)  

### Git Colors
![#89a87d](https://via.placeholder.com/15/89a87d/000000?text=+) **Added**: `#89a87d` (git additions)  
![#d6b986](https://via.placeholder.com/15/d6b986/000000?text=+) **Modified**: `#d6b986` (git modifications)  
![#a96b69](https://via.placeholder.com/15/a96b69/000000?text=+) **Deleted**: `#a96b69` (git deletions)  

> **Note**: The color swatches above are generated using placeholder images and may not render in all markdown viewers. The hex values are the authoritative color references.

## Troubleshooting

### Colors Don't Display Correctly

1. **Check Vim version**: Run `:version` and ensure you're using Vim 8.0+
2. **Enable termguicolors**: Add `set termguicolors` to your `~/.vimrc`
3. **Check terminal support**: Ensure your terminal supports 24-bit colors
4. **Test terminal colors**: Run `echo $TERM` and verify it's set to something like `xterm-256color` or `screen-256color`

### Common Terminal Color Test

```bash
# Test if your terminal supports true colors
printf \"\\x1b[38;2;255;100;0mTRUECOLOR\\x1b[0m\\n\"
```

### Force 256 Color Mode

If true colors aren't working, you can force 256 color mode (colors will be approximated):

```vim
set t_Co=256
colorscheme guttenbergovitz
```

## Language Support

The theme includes specific highlighting for:

- HTML/XML
- CSS/SCSS
- JavaScript
- Python
- Ruby
- PHP
- Markdown
- Git commit messages
- Vim script

## Contributing

Found a bug or want to contribute? Please visit the [GitHub repository](https://github.com/guttenbergovitz/guttenbergovitz-theme).

## License

MIT License - see the repository for full details.