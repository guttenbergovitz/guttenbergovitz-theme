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

The theme uses a warm, low-contrast color palette:

- **Background**: `#232326` (main) / `#1d1d20` (darker)
- **Foreground**: `#d4be98` (main) / `#7c7c7c` (dimmed)
- **Accent Colors**:
  - Red: `#a96b69`
  - Green: `#89a87d`
  - Yellow: `#d6b986`
  - Blue: `#7a9ec2`
  - Orange: `#d79969`
  - Purple: `#b194a3`
  - Cyan: `#89b4ac`

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