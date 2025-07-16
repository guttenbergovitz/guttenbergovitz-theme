local M = {}

-- Color palette
M.colors = {
    -- Base colors
    bg = "#232326",
    bg_dark = "#1d1d20",
    bg_light = "#2a2a2d",
    fg = "#d4be98",
    fg_dark = "#7c7c7c",
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
    comment = "#7c7c7c",
    cursor = "#d4be98",
    border = "#3a3a3d",
    
    -- Status colors
    error = "#cc6666",
    warn = "#de935f",
    info = "#81a2be",
    hint = "#8abeb7",
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
        bright_black = "#7c7c7c",
        bright_red = "#cc6666",
        bright_green = "#b5bd68",
        bright_yellow = "#f0c674",
        bright_blue = "#81a2be",
        bright_magenta = "#b294bb",
        bright_cyan = "#8abeb7",
        bright_white = "#e0d2a6",
    },
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
    IblIndent = { fg = M.colors.selection },
    IblScope = { fg = M.colors.fg_dark },

    -- TreeSitter highlight groups
    ["@comment"] = { fg = M.colors.comment, italic = true },
    ["@comment.documentation"] = { fg = M.colors.comment, italic = true },
    ["@error"] = { fg = M.colors.error },
    ["@none"] = { fg = M.colors.fg },
    ["@preproc"] = { fg = M.colors.purple },
    ["@define"] = { fg = M.colors.purple },
    ["@operator"] = { fg = M.colors.fg },

    -- Literals
    ["@string"] = { fg = M.colors.green },
    ["@string.documentation"] = { fg = M.colors.green },
    ["@string.regex"] = { fg = M.colors.cyan },
    ["@string.escape"] = { fg = M.colors.orange },
    ["@string.special"] = { fg = M.colors.orange },
    ["@character"] = { fg = M.colors.green },
    ["@character.special"] = { fg = M.colors.orange },
    ["@boolean"] = { fg = M.colors.purple },
    ["@number"] = { fg = M.colors.yellow },
    ["@float"] = { fg = M.colors.yellow },

    -- Functions
    ["@function"] = { fg = M.colors.orange },
    ["@function.call"] = { fg = M.colors.orange },
    ["@function.builtin"] = { fg = M.colors.orange },
    ["@function.macro"] = { fg = M.colors.purple },
    ["@method"] = { fg = M.colors.orange },
    ["@method.call"] = { fg = M.colors.orange },
    ["@constructor"] = { fg = M.colors.yellow },
    ["@parameter"] = { fg = M.colors.fg },

    -- Keywords
    ["@keyword"] = { fg = M.colors.red },
    ["@keyword.coroutine"] = { fg = M.colors.red },
    ["@keyword.function"] = { fg = M.colors.red },
    ["@keyword.operator"] = { fg = M.colors.red },
    ["@keyword.return"] = { fg = M.colors.red },
    ["@conditional"] = { fg = M.colors.red },
    ["@conditional.ternary"] = { fg = M.colors.red },
    ["@repeat"] = { fg = M.colors.red },
    ["@debug"] = { fg = M.colors.red },
    ["@label"] = { fg = M.colors.red },
    ["@include"] = { fg = M.colors.red },
    ["@exception"] = { fg = M.colors.red },

    -- Types
    ["@type"] = { fg = M.colors.yellow },
    ["@type.builtin"] = { fg = M.colors.yellow },
    ["@type.definition"] = { fg = M.colors.yellow },
    ["@type.qualifier"] = { fg = M.colors.red },
    ["@storageclass"] = { fg = M.colors.red },
    ["@attribute"] = { fg = M.colors.purple },
    ["@field"] = { fg = M.colors.fg },
    ["@property"] = { fg = M.colors.fg },

    -- Identifiers
    ["@variable"] = { fg = M.colors.fg },
    ["@variable.builtin"] = { fg = M.colors.purple },
    ["@constant"] = { fg = M.colors.yellow },
    ["@constant.builtin"] = { fg = M.colors.purple },
    ["@constant.macro"] = { fg = M.colors.purple },
    ["@namespace"] = { fg = M.colors.fg },
    ["@symbol"] = { fg = M.colors.fg },

    -- Text
    ["@text"] = { fg = M.colors.fg },
    ["@text.strong"] = { fg = M.colors.fg, bold = true },
    ["@text.emphasis"] = { fg = M.colors.fg, italic = true },
    ["@text.underline"] = { fg = M.colors.fg, underline = true },
    ["@text.strike"] = { fg = M.colors.fg, strikethrough = true },
    ["@text.title"] = { fg = M.colors.orange, bold = true },
    ["@text.literal"] = { fg = M.colors.green },
    ["@text.uri"] = { fg = M.colors.cyan, underline = true },
    ["@text.math"] = { fg = M.colors.yellow },
    ["@text.environment"] = { fg = M.colors.purple },
    ["@text.environment.name"] = { fg = M.colors.yellow },
    ["@text.reference"] = { fg = M.colors.cyan },
    ["@text.todo"] = { fg = M.colors.bg, bg = M.colors.info },
    ["@text.note"] = { fg = M.colors.bg, bg = M.colors.hint },
    ["@text.warning"] = { fg = M.colors.bg, bg = M.colors.warn },
    ["@text.danger"] = { fg = M.colors.bg, bg = M.colors.error },

    -- Tags
    ["@tag"] = { fg = M.colors.red },
    ["@tag.attribute"] = { fg = M.colors.yellow },
    ["@tag.delimiter"] = { fg = M.colors.fg_dark },

    -- Punctuation
    ["@punctuation"] = { fg = M.colors.fg },
    ["@punctuation.delimiter"] = { fg = M.colors.fg },
    ["@punctuation.bracket"] = { fg = M.colors.fg },
    ["@punctuation.special"] = { fg = M.colors.orange },

    -- Conceal
    ["@conceal"] = { fg = M.colors.fg_dark },

    -- Spell
    ["@spell"] = { fg = M.colors.fg },
    ["@nospell"] = { fg = M.colors.fg },

    -- LSP Diagnostic
    DiagnosticError = { fg = M.colors.error },
    DiagnosticWarn = { fg = M.colors.warn },
    DiagnosticInfo = { fg = M.colors.info },
    DiagnosticHint = { fg = M.colors.hint },
    DiagnosticOk = { fg = M.colors.ok },
    
    -- LSP Diagnostic Virtual Text
    DiagnosticVirtualTextError = { fg = M.colors.error, bg = M.colors.bg },
    DiagnosticVirtualTextWarn = { fg = M.colors.warn, bg = M.colors.bg },
    DiagnosticVirtualTextInfo = { fg = M.colors.info, bg = M.colors.bg },
    DiagnosticVirtualTextHint = { fg = M.colors.hint, bg = M.colors.bg },
    DiagnosticVirtualTextOk = { fg = M.colors.ok, bg = M.colors.bg },
    
    -- LSP Diagnostic Underline
    DiagnosticUnderlineError = { sp = M.colors.error, undercurl = true },
    DiagnosticUnderlineWarn = { sp = M.colors.warn, undercurl = true },
    DiagnosticUnderlineInfo = { sp = M.colors.info, undercurl = true },
    DiagnosticUnderlineHint = { sp = M.colors.hint, undercurl = true },
    DiagnosticUnderlineOk = { sp = M.colors.ok, undercurl = true },
    
    -- LSP Diagnostic Floating Window
    DiagnosticFloatingError = { fg = M.colors.error, bg = M.colors.bg_dark },
    DiagnosticFloatingWarn = { fg = M.colors.warn, bg = M.colors.bg_dark },
    DiagnosticFloatingInfo = { fg = M.colors.info, bg = M.colors.bg_dark },
    DiagnosticFloatingHint = { fg = M.colors.hint, bg = M.colors.bg_dark },
    DiagnosticFloatingOk = { fg = M.colors.ok, bg = M.colors.bg_dark },
    
    -- LSP Diagnostic Signs
    DiagnosticSignError = { fg = M.colors.error, bg = M.colors.bg },
    DiagnosticSignWarn = { fg = M.colors.warn, bg = M.colors.bg },
    DiagnosticSignInfo = { fg = M.colors.info, bg = M.colors.bg },
    DiagnosticSignHint = { fg = M.colors.hint, bg = M.colors.bg },
    DiagnosticSignOk = { fg = M.colors.ok, bg = M.colors.bg },

    -- LSP Semantic Token Groups
    ["@lsp.type.class"] = { fg = M.colors.yellow },
    ["@lsp.type.decorator"] = { fg = M.colors.purple },
    ["@lsp.type.enum"] = { fg = M.colors.yellow },
    ["@lsp.type.enumMember"] = { fg = M.colors.purple },
    ["@lsp.type.function"] = { fg = M.colors.orange },
    ["@lsp.type.interface"] = { fg = M.colors.yellow },
    ["@lsp.type.macro"] = { fg = M.colors.purple },
    ["@lsp.type.method"] = { fg = M.colors.orange },
    ["@lsp.type.namespace"] = { fg = M.colors.fg },
    ["@lsp.type.parameter"] = { fg = M.colors.fg },
    ["@lsp.type.property"] = { fg = M.colors.fg },
    ["@lsp.type.struct"] = { fg = M.colors.yellow },
    ["@lsp.type.type"] = { fg = M.colors.yellow },
    ["@lsp.type.typeParameter"] = { fg = M.colors.yellow },
    ["@lsp.type.variable"] = { fg = M.colors.fg },

    -- TypeScript specific highlighting
    ["@type.typescript"] = { fg = M.colors.yellow },
    ["@type.builtin.typescript"] = { fg = M.colors.yellow },
    ["@keyword.type.typescript"] = { fg = M.colors.red },
    ["@keyword.modifier.typescript"] = { fg = M.colors.red },
    ["@keyword.operator.type.typescript"] = { fg = M.colors.red },
    ["@punctuation.bracket.typescript"] = { fg = M.colors.fg },
    ["@punctuation.delimiter.typescript"] = { fg = M.colors.fg },
    ["@operator.typescript"] = { fg = M.colors.red },
    
    -- JavaScript/TypeScript specific tokens
    ["@variable.builtin.javascript"] = { fg = M.colors.purple },
    ["@variable.builtin.typescript"] = { fg = M.colors.purple },
    ["@type.definition.typescript"] = { fg = M.colors.yellow },
    ["@function.call.typescript"] = { fg = M.colors.orange },
    ["@method.call.typescript"] = { fg = M.colors.orange },
    ["@constructor.typescript"] = { fg = M.colors.yellow },
    
    -- Additional TypeScript/JavaScript groups
    ["@keyword.import"] = { fg = M.colors.red },
    ["@keyword.export"] = { fg = M.colors.red },
    ["@module"] = { fg = M.colors.fg },
    ["@string.special.url"] = { fg = M.colors.cyan },
    ["@string.special.path"] = { fg = M.colors.cyan },
    ["@variable.parameter.builtin"] = { fg = M.colors.purple },
    ["@variable.member"] = { fg = M.colors.fg },
    ["@property"] = { fg = M.colors.fg },
    ["@lsp.type.selfKeyword"] = { fg = M.colors.purple },
    ["@lsp.type.builtinType"] = { fg = M.colors.yellow },
    ["@lsp.mod.declaration"] = { fg = M.colors.fg },
    ["@lsp.mod.readonly"] = { fg = M.colors.fg },
    ["@lsp.mod.static"] = { fg = M.colors.red },

    -- LSP References
    LspReferenceText = { bg = M.colors.selection },
    LspReferenceRead = { bg = M.colors.selection },
    LspReferenceWrite = { bg = M.colors.selection },
    
    -- LSP Signature Help
    LspSignatureActiveParameter = { bg = M.colors.selection, bold = true },

    -- Modern UI Elements
    -- Floating windows
    NormalFloat = { fg = M.colors.fg, bg = M.colors.bg_dark },
    FloatBorder = { fg = M.colors.border, bg = M.colors.bg_dark },
    FloatTitle = { fg = M.colors.orange, bg = M.colors.bg_dark, bold = true },
    
    -- Popups
    Pmenu = { fg = M.colors.fg, bg = M.colors.bg_dark },
    PmenuSel = { fg = M.colors.fg, bg = M.colors.selection },
    PmenuSbar = { bg = M.colors.bg_light },
    PmenuThumb = { bg = M.colors.fg_dark },
    PmenuKind = { fg = M.colors.yellow, bg = M.colors.bg_dark },
    PmenuKindSel = { fg = M.colors.yellow, bg = M.colors.selection },
    PmenuExtra = { fg = M.colors.fg_dark, bg = M.colors.bg_dark },
    PmenuExtraSel = { fg = M.colors.fg_dark, bg = M.colors.selection },
    
    -- Wild menu
    WildMenu = { fg = M.colors.fg, bg = M.colors.selection },
    
    -- Cursor
    Cursor = { fg = M.colors.bg, bg = M.colors.cursor },
    CursorIM = { fg = M.colors.bg, bg = M.colors.cursor },
    
    -- Folding
    Folded = { fg = M.colors.fg_dark, bg = M.colors.bg_light },
    FoldColumn = { fg = M.colors.fg_dark, bg = M.colors.bg },
    
    -- Spell checking
    SpellBad = { sp = M.colors.error, undercurl = true },
    SpellCap = { sp = M.colors.warn, undercurl = true },
    SpellLocal = { sp = M.colors.info, undercurl = true },
    SpellRare = { sp = M.colors.hint, undercurl = true },
    
    -- Diff
    DiffAdd = { fg = M.colors.git_add, bg = M.colors.diff_add },
    DiffChange = { fg = M.colors.git_change, bg = M.colors.diff_change },
    DiffDelete = { fg = M.colors.git_delete, bg = M.colors.diff_delete },
    DiffText = { fg = M.colors.git_change, bg = M.colors.diff_text },
    
    -- Messages
    MsgArea = { fg = M.colors.fg, bg = M.colors.bg },
    MsgSeparator = { fg = M.colors.border, bg = M.colors.bg },
    
    -- Question
    Question = { fg = M.colors.green },
    
    -- QuickFix
    QuickFixLine = { bg = M.colors.selection },
    
    -- Error messages
    ErrorMsg = { fg = M.colors.error },
    WarningMsg = { fg = M.colors.warn },
    
    -- More prompt
    MoreMsg = { fg = M.colors.green },
    
    -- Mode messages
    ModeMsg = { fg = M.colors.fg },
    
    -- Directory
    Directory = { fg = M.colors.blue },
    
    -- Title
    Title = { fg = M.colors.orange, bold = true },
    
    -- Substitute
    Substitute = { fg = M.colors.bg, bg = M.colors.orange },
    
    -- Whitespace
    Whitespace = { fg = M.colors.bg_light },
    NonText = { fg = M.colors.bg_light },
    SpecialKey = { fg = M.colors.bg_light },
    
    -- Concealed
    Conceal = { fg = M.colors.fg_dark },
    
    -- Color column
    ColorColumn = { bg = M.colors.bg_light },
    
    -- Sign column
    SignColumn = { fg = M.colors.fg_dark, bg = M.colors.bg },
    
    -- Matching
    MatchParen = { fg = M.colors.orange, bold = true },

    -- Plugin Support: Telescope
    TelescopeNormal = { fg = M.colors.fg, bg = M.colors.bg_dark },
    TelescopeBorder = { fg = M.colors.border, bg = M.colors.bg_dark },
    TelescopePromptBorder = { fg = M.colors.border, bg = M.colors.bg_dark },
    TelescopeResultsBorder = { fg = M.colors.border, bg = M.colors.bg_dark },
    TelescopePreviewBorder = { fg = M.colors.border, bg = M.colors.bg_dark },
    TelescopeSelection = { fg = M.colors.fg, bg = M.colors.selection },
    TelescopeSelectionCaret = { fg = M.colors.orange, bg = M.colors.selection },
    TelescopeMultiSelection = { fg = M.colors.purple, bg = M.colors.selection },
    TelescopeMatching = { fg = M.colors.orange, bold = true },
    TelescopePromptPrefix = { fg = M.colors.orange },
    TelescopePromptCounter = { fg = M.colors.fg_dark },
    TelescopeTitle = { fg = M.colors.orange, bold = true },
    TelescopePreviewTitle = { fg = M.colors.green, bold = true },
    TelescopeResultsTitle = { fg = M.colors.blue, bold = true },
    TelescopePromptTitle = { fg = M.colors.orange, bold = true },

    -- Plugin Support: nvim-cmp
    CmpItemAbbr = { fg = M.colors.fg },
    CmpItemAbbrDeprecated = { fg = M.colors.fg_dark, strikethrough = true },
    CmpItemAbbrMatch = { fg = M.colors.orange, bold = true },
    CmpItemAbbrMatchFuzzy = { fg = M.colors.orange, bold = true },
    CmpItemKind = { fg = M.colors.yellow },
    CmpItemKindDefault = { fg = M.colors.yellow },
    CmpItemMenu = { fg = M.colors.fg_dark },
    CmpItemKindText = { fg = M.colors.fg },
    CmpItemKindMethod = { fg = M.colors.orange },
    CmpItemKindFunction = { fg = M.colors.orange },
    CmpItemKindConstructor = { fg = M.colors.yellow },
    CmpItemKindField = { fg = M.colors.fg },
    CmpItemKindVariable = { fg = M.colors.fg },
    CmpItemKindClass = { fg = M.colors.yellow },
    CmpItemKindInterface = { fg = M.colors.yellow },
    CmpItemKindModule = { fg = M.colors.blue },
    CmpItemKindProperty = { fg = M.colors.fg },
    CmpItemKindUnit = { fg = M.colors.yellow },
    CmpItemKindValue = { fg = M.colors.yellow },
    CmpItemKindEnum = { fg = M.colors.yellow },
    CmpItemKindKeyword = { fg = M.colors.red },
    CmpItemKindSnippet = { fg = M.colors.green },
    CmpItemKindColor = { fg = M.colors.purple },
    CmpItemKindFile = { fg = M.colors.blue },
    CmpItemKindReference = { fg = M.colors.cyan },
    CmpItemKindFolder = { fg = M.colors.blue },
    CmpItemKindEnumMember = { fg = M.colors.purple },
    CmpItemKindConstant = { fg = M.colors.yellow },
    CmpItemKindStruct = { fg = M.colors.yellow },
    CmpItemKindEvent = { fg = M.colors.orange },
    CmpItemKindOperator = { fg = M.colors.fg },
    CmpItemKindTypeParameter = { fg = M.colors.yellow },

    -- Plugin Support: Which-key
    WhichKey = { fg = M.colors.orange, bold = true },
    WhichKeyGroup = { fg = M.colors.blue },
    WhichKeyDesc = { fg = M.colors.fg },
    WhichKeySeperator = { fg = M.colors.fg_dark },
    WhichKeyFloat = { bg = M.colors.bg_dark },
    WhichKeyBorder = { fg = M.colors.border, bg = M.colors.bg_dark },
    WhichKeyValue = { fg = M.colors.green },

    -- Plugin Support: Neo-tree
    NeoTreeNormal = { fg = M.colors.fg, bg = M.colors.bg_dark },
    NeoTreeNormalNC = { fg = M.colors.fg, bg = M.colors.bg_dark },
    NeoTreeDirectoryName = { fg = M.colors.fg },
    NeoTreeDirectoryIcon = { fg = M.colors.blue },
    NeoTreeRootName = { fg = M.colors.orange, bold = true },
    NeoTreeFileName = { fg = M.colors.fg },
    NeoTreeFileIcon = { fg = M.colors.fg },
    NeoTreeFileNameOpened = { fg = M.colors.orange },
    NeoTreeIndentMarker = { fg = M.colors.fg_dark },
    NeoTreeExpander = { fg = M.colors.fg_dark },
    NeoTreeDotfile = { fg = M.colors.fg_dark },
    NeoTreeGitAdded = { fg = M.colors.git_add },
    NeoTreeGitDeleted = { fg = M.colors.git_delete },
    NeoTreeGitModified = { fg = M.colors.git_change },
    NeoTreeGitConflict = { fg = M.colors.error },
    NeoTreeGitUntracked = { fg = M.colors.hint },
    NeoTreeGitIgnored = { fg = M.colors.fg_dark },
    NeoTreeGitStaged = { fg = M.colors.git_add },
    NeoTreeFloatBorder = { fg = M.colors.border, bg = M.colors.bg_dark },
    NeoTreeFloatTitle = { fg = M.colors.orange, bg = M.colors.bg_dark, bold = true },
    NeoTreeTitleBar = { fg = M.colors.fg, bg = M.colors.bg_light },

    -- Plugin Support: DAP (Debug Adapter Protocol)
    DapBreakpoint = { fg = M.colors.error },
    DapBreakpointCondition = { fg = M.colors.warn },
    DapBreakpointRejected = { fg = M.colors.fg_dark },
    DapLogPoint = { fg = M.colors.info },
    DapStopped = { fg = M.colors.ok },
    DapUIVariable = { fg = M.colors.fg },
    DapUIScope = { fg = M.colors.cyan },
    DapUIType = { fg = M.colors.purple },
    DapUIValue = { fg = M.colors.fg },
    DapUIModifiedValue = { fg = M.colors.warn, bold = true },
    DapUIDecoration = { fg = M.colors.cyan },
    DapUIThread = { fg = M.colors.green },
    DapUIStoppedThread = { fg = M.colors.cyan },
    DapUIFrameName = { fg = M.colors.fg },
    DapUISource = { fg = M.colors.purple },
    DapUILineNumber = { fg = M.colors.cyan },
    DapUIFloatBorder = { fg = M.colors.border },
    DapUIWatchesEmpty = { fg = M.colors.error },
    DapUIWatchesValue = { fg = M.colors.green },
    DapUIWatchesError = { fg = M.colors.error },
    DapUIBreakpointsPath = { fg = M.colors.cyan },
    DapUIBreakpointsInfo = { fg = M.colors.green },
    DapUIBreakpointsCurrentLine = { fg = M.colors.green, bold = true },
    DapUIBreakpointsLine = { fg = M.colors.cyan },
    DapUIBreakpointsDisabledLine = { fg = M.colors.fg_dark },
    DapUICurrentFrameName = { fg = M.colors.green, bold = true },
    DapUIStepOver = { fg = M.colors.cyan },
    DapUIStepInto = { fg = M.colors.cyan },
    DapUIStepBack = { fg = M.colors.cyan },
    DapUIStepOut = { fg = M.colors.cyan },
    DapUIStop = { fg = M.colors.error },
    DapUIPlayPause = { fg = M.colors.green },
    DapUIRestart = { fg = M.colors.green },
    DapUIUnavailable = { fg = M.colors.fg_dark },
}

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

    -- Neovim settings
    vim.cmd('hi clear')
    if vim.fn.exists('syntax_on') then
        vim.cmd('syntax reset')
    end
    vim.o.termguicolors = true
    vim.g.colors_name = 'guttenbergovitz'

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

return M
