local M = {}

-- Function to get color palette based on variant
local function get_colors(variant)
    variant = variant or vim.g.guttenbergovitz_variant or "dark"
    
    return variant == "light" and {
    -- Base colors (light theme)
    bg = "#f5f3f0",
    bg_dark = "#eae8e5",
    bg_light = "#ffffff",
    fg = "#5a4a3a",
    fg_dark = "#7a6a5a",
    fg_light = "#3a2a1a",
    
    -- Core colors (adjusted for light theme)
    red = "#8b4c4a",
    green = "#6b8860",
    yellow = "#b8995a",
    blue = "#5e7ea5",
    orange = "#b8784c",
    purple = "#956d7e",
    cyan = "#6b958f",
    
    -- UI colors
    selection = "#e8e6e3",
    comment = "#8a7a6a",
    cursor = "#5a4a3a",
    border = "#d8d6d3",
    type_hint = "#a4a2a0",
    
    -- Status colors
    error = "#cc6666",
    warn = "#de935f",
    info = "#5e7ea5",
    hint = "#6b958f",
    ok = "#6b8860",
    
    -- Diff colors
    diff_add = "#e8f0e8",
    diff_delete = "#f0e8e8",
    diff_change = "#f0f0e8",
    diff_text = "#e8e8d8",
    
    -- Git colors
    git_add = "#6b8860",
    git_change = "#b8995a",
    git_delete = "#8b4c4a",
    
    -- Terminal colors (16 ANSI colors)
    terminal = {
        black = "#3a2a1a",
        red = "#8b4c4a",
        green = "#6b8860",
        yellow = "#b8995a",
        blue = "#5e7ea5",
        magenta = "#956d7e",
        cyan = "#6b958f",
        white = "#7a6a5a",
        bright_black = "#5a4a3a",
        bright_red = "#cc6666",
        bright_green = "#8ba168",
        bright_yellow = "#d6b986",
        bright_blue = "#81a2be",
        bright_magenta = "#b294bb",
        bright_cyan = "#8abeb7",
        bright_white = "#f5f3f0",
    },
} or {
    -- Base colors (dark theme)
    bg = "#232326",
    bg_dark = "#1d1d20",
    bg_light = "#2a2a2d",
    fg = "#d4be98",
    fg_dark = "#a69a88",
    fg_light = "#e0d2a6",
    
    -- Core colors
    red = "#a96b69",
    green = "#89a87d",
    yellow = "#d6b986",
    blue = "#7a9ec2",
    orange = "#d79969",
    purple = "#b194a3",
    cyan = "#89b4ac",
    
    -- UI colors
    selection = "#3a3a3d",
    comment = "#a69a88",
    cursor = "#d4be98",
    border = "#3a3a3d",
    type_hint = "#44444b",
    
    -- Status colors
    error = "#cc6666",
    warn = "#de935f",
    info = "#81a2be",
    hint = "#9cc5c0",
    ok = "#b5bd68",
    
    -- Diff colors
    diff_add = "#2d3c2d",
    diff_delete = "#3c2d2d",
    diff_change = "#3c3c2d",
    diff_text = "#4c4c2d",
    
    -- Git colors
    git_add = "#89a87d",
    git_change = "#d6b986",
    git_delete = "#a96b69",
    
    -- Terminal colors (16 ANSI colors)
    terminal = {
        black = "#1d1d20",
        red = "#a96b69",
        green = "#89a87d",
        yellow = "#d6b986",
        blue = "#7a9ec2",
        magenta = "#b194a3",
        cyan = "#89b4ac",
        white = "#d4be98",
        bright_black = "#a69a88",
        bright_red = "#cc6666",
        bright_green = "#b5bd68",
        bright_yellow = "#f0c674",
        bright_blue = "#81a2be",
        bright_magenta = "#b294bb",
        bright_cyan = "#9cc5c0",
        bright_white = "#e0d2a6",
    },
}
end

-- Function to get highlight groups based on colors
local function get_groups(colors)
    -- Check if italics should be disabled globally
    local use_italics = vim.g.guttenbergovitz_italics ~= false
    
    return {
    -- Editor
    Normal = { fg = colors.fg, bg = colors.bg },
    NormalFloat = { fg = colors.fg, bg = colors.bg_dark },
    LineNr = { fg = colors.fg_dark },
    CursorLine = { bg = colors.selection },
    CursorLineNr = { fg = colors.fg },
    Visual = { bg = colors.selection },
    IncSearch = { fg = colors.bg, bg = colors.orange },
    Search = { fg = colors.bg, bg = colors.yellow },

    -- Syntax
    Comment = { fg = colors.comment, italic = use_italics },
    Constant = { fg = colors.yellow },
    String = { fg = colors.green },
    Identifier = { fg = colors.fg },
    Function = { fg = colors.orange },
    Statement = { fg = colors.red },
    Keyword = { fg = colors.red },
    Type = { fg = colors.yellow },
    Special = { fg = colors.orange },

    -- Interface
    StatusLine = { fg = colors.fg, bg = colors.bg_dark },
    StatusLineNC = { fg = colors.fg_dark, bg = colors.bg_dark },
    VertSplit = { fg = colors.selection },
    TabLine = { fg = colors.fg_dark, bg = colors.bg_dark },
    TabLineFill = { bg = colors.bg_dark },
    TabLineSel = { fg = colors.fg, bg = colors.bg },

    -- Plugin Support: vim-airline
    airline_a = { fg = colors.bg, bg = colors.orange, bold = true },
    airline_b = { fg = colors.fg, bg = colors.bg_dark },
    airline_c = { fg = colors.fg_dark, bg = colors.bg },
    airline_x = { fg = colors.fg_dark, bg = colors.bg },
    airline_y = { fg = colors.fg, bg = colors.bg_dark },
    airline_z = { fg = colors.bg, bg = colors.green, bold = true },
    airline_error = { fg = colors.red },
    airline_warning = { fg = colors.yellow },

    -- Plugin Support: lualine.nvim
    LualineA = { fg = colors.bg, bg = colors.orange },
    LualineB = { fg = colors.fg, bg = colors.bg_dark },
    LualineC = { fg = colors.fg_dark, bg = colors.bg },
    LualineX = { fg = colors.fg_dark, bg = colors.bg },
    LualineY = { fg = colors.fg, bg = colors.bg_dark },
    LualineZ = { fg = colors.bg, bg = colors.green },

    -- Plugin Support: bufferline.nvim
    BufferLineFill = { bg = colors.bg_dark },
    BufferLineBackground = { fg = colors.fg_dark, bg = colors.bg_dark },
    BufferLineSelected = { fg = colors.fg, bg = colors.bg, bold = true },
    BufferLineIndicatorSelected = { fg = colors.orange, bg = colors.bg },

    -- Plugin Support: nvim-tree
    NvimTreeNormal = { fg = colors.fg, bg = colors.bg_dark },
    NvimTreeFolderName = { fg = colors.fg },
    NvimTreeFolderIcon = { fg = colors.yellow },
    NvimTreeOpenedFolderName = { fg = colors.orange },
    NvimTreeGitDirty = { fg = colors.red },
    NvimTreeGitNew = { fg = colors.green },
    NvimTreeGitDeleted = { fg = colors.red },

    -- Plugin Support: gitsigns.nvim
    GitSignsAdd = { fg = colors.green },
    GitSignsChange = { fg = colors.yellow },
    GitSignsDelete = { fg = colors.red },

    -- Plugin Support: indent-blankline.nvim
    IndentBlanklineChar = { fg = colors.selection },
    IndentBlanklineContextChar = { fg = colors.fg_dark },
    IblIndent = { fg = colors.selection },
    IblScope = { fg = colors.fg_dark },

    -- TreeSitter highlight groups
    ["@comment"] = { fg = colors.comment, italic = use_italics },
    ["@comment.documentation"] = { fg = colors.comment, italic = use_italics },
    ["@error"] = { fg = colors.error },
    ["@none"] = { fg = colors.fg },
    ["@preproc"] = { fg = colors.purple },
    ["@define"] = { fg = colors.purple },
    ["@operator"] = { fg = colors.fg },

    -- Literals
    ["@string"] = { fg = colors.green },
    ["@string.documentation"] = { fg = colors.green },
    ["@string.regex"] = { fg = colors.cyan },
    ["@string.escape"] = { fg = colors.orange },
    ["@string.special"] = { fg = colors.orange },
    ["@character"] = { fg = colors.green },
    ["@character.special"] = { fg = colors.orange },
    ["@boolean"] = { fg = colors.purple },
    ["@number"] = { fg = colors.yellow },
    ["@float"] = { fg = colors.yellow },

    -- Functions
    ["@function"] = { fg = colors.orange },
    ["@function.call"] = { fg = colors.orange },
    ["@function.builtin"] = { fg = colors.orange },
    ["@function.macro"] = { fg = colors.purple },
    ["@method"] = { fg = colors.orange },
    ["@method.call"] = { fg = colors.orange },
    ["@constructor"] = { fg = colors.yellow },
    ["@parameter"] = { fg = colors.fg },

    -- Keywords
    ["@keyword"] = { fg = colors.red },
    ["@keyword.coroutine"] = { fg = colors.red },
    ["@keyword.function"] = { fg = colors.red },
    ["@keyword.operator"] = { fg = colors.red },
    ["@keyword.return"] = { fg = colors.red },
    ["@conditional"] = { fg = colors.red },
    ["@conditional.ternary"] = { fg = colors.red },
    ["@repeat"] = { fg = colors.red },
    ["@debug"] = { fg = colors.red },
    ["@label"] = { fg = colors.red },
    ["@include"] = { fg = colors.red },
    ["@exception"] = { fg = colors.red },

    -- Types
    ["@type"] = { fg = colors.yellow },
    ["@type.builtin"] = { fg = colors.yellow },
    ["@type.definition"] = { fg = colors.yellow },
    ["@type.qualifier"] = { fg = colors.red },
    ["@storageclass"] = { fg = colors.red },
    ["@attribute"] = { fg = colors.purple },
    ["@field"] = { fg = colors.fg },
    ["@property"] = { fg = colors.fg },

    -- Identifiers
    ["@variable"] = { fg = colors.fg },
    ["@variable.builtin"] = { fg = colors.purple },
    ["@constant"] = { fg = colors.yellow },
    ["@constant.builtin"] = { fg = colors.purple },
    ["@constant.macro"] = { fg = colors.purple },
    ["@namespace"] = { fg = colors.fg },
    ["@symbol"] = { fg = colors.fg },

    -- Text
    ["@text"] = { fg = colors.fg },
    ["@text.strong"] = { fg = colors.fg, bold = true },
    ["@text.emphasis"] = { fg = colors.fg, italic = use_italics },
    ["@text.underline"] = { fg = colors.fg, underline = true },
    ["@text.strike"] = { fg = colors.fg, strikethrough = true },
    ["@text.title"] = { fg = colors.orange, bold = true },
    ["@text.literal"] = { fg = colors.green },
    ["@text.uri"] = { fg = colors.cyan, underline = true },
    ["@text.math"] = { fg = colors.yellow },
    ["@text.environment"] = { fg = colors.purple },
    ["@text.environment.name"] = { fg = colors.yellow },
    ["@text.reference"] = { fg = colors.cyan },
    ["@text.todo"] = { fg = colors.bg, bg = colors.info },
    ["@text.note"] = { fg = colors.bg, bg = colors.hint },
    ["@text.warning"] = { fg = colors.bg, bg = colors.warn },
    ["@text.danger"] = { fg = colors.bg, bg = colors.error },

    -- Tags
    ["@tag"] = { fg = colors.red },
    ["@tag.attribute"] = { fg = colors.yellow },
    ["@tag.delimiter"] = { fg = colors.fg_dark },

    -- Punctuation
    ["@punctuation"] = { fg = colors.fg },
    ["@punctuation.delimiter"] = { fg = colors.fg },
    ["@punctuation.bracket"] = { fg = colors.fg },
    ["@punctuation.special"] = { fg = colors.orange },

    -- Conceal
    ["@conceal"] = { fg = colors.fg_dark },

    -- Spell
    ["@spell"] = { fg = colors.fg },
    ["@nospell"] = { fg = colors.fg },

    -- LSP Diagnostic
    DiagnosticError = { fg = colors.error },
    DiagnosticWarn = { fg = colors.warn },
    DiagnosticInfo = { fg = colors.info },
    DiagnosticHint = { fg = colors.hint },
    DiagnosticOk = { fg = colors.ok },
    
    -- LSP Diagnostic Virtual Text
    DiagnosticVirtualTextError = { fg = colors.error, bg = colors.bg },
    DiagnosticVirtualTextWarn = { fg = colors.warn, bg = colors.bg },
    DiagnosticVirtualTextInfo = { fg = colors.info, bg = colors.bg },
    DiagnosticVirtualTextHint = { fg = colors.hint, bg = colors.bg },
    DiagnosticVirtualTextOk = { fg = colors.ok, bg = colors.bg },
    
    -- LSP Diagnostic Underline
    DiagnosticUnderlineError = { sp = colors.error, undercurl = true },
    DiagnosticUnderlineWarn = { sp = colors.warn, undercurl = true },
    DiagnosticUnderlineInfo = { sp = colors.info, undercurl = true },
    DiagnosticUnderlineHint = { sp = colors.hint, undercurl = true },
    DiagnosticUnderlineOk = { sp = colors.ok, undercurl = true },
    
    -- LSP Diagnostic Floating Window
    DiagnosticFloatingError = { fg = colors.error, bg = colors.bg_dark },
    DiagnosticFloatingWarn = { fg = colors.warn, bg = colors.bg_dark },
    DiagnosticFloatingInfo = { fg = colors.info, bg = colors.bg_dark },
    DiagnosticFloatingHint = { fg = colors.hint, bg = colors.bg_dark },
    DiagnosticFloatingOk = { fg = colors.ok, bg = colors.bg_dark },
    
    -- LSP Diagnostic Signs
    DiagnosticSignError = { fg = colors.error, bg = colors.bg },
    DiagnosticSignWarn = { fg = colors.warn, bg = colors.bg },
    DiagnosticSignInfo = { fg = colors.info, bg = colors.bg },
    DiagnosticSignHint = { fg = colors.hint, bg = colors.bg },
    DiagnosticSignOk = { fg = colors.ok, bg = colors.bg },

    -- LSP Semantic Token Groups
    ["@lsp.type.class"] = { fg = colors.yellow },
    ["@lsp.type.decorator"] = { fg = colors.purple },
    ["@lsp.type.enum"] = { fg = colors.yellow },
    ["@lsp.type.enumMember"] = { fg = colors.purple },
    ["@lsp.type.function"] = { fg = colors.orange },
    ["@lsp.type.interface"] = { fg = colors.yellow },
    ["@lsp.type.macro"] = { fg = colors.purple },
    ["@lsp.type.method"] = { fg = colors.orange },
    ["@lsp.type.namespace"] = { fg = colors.fg },
    ["@lsp.type.parameter"] = { fg = colors.fg },
    ["@lsp.type.property"] = { fg = colors.fg },
    ["@lsp.type.struct"] = { fg = colors.yellow },
    ["@lsp.type.type"] = { fg = colors.yellow },
    ["@lsp.type.typeParameter"] = { fg = colors.yellow },
    ["@lsp.type.variable"] = { fg = colors.fg },

    -- TypeScript specific highlighting
    ["@type.typescript"] = { fg = colors.yellow },
    ["@type.builtin.typescript"] = { fg = colors.yellow },
    ["@keyword.type.typescript"] = { fg = colors.red },
    ["@keyword.modifier.typescript"] = { fg = colors.red },
    ["@keyword.operator.type.typescript"] = { fg = colors.red },
    ["@punctuation.bracket.typescript"] = { fg = colors.fg },
    ["@punctuation.delimiter.typescript"] = { fg = colors.fg },
    ["@operator.typescript"] = { fg = colors.red },
    
    -- JavaScript/TypeScript specific tokens
    ["@variable.builtin.javascript"] = { fg = colors.purple },
    ["@variable.builtin.typescript"] = { fg = colors.purple },
    ["@type.definition.typescript"] = { fg = colors.yellow },
    ["@function.call.typescript"] = { fg = colors.orange },
    ["@method.call.typescript"] = { fg = colors.orange },
    ["@constructor.typescript"] = { fg = colors.yellow },
    
    -- Additional TypeScript/JavaScript groups
    ["@keyword.import"] = { fg = colors.red },
    ["@keyword.export"] = { fg = colors.red },
    ["@module"] = { fg = colors.fg },
    ["@string.special.url"] = { fg = colors.cyan },
    ["@string.special.path"] = { fg = colors.cyan },
    ["@variable.parameter.builtin"] = { fg = colors.purple },
    ["@variable.member"] = { fg = colors.fg },
    ["@property"] = { fg = colors.fg },
    ["@lsp.type.selfKeyword"] = { fg = colors.purple },
    ["@lsp.type.builtinType"] = { fg = colors.yellow },
    ["@lsp.mod.declaration"] = { fg = colors.fg },
    ["@lsp.mod.readonly"] = { fg = colors.fg },
    ["@lsp.mod.static"] = { fg = colors.red },

    -- LSP References
    LspReferenceText = { bg = colors.selection },
    LspReferenceRead = { bg = colors.selection },
    LspReferenceWrite = { bg = colors.selection },
    
    -- LSP Signature Help
    LspSignatureActiveParameter = { bg = colors.selection, bold = true },
    
    -- LSP Inlay Hints (type hints)
    LspInlayHint = { fg = colors.type_hint, bg = colors.bg },

    -- Modern UI Elements
    -- Floating windows
    NormalFloat = { fg = colors.fg, bg = colors.bg_dark },
    FloatBorder = { fg = colors.border, bg = colors.bg_dark },
    FloatTitle = { fg = colors.orange, bg = colors.bg_dark, bold = true },
    
    -- Popups
    Pmenu = { fg = colors.fg, bg = colors.bg_dark },
    PmenuSel = { fg = colors.fg, bg = colors.selection },
    PmenuSbar = { bg = colors.bg_light },
    PmenuThumb = { bg = colors.fg_dark },
    PmenuKind = { fg = colors.yellow, bg = colors.bg_dark },
    PmenuKindSel = { fg = colors.yellow, bg = colors.selection },
    PmenuExtra = { fg = colors.fg_dark, bg = colors.bg_dark },
    PmenuExtraSel = { fg = colors.fg_dark, bg = colors.selection },
    
    -- Wild menu
    WildMenu = { fg = colors.fg, bg = colors.selection },
    
    -- Cursor
    Cursor = { fg = colors.bg, bg = colors.cursor },
    CursorIM = { fg = colors.bg, bg = colors.cursor },
    
    -- Folding
    Folded = { fg = colors.fg_dark, bg = colors.bg_light },
    FoldColumn = { fg = colors.fg_dark, bg = colors.bg },
    
    -- Spell checking
    SpellBad = { sp = colors.error, undercurl = true },
    SpellCap = { sp = colors.warn, undercurl = true },
    SpellLocal = { sp = colors.info, undercurl = true },
    SpellRare = { sp = colors.hint, undercurl = true },
    
    -- Diff
    DiffAdd = { fg = colors.git_add, bg = colors.diff_add },
    DiffChange = { fg = colors.git_change, bg = colors.diff_change },
    DiffDelete = { fg = colors.git_delete, bg = colors.diff_delete },
    DiffText = { fg = colors.git_change, bg = colors.diff_text },
    
    -- Messages
    MsgArea = { fg = colors.fg, bg = colors.bg },
    MsgSeparator = { fg = colors.border, bg = colors.bg },
    
    -- Question
    Question = { fg = colors.green },
    
    -- QuickFix
    QuickFixLine = { bg = colors.selection },
    
    -- Error messages
    ErrorMsg = { fg = colors.error },
    WarningMsg = { fg = colors.warn },
    
    -- More prompt
    MoreMsg = { fg = colors.green },
    
    -- Mode messages
    ModeMsg = { fg = colors.fg },
    
    -- Directory
    Directory = { fg = colors.blue },
    
    -- Title
    Title = { fg = colors.orange, bold = true },
    
    -- Substitute
    Substitute = { fg = colors.bg, bg = colors.orange },
    
    -- Whitespace
    Whitespace = { fg = colors.bg_light },
    NonText = { fg = colors.bg_light },
    SpecialKey = { fg = colors.bg_light },
    
    -- Concealed
    Conceal = { fg = colors.fg_dark },
    
    -- Color column
    ColorColumn = { bg = colors.bg_light },
    
    -- Sign column
    SignColumn = { fg = colors.fg_dark, bg = colors.bg },
    
    -- Matching
    MatchParen = { fg = colors.orange, bold = true },

    -- Plugin Support: Telescope
    TelescopeNormal = { fg = colors.fg, bg = colors.bg_dark },
    TelescopeBorder = { fg = colors.border, bg = colors.bg_dark },
    TelescopePromptBorder = { fg = colors.border, bg = colors.bg_dark },
    TelescopeResultsBorder = { fg = colors.border, bg = colors.bg_dark },
    TelescopePreviewBorder = { fg = colors.border, bg = colors.bg_dark },
    TelescopeSelection = { fg = colors.fg, bg = colors.selection },
    TelescopeSelectionCaret = { fg = colors.orange, bg = colors.selection },
    TelescopeMultiSelection = { fg = colors.purple, bg = colors.selection },
    TelescopeMatching = { fg = colors.orange, bold = true },
    TelescopePromptPrefix = { fg = colors.orange },
    TelescopePromptCounter = { fg = colors.fg_dark },
    TelescopeTitle = { fg = colors.orange, bold = true },
    TelescopePreviewTitle = { fg = colors.green, bold = true },
    TelescopeResultsTitle = { fg = colors.blue, bold = true },
    TelescopePromptTitle = { fg = colors.orange, bold = true },

    -- Plugin Support: nvim-cmp
    CmpItemAbbr = { fg = colors.fg },
    CmpItemAbbrDeprecated = { fg = colors.fg_dark, strikethrough = true },
    CmpItemAbbrMatch = { fg = colors.orange, bold = true },
    CmpItemAbbrMatchFuzzy = { fg = colors.orange, bold = true },
    CmpItemKind = { fg = colors.yellow },
    CmpItemKindDefault = { fg = colors.yellow },
    CmpItemMenu = { fg = colors.fg_dark },
    CmpItemKindText = { fg = colors.fg },
    CmpItemKindMethod = { fg = colors.orange },
    CmpItemKindFunction = { fg = colors.orange },
    CmpItemKindConstructor = { fg = colors.yellow },
    CmpItemKindField = { fg = colors.fg },
    CmpItemKindVariable = { fg = colors.fg },
    CmpItemKindClass = { fg = colors.yellow },
    CmpItemKindInterface = { fg = colors.yellow },
    CmpItemKindModule = { fg = colors.blue },
    CmpItemKindProperty = { fg = colors.fg },
    CmpItemKindUnit = { fg = colors.yellow },
    CmpItemKindValue = { fg = colors.yellow },
    CmpItemKindEnum = { fg = colors.yellow },
    CmpItemKindKeyword = { fg = colors.red },
    CmpItemKindSnippet = { fg = colors.green },
    CmpItemKindColor = { fg = colors.purple },
    CmpItemKindFile = { fg = colors.blue },
    CmpItemKindReference = { fg = colors.cyan },
    CmpItemKindFolder = { fg = colors.blue },
    CmpItemKindEnumMember = { fg = colors.purple },
    CmpItemKindConstant = { fg = colors.yellow },
    CmpItemKindStruct = { fg = colors.yellow },
    CmpItemKindEvent = { fg = colors.orange },
    CmpItemKindOperator = { fg = colors.fg },
    CmpItemKindTypeParameter = { fg = colors.yellow },

    -- Plugin Support: Which-key
    WhichKey = { fg = colors.orange, bold = true },
    WhichKeyGroup = { fg = colors.blue },
    WhichKeyDesc = { fg = colors.fg },
    WhichKeySeperator = { fg = colors.fg_dark },
    WhichKeyFloat = { bg = colors.bg_dark },
    WhichKeyBorder = { fg = colors.border, bg = colors.bg_dark },
    WhichKeyValue = { fg = colors.green },

    -- Plugin Support: Neo-tree
    NeoTreeNormal = { fg = colors.fg, bg = colors.bg_dark },
    NeoTreeNormalNC = { fg = colors.fg, bg = colors.bg_dark },
    NeoTreeDirectoryName = { fg = colors.fg },
    NeoTreeDirectoryIcon = { fg = colors.blue },
    NeoTreeRootName = { fg = colors.orange, bold = true },
    NeoTreeFileName = { fg = colors.fg },
    NeoTreeFileIcon = { fg = colors.fg },
    NeoTreeFileNameOpened = { fg = colors.orange },
    NeoTreeIndentMarker = { fg = colors.fg_dark },
    NeoTreeExpander = { fg = colors.fg_dark },
    NeoTreeDotfile = { fg = colors.fg_dark },
    NeoTreeGitAdded = { fg = colors.git_add },
    NeoTreeGitDeleted = { fg = colors.git_delete },
    NeoTreeGitModified = { fg = colors.git_change },
    NeoTreeGitConflict = { fg = colors.error },
    NeoTreeGitUntracked = { fg = colors.hint },
    NeoTreeGitIgnored = { fg = colors.fg_dark },
    NeoTreeGitStaged = { fg = colors.git_add },
    NeoTreeFloatBorder = { fg = colors.border, bg = colors.bg_dark },
    NeoTreeFloatTitle = { fg = colors.orange, bg = colors.bg_dark, bold = true },
    NeoTreeTitleBar = { fg = colors.fg, bg = colors.bg_light },

    -- Plugin Support: DAP (Debug Adapter Protocol)
    DapBreakpoint = { fg = colors.error },
    DapBreakpointCondition = { fg = colors.warn },
    DapBreakpointRejected = { fg = colors.fg_dark },
    DapLogPoint = { fg = colors.info },
    DapStopped = { fg = colors.ok },
    DapUIVariable = { fg = colors.fg },
    DapUIScope = { fg = colors.cyan },
    DapUIType = { fg = colors.purple },
    DapUIValue = { fg = colors.fg },
    DapUIModifiedValue = { fg = colors.warn, bold = true },
    DapUIDecoration = { fg = colors.cyan },
    DapUIThread = { fg = colors.green },
    DapUIStoppedThread = { fg = colors.cyan },
    DapUIFrameName = { fg = colors.fg },
    DapUISource = { fg = colors.purple },
    DapUILineNumber = { fg = colors.cyan },
    DapUIFloatBorder = { fg = colors.border },
    DapUIWatchesEmpty = { fg = colors.error },
    DapUIWatchesValue = { fg = colors.green },
    DapUIWatchesError = { fg = colors.error },
    DapUIBreakpointsPath = { fg = colors.cyan },
    DapUIBreakpointsInfo = { fg = colors.green },
    DapUIBreakpointsCurrentLine = { fg = colors.green, bold = true },
    DapUIBreakpointsLine = { fg = colors.cyan },
    DapUIBreakpointsDisabledLine = { fg = colors.fg_dark },
    DapUICurrentFrameName = { fg = colors.green, bold = true },
    DapUIStepOver = { fg = colors.cyan },
    DapUIStepInto = { fg = colors.cyan },
    DapUIStepBack = { fg = colors.cyan },
    DapUIStepOut = { fg = colors.cyan },
    DapUIStop = { fg = colors.error },
    DapUIPlayPause = { fg = colors.green },
    DapUIRestart = { fg = colors.green },
    DapUIUnavailable = { fg = colors.fg_dark },
    }
end

-- Initialize theme
M.variant = vim.g.guttenbergovitz_variant or "dark"
M.colors = get_colors(M.variant)
M.groups = get_groups(M.colors)

function M.setup()
    -- Version compatibility check
    local nvim_version = vim.version()
    if nvim_version.major == 0 and nvim_version.minor < 7 then
        vim.notify(
            "guttenbergovitz.nvim: requires Neovim >= 0.7.0",
            vim.log.levels.ERROR
        )
        return
    end

    -- Refresh variant and colors
    M.variant = vim.g.guttenbergovitz_variant or "dark"
    M.colors = get_colors(M.variant)
    M.groups = get_groups(M.colors)

    -- Neovim settings
    vim.cmd('hi clear')
    if vim.fn.exists('syntax_on') then
        vim.cmd('syntax reset')
    end
    vim.o.termguicolors = true
    vim.g.colors_name = M.variant == "light" and 'guttenbergovitz-light' or 'guttenbergovitz'

    -- Apply highlight groups with error handling
    local function safe_set_hl(group, settings)
        local ok, err = pcall(vim.api.nvim_set_hl, 0, group, settings)
        if not ok then
            vim.notify(
                string.format("guttenbergovitz.nvim: Failed to set highlight %s: %s", group, err),
                vim.log.levels.WARN
            )
        end
    end

    for group, settings in pairs(M.groups) do
        safe_set_hl(group, settings)
    end
    
    -- Set terminal colors with version check
    if nvim_version.major > 0 or nvim_version.minor >= 7 then
        vim.g.terminal_color_0 = M.colors.terminal.black
        vim.g.terminal_color_1 = M.colors.terminal.red
        vim.g.terminal_color_2 = M.colors.terminal.green
        vim.g.terminal_color_3 = M.colors.terminal.yellow
        vim.g.terminal_color_4 = M.colors.terminal.blue
        vim.g.terminal_color_5 = M.colors.terminal.magenta
        vim.g.terminal_color_6 = M.colors.terminal.cyan
        vim.g.terminal_color_7 = M.colors.terminal.white
        vim.g.terminal_color_8 = M.colors.terminal.bright_black
        vim.g.terminal_color_9 = M.colors.terminal.bright_red
        vim.g.terminal_color_10 = M.colors.terminal.bright_green
        vim.g.terminal_color_11 = M.colors.terminal.bright_yellow
        vim.g.terminal_color_12 = M.colors.terminal.bright_blue
        vim.g.terminal_color_13 = M.colors.terminal.bright_magenta
        vim.g.terminal_color_14 = M.colors.terminal.bright_cyan
        vim.g.terminal_color_15 = M.colors.terminal.bright_white
    end
end

-- Function to switch between light and dark themes
function M.toggle()
    local current_variant = vim.g.guttenbergovitz_variant or "dark"
    if current_variant == "light" then
        vim.g.guttenbergovitz_variant = "dark"
    else
        vim.g.guttenbergovitz_variant = "light"
    end
    M.setup()
end

-- Function to set specific variant
function M.set_variant(variant)
    if variant == "light" or variant == "dark" then
        vim.g.guttenbergovitz_variant = variant
        M.setup()
    else
        vim.notify("guttenbergovitz.nvim: Invalid variant. Use 'light' or 'dark'", vim.log.levels.ERROR)
    end
end

return M
