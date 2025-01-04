if vim.version().minor < 7 then
    vim.notify(
        "guttenbergovitz.nvim: you need Neovim >= 0.7",
        vim.log.levels.ERROR
    )
    return
end

-- Set name before clearing
vim.g.colors_name = "guttenbergovitz"

-- Load and setup the colorscheme
local colors = require("guttenbergovitz")

-- Clear existing highlights
vim.cmd.hi("clear")
if vim.fn.exists("syntax_on") then
    vim.cmd.syntax("reset")
end

-- Setup the colorscheme
colors.setup() 