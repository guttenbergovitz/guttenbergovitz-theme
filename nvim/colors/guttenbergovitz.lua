-- Check Neovim version
if vim.version().minor < 7 then
    vim.notify(
        "guttenbergovitz.nvim: you need Neovim >= 0.7",
        vim.log.levels.ERROR
    )
    return
end

-- Set colorscheme name before anything else
vim.g.colors_name = "guttenbergovitz"

-- Enable true colors
vim.opt.termguicolors = true

-- Clear existing highlights
vim.cmd("hi clear")
if vim.fn.exists("syntax_on") then
    vim.cmd("syntax reset")
end

-- Try to load and setup the colorscheme
local ok, colors = pcall(require, "guttenbergovitz")
if not ok then
    vim.notify(
        "guttenbergovitz.nvim: could not load the colorscheme: " .. colors,
        vim.log.levels.ERROR
    )
    return
end

-- Setup the colorscheme
colors.setup() 