if vim.version().minor < 7 then
    vim.notify(
        "guttenbergovitz.nvim: you need Neovim >= 0.7",
        vim.log.levels.ERROR
    )
    return
end

-- Try to load and setup the colorscheme
local ok, guttenbergovitz = pcall(require, "guttenbergovitz")
if not ok then
    vim.notify(
        "guttenbergovitz.nvim: could not load the colorscheme",
        vim.log.levels.ERROR
    )
    return
end

-- Use vim.api.nvim_set_hl for setting highlight groups
guttenbergovitz.setup()
