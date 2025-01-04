# Guttenbergovitz for Neovim

A minimalist theme for Neovim inspired by jazz and traditional printing aesthetics.

## Installation

### Using [packer.nvim](https://github.com/wbthomason/packer.nvim)

```lua
use {
    'guttenbergovitz/guttenbergovitz-theme',
    config = function()
        require('guttenbergovitz').setup()
    end
}
```

### Using [lazy.nvim](https://github.com/folke/lazy.nvim)

```lua
{
    'guttenbergovitz/guttenbergovitz-theme',
    config = function()
        require('guttenbergovitz').setup()
    end
}
```

## Activation

Add to your init.lua:

```lua
vim.cmd.colorscheme 'guttenbergovitz'
```

## Features

- Warm, ergonomic color palette
- Optimized for readability
- Minimal yet meaningful syntax highlighting
- True color support
- Inspired by traditional printing and jazz aesthetics

## Supported Plugins

The theme includes custom highlighting for popular plugins:

- **Status Lines**
  - vim-airline
  - lualine.nvim

- **File Navigation**
  - nvim-tree
  - bufferline.nvim

- **Git Integration**
  - gitsigns.nvim

- **Editor Enhancement**
  - indent-blankline.nvim

## Philosophy

> "It's not the notes you play, it's the notes you don't play." - Miles Davis

Guttenbergovitz for Neovim maintains the same philosophy as its VS Code counterpart - minimalism, elegance, and functionality. Each color element has been carefully chosen to ensure comfortable work and reduce eye strain. 