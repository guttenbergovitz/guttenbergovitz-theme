if vim.version().minor < 7 then
    vim.notify(
        "guttenbergovitz.nvim: you need Neovim >= 0.7",
        vim.log.levels.ERROR
    )
    return
end

vim.cmd.hi("clear")
if vim.fn.exists("syntax_on") then
    vim.cmd.syntax("reset")
end

require("guttenbergovitz").setup() 