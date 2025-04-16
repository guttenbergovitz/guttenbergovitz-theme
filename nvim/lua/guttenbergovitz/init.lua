local M = {}

-- Color palette
M.colors = {
    bg = "#232326",
    bg_dark = "#1d1d20",
    fg = "#d4be98",
    fg_dark = "#7c7c7c",
    red = "#a96b69",
    green = "#89a87d",
    yellow = "#d6b986",
    blue = "#d79969",
    orange = "#d79969",
    selection = "#3a3a3d",
    comment = "#7c7c7c",
}

-- Highlight groups
M.groups = {
    -- Editor
    Normal = { fg = M.colors.fg, bg = M.colors.bg },
    NormalFloat = { fg = M.colors.fg, bg = M.colors.bg_dark },
    LineNr = { fg = M.colors.fg_dark },
    CursorLine = { bg = M.colors.selection },
    CursorLineNr = { fg = M.colors.fg },
    Visual = { bg = M.colors.selection },
    IncSearch = { fg = M.colors.bg, bg = M.colors.orange },
    Search = { fg = M.colors.bg, bg = M.colors.yellow },

    -- Syntax
    Comment = { fg = M.colors.comment, italic = true },
    Constant = { fg = M.colors.yellow },
    String = { fg = M.colors.green },
    Identifier = { fg = M.colors.fg },
    Function = { fg = M.colors.orange },
    Statement = { fg = M.colors.red },
    Keyword = { fg = M.colors.red },
    Type = { fg = M.colors.yellow },
    Special = { fg = M.colors.orange },

    -- Interface
    StatusLine = { fg = M.colors.fg, bg = M.colors.bg_dark },
    StatusLineNC = { fg = M.colors.fg_dark, bg = M.colors.bg_dark },
    VertSplit = { fg = M.colors.selection },
    TabLine = { fg = M.colors.fg_dark, bg = M.colors.bg_dark },
    TabLineFill = { bg = M.colors.bg_dark },
    TabLineSel = { fg = M.colors.fg, bg = M.colors.bg },

    -- Plugin Support: vim-airline
    airline_a = { fg = M.colors.bg, bg = M.colors.orange, bold = true },
    airline_b = { fg = M.colors.fg, bg = M.colors.bg_dark },
    airline_c = { fg = M.colors.fg_dark, bg = M.colors.bg },
    airline_x = { fg = M.colors.fg_dark, bg = M.colors.bg },
    airline_y = { fg = M.colors.fg, bg = M.colors.bg_dark },
    airline_z = { fg = M.colors.bg, bg = M.colors.green, bold = true },
    airline_error = { fg = M.colors.red },
    airline_warning = { fg = M.colors.yellow },

    -- Plugin Support: lualine.nvim
    LualineA = { fg = M.colors.bg, bg = M.colors.orange },
    LualineB = { fg = M.colors.fg, bg = M.colors.bg_dark },
    LualineC = { fg = M.colors.fg_dark, bg = M.colors.bg },
    LualineX = { fg = M.colors.fg_dark, bg = M.colors.bg },
    LualineY = { fg = M.colors.fg, bg = M.colors.bg_dark },
    LualineZ = { fg = M.colors.bg, bg = M.colors.green },

    -- Plugin Support: bufferline.nvim
    BufferLineFill = { bg = M.colors.bg_dark },
    BufferLineBackground = { fg = M.colors.fg_dark, bg = M.colors.bg_dark },
    BufferLineSelected = { fg = M.colors.fg, bg = M.colors.bg, bold = true },
    BufferLineIndicatorSelected = { fg = M.colors.orange, bg = M.colors.bg },

    -- Plugin Support: nvim-tree
    NvimTreeNormal = { fg = M.colors.fg, bg = M.colors.bg_dark },
    NvimTreeFolderName = { fg = M.colors.fg },
    NvimTreeFolderIcon = { fg = M.colors.yellow },
    NvimTreeOpenedFolderName = { fg = M.colors.orange },
    NvimTreeGitDirty = { fg = M.colors.red },
    NvimTreeGitNew = { fg = M.colors.green },
    NvimTreeGitDeleted = { fg = M.colors.red },

    -- Plugin Support: gitsigns.nvim
    GitSignsAdd = { fg = M.colors.green },
    GitSignsChange = { fg = M.colors.yellow },
    GitSignsDelete = { fg = M.colors.red },

    -- Plugin Support: indent-blankline.nvim
    IndentBlanklineChar = { fg = M.colors.selection },
    IndentBlanklineContextChar = { fg = M.colors.fg_dark },
}

function M.setup()
    -- Neovim settings
    vim.cmd('hi clear')
    if vim.fn.exists('syntax_on') then
        vim.cmd('syntax reset')
    end
    vim.o.termguicolors = true
    vim.g.colors_name = 'guttenbergovitz'

    -- Apply highlight groups
    for group, settings in pairs(M.groups) do
        vim.api.nvim_set_hl(0, group, settings)
    end
end

return M
