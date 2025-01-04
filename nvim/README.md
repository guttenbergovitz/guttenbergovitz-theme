# Guttenbergovitz for Neovim

A minimalist theme for Neovim inspired by jazz and traditional printing aesthetics.

## Requirements

- Neovim >= 0.7.0
- True color terminal support

## Installation

### Using [lazy.nvim](https://github.com/folke/lazy.nvim)

```lua
{
    "guttenbergovitz/guttenbergovitz.nvim",
    priority = 1000,
    lazy = false,
    config = function()
        vim.opt.termguicolors = true
        require("guttenbergovitz").setup()
        vim.cmd.colorscheme("guttenbergovitz")
    end,
}
```

### Using [packer.nvim](https://github.com/wbthomason/packer.nvim)

```lua
use {
    'guttenbergovitz/guttenbergovitz-theme',
    rtp = 'nvim',
    config = function()
        vim.cmd.colorscheme('guttenbergovitz')
    end
}
```

## Manual Activation

If you want to activate the theme manually, add to your init.lua:

```lua
vim.cmd.colorscheme('guttenbergovitz')
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

## Troubleshooting

If you encounter the "module 'guttenbergovitz' not found" error:

1. Make sure the plugin is properly installed
2. Check if the plugin path is in your runtimepath:
   ```lua
   :lua print(vim.inspect(vim.api.nvim_list_runtime_paths()))
   ```
3. Clear the plugin cache:
   - For Packer:
     ```
     :PackerClean
     :PackerSync
     ```
   - For Lazy:
     ```
     :Lazy clean
     :Lazy sync
     ```
   - Manual cache clearing:
     ```
     rm -rf ~/.cache/nvim
     rm -rf ~/.local/share/nvim/lazy
     rm -rf ~/.local/share/nvim/site
     ```
4. Restart Neovim after clearing the cache

## Philosophy

> "It's not the notes you play, it's the notes you don't play." - Miles Davis

Guttenbergovitz for Neovim maintains the same philosophy as its VS Code counterpart - minimalism, elegance, and functionality. Each color element has been carefully chosen to ensure comfortable work and reduce eye strain. 