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
}

function M.setup()
    -- Neovim settings
    vim.cmd('hi clear')
    if vim.fn.exists('syntax_on') then
        vim.cmd('syntax reset')
    end
    vim.o.termguicolors = true
    vim.g.colors_name = 'guttenbergovitz'

    -- Apply color groups
    for group, settings in pairs(M.groups) do
        vim.api.nvim_set_hl(0, group, settings)
    end
end

return M 