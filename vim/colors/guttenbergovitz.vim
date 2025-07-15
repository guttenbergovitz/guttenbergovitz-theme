" Guttenbergovitz Color Scheme for Vim 8+
" Maintainer: Guttenbergovitz Theme
" License: MIT
" Version: 1.0.0

" Check for Vim version compatibility
if v:version < 800
    echohl ErrorMsg
    echomsg "guttenbergovitz.vim: This colorscheme requires Vim 8 or higher"
    echohl None
    finish
endif

" Check for termguicolors support
if !has('termguicolors') && !has('gui_running')
    echohl ErrorMsg
    echomsg "guttenbergovitz.vim: This colorscheme requires termguicolors or GUI support"
    echohl None
    finish
endif

" Reset colors
highlight clear
if exists('syntax_on')
    syntax reset
endif

" Set colorscheme name
let g:colors_name = 'guttenbergovitz'

" Enable true color support
if has('termguicolors')
    set termguicolors
endif

" Color palette
let s:colors = {
    \ 'bg': '#232326',
    \ 'bg_dark': '#1d1d20',
    \ 'bg_light': '#2a2a2d',
    \ 'fg': '#d4be98',
    \ 'fg_dark': '#7c7c7c',
    \ 'fg_light': '#e0d2a6',
    \ 'red': '#a96b69',
    \ 'green': '#89a87d',
    \ 'yellow': '#d6b986',
    \ 'blue': '#7a9ec2',
    \ 'orange': '#d79969',
    \ 'purple': '#b194a3',
    \ 'cyan': '#89b4ac',
    \ 'selection': '#3a3a3d',
    \ 'comment': '#7c7c7c',
    \ 'cursor': '#d4be98',
    \ 'border': '#3a3a3d',
    \ 'error': '#cc6666',
    \ 'warn': '#de935f',
    \ 'info': '#81a2be',
    \ 'hint': '#8abeb7',
    \ 'ok': '#b5bd68',
    \ 'diff_add': '#2d3c2d',
    \ 'diff_delete': '#3c2d2d',
    \ 'diff_change': '#3c3c2d',
    \ 'diff_text': '#4c4c2d',
    \ 'git_add': '#89a87d',
    \ 'git_change': '#d6b986',
    \ 'git_delete': '#a96b69',
    \ 'none': 'NONE'
\ }

" Helper function to set highlight groups
function! s:hi(group, fg, bg, attr, sp)
    let l:cmd = 'highlight ' . a:group
    if a:fg != ''
        let l:cmd .= ' guifg=' . a:fg
    endif
    if a:bg != ''
        let l:cmd .= ' guibg=' . a:bg
    endif
    if a:attr != ''
        let l:cmd .= ' gui=' . a:attr
    endif
    if a:sp != ''
        let l:cmd .= ' guisp=' . a:sp
    endif
    execute l:cmd
endfunction

" Core highlight groups
call s:hi('Normal', s:colors.fg, s:colors.bg, '', '')
call s:hi('NormalFloat', s:colors.fg, s:colors.bg_dark, '', '')
call s:hi('LineNr', s:colors.fg_dark, '', '', '')
call s:hi('CursorLine', '', s:colors.selection, '', '')
call s:hi('CursorLineNr', s:colors.fg, '', '', '')
call s:hi('Visual', '', s:colors.selection, '', '')
call s:hi('IncSearch', s:colors.bg, s:colors.orange, '', '')
call s:hi('Search', s:colors.bg, s:colors.yellow, '', '')

" Syntax highlighting
call s:hi('Comment', s:colors.comment, '', 'italic', '')
call s:hi('Constant', s:colors.yellow, '', '', '')
call s:hi('String', s:colors.green, '', '', '')
call s:hi('Character', s:colors.green, '', '', '')
call s:hi('Number', s:colors.yellow, '', '', '')
call s:hi('Boolean', s:colors.purple, '', '', '')
call s:hi('Float', s:colors.yellow, '', '', '')
call s:hi('Identifier', s:colors.fg, '', '', '')
call s:hi('Function', s:colors.orange, '', '', '')
call s:hi('Statement', s:colors.red, '', '', '')
call s:hi('Conditional', s:colors.red, '', '', '')
call s:hi('Repeat', s:colors.red, '', '', '')
call s:hi('Label', s:colors.red, '', '', '')
call s:hi('Operator', s:colors.fg, '', '', '')
call s:hi('Keyword', s:colors.red, '', '', '')
call s:hi('Exception', s:colors.red, '', '', '')
call s:hi('PreProc', s:colors.purple, '', '', '')
call s:hi('Include', s:colors.red, '', '', '')
call s:hi('Define', s:colors.purple, '', '', '')
call s:hi('Macro', s:colors.purple, '', '', '')
call s:hi('PreCondit', s:colors.purple, '', '', '')
call s:hi('Type', s:colors.yellow, '', '', '')
call s:hi('StorageClass', s:colors.red, '', '', '')
call s:hi('Structure', s:colors.yellow, '', '', '')
call s:hi('Typedef', s:colors.yellow, '', '', '')
call s:hi('Special', s:colors.orange, '', '', '')
call s:hi('SpecialChar', s:colors.orange, '', '', '')
call s:hi('Tag', s:colors.red, '', '', '')
call s:hi('Delimiter', s:colors.fg_dark, '', '', '')
call s:hi('SpecialComment', s:colors.comment, '', 'italic', '')
call s:hi('Debug', s:colors.red, '', '', '')

" Interface elements
call s:hi('StatusLine', s:colors.fg, s:colors.bg_dark, '', '')
call s:hi('StatusLineNC', s:colors.fg_dark, s:colors.bg_dark, '', '')
call s:hi('VertSplit', s:colors.selection, '', '', '')
call s:hi('TabLine', s:colors.fg_dark, s:colors.bg_dark, '', '')
call s:hi('TabLineFill', '', s:colors.bg_dark, '', '')
call s:hi('TabLineSel', s:colors.fg, s:colors.bg, '', '')

" Folding
call s:hi('Folded', s:colors.fg_dark, s:colors.bg_light, '', '')
call s:hi('FoldColumn', s:colors.fg_dark, s:colors.bg, '', '')

" Cursor
call s:hi('Cursor', s:colors.bg, s:colors.cursor, '', '')
call s:hi('CursorIM', s:colors.bg, s:colors.cursor, '', '')

" Popup menus
call s:hi('Pmenu', s:colors.fg, s:colors.bg_dark, '', '')
call s:hi('PmenuSel', s:colors.fg, s:colors.selection, '', '')
call s:hi('PmenuSbar', '', s:colors.bg_light, '', '')
call s:hi('PmenuThumb', '', s:colors.fg_dark, '', '')

" Diff
call s:hi('DiffAdd', s:colors.git_add, s:colors.diff_add, '', '')
call s:hi('DiffChange', s:colors.git_change, s:colors.diff_change, '', '')
call s:hi('DiffDelete', s:colors.git_delete, s:colors.diff_delete, '', '')
call s:hi('DiffText', s:colors.git_change, s:colors.diff_text, '', '')

" Spell checking
call s:hi('SpellBad', '', '', 'undercurl', s:colors.error)
call s:hi('SpellCap', '', '', 'undercurl', s:colors.warn)
call s:hi('SpellLocal', '', '', 'undercurl', s:colors.info)
call s:hi('SpellRare', '', '', 'undercurl', s:colors.hint)

" Error messages
call s:hi('ErrorMsg', s:colors.error, '', '', '')
call s:hi('WarningMsg', s:colors.warn, '', '', '')
call s:hi('ModeMsg', s:colors.fg, '', '', '')
call s:hi('MoreMsg', s:colors.green, '', '', '')
call s:hi('Question', s:colors.green, '', '', '')

" Matching
call s:hi('MatchParen', s:colors.orange, '', 'bold', '')

" Whitespace
call s:hi('Whitespace', s:colors.bg_light, '', '', '')
call s:hi('NonText', s:colors.bg_light, '', '', '')
call s:hi('SpecialKey', s:colors.bg_light, '', '', '')

" Concealed
call s:hi('Conceal', s:colors.fg_dark, '', '', '')

" Color column
call s:hi('ColorColumn', '', s:colors.bg_light, '', '')

" Sign column
call s:hi('SignColumn', s:colors.fg_dark, s:colors.bg, '', '')

" Directory
call s:hi('Directory', s:colors.blue, '', '', '')

" Title
call s:hi('Title', s:colors.orange, '', 'bold', '')

" Substitute
call s:hi('Substitute', s:colors.bg, s:colors.orange, '', '')

" Wild menu
call s:hi('WildMenu', s:colors.fg, s:colors.selection, '', '')

" QuickFix
call s:hi('QuickFixLine', '', s:colors.selection, '', '')

" Messages
call s:hi('MsgArea', s:colors.fg, s:colors.bg, '', '')
call s:hi('MsgSeparator', s:colors.border, s:colors.bg, '', '')

" Floating windows
call s:hi('FloatBorder', s:colors.border, s:colors.bg_dark, '', '')
call s:hi('FloatTitle', s:colors.orange, s:colors.bg_dark, 'bold', '')

" Plugin Support: vim-airline
call s:hi('airline_a', s:colors.bg, s:colors.orange, 'bold', '')
call s:hi('airline_b', s:colors.fg, s:colors.bg_dark, '', '')
call s:hi('airline_c', s:colors.fg_dark, s:colors.bg, '', '')
call s:hi('airline_x', s:colors.fg_dark, s:colors.bg, '', '')
call s:hi('airline_y', s:colors.fg, s:colors.bg_dark, '', '')
call s:hi('airline_z', s:colors.bg, s:colors.green, 'bold', '')
call s:hi('airline_error', s:colors.red, '', '', '')
call s:hi('airline_warning', s:colors.yellow, '', '', '')

" Plugin Support: vim-gitgutter
call s:hi('GitGutterAdd', s:colors.green, '', '', '')
call s:hi('GitGutterChange', s:colors.yellow, '', '', '')
call s:hi('GitGutterDelete', s:colors.red, '', '', '')
call s:hi('GitGutterChangeDelete', s:colors.red, '', '', '')

" Plugin Support: vim-signify
call s:hi('SignifySignAdd', s:colors.green, '', '', '')
call s:hi('SignifySignChange', s:colors.yellow, '', '', '')
call s:hi('SignifySignDelete', s:colors.red, '', '', '')
call s:hi('SignifySignChangeDelete', s:colors.red, '', '', '')

" Plugin Support: NERDTree
call s:hi('NERDTreeDir', s:colors.fg, '', '', '')
call s:hi('NERDTreeDirSlash', s:colors.fg_dark, '', '', '')
call s:hi('NERDTreeOpenable', s:colors.yellow, '', '', '')
call s:hi('NERDTreeClosable', s:colors.yellow, '', '', '')
call s:hi('NERDTreeFile', s:colors.fg, '', '', '')
call s:hi('NERDTreeExecFile', s:colors.green, '', '', '')
call s:hi('NERDTreeUp', s:colors.fg_dark, '', '', '')
call s:hi('NERDTreeCWD', s:colors.orange, '', 'bold', '')
call s:hi('NERDTreeHelp', s:colors.fg_dark, '', '', '')
call s:hi('NERDTreeToggleOn', s:colors.green, '', '', '')
call s:hi('NERDTreeToggleOff', s:colors.red, '', '', '')

" Plugin Support: fzf
call s:hi('fzf1', s:colors.fg, s:colors.bg_dark, '', '')
call s:hi('fzf2', s:colors.fg, s:colors.bg_dark, '', '')
call s:hi('fzf3', s:colors.fg, s:colors.bg_dark, '', '')

" Plugin Support: CtrlP
call s:hi('CtrlPMatch', s:colors.orange, '', 'bold', '')
call s:hi('CtrlPLinePre', s:colors.fg_dark, '', '', '')
call s:hi('CtrlPPrtBase', s:colors.fg_dark, '', '', '')
call s:hi('CtrlPPrtText', s:colors.fg, '', '', '')
call s:hi('CtrlPPrtCursor', s:colors.fg, '', 'reverse', '')

" Plugin Support: vim-indent-guides
call s:hi('IndentGuidesOdd', '', s:colors.bg_light, '', '')
call s:hi('IndentGuidesEven', '', s:colors.bg_dark, '', '')

" Plugin Support: vim-startify
call s:hi('StartifyBracket', s:colors.fg_dark, '', '', '')
call s:hi('StartifyFile', s:colors.fg, '', '', '')
call s:hi('StartifyFooter', s:colors.fg_dark, '', '', '')
call s:hi('StartifyHeader', s:colors.orange, '', 'bold', '')
call s:hi('StartifyNumber', s:colors.yellow, '', '', '')
call s:hi('StartifyPath', s:colors.blue, '', '', '')
call s:hi('StartifySection', s:colors.green, '', 'bold', '')
call s:hi('StartifySelect', s:colors.fg, '', '', '')
call s:hi('StartifySlash', s:colors.fg_dark, '', '', '')
call s:hi('StartifySpecial', s:colors.orange, '', '', '')

" Plugin Support: vim-fugitive
call s:hi('fugitiveBlame', s:colors.fg_dark, '', '', '')
call s:hi('fugitiveHash', s:colors.purple, '', '', '')

" Plugin Support: vim-which-key
call s:hi('WhichKey', s:colors.orange, '', 'bold', '')
call s:hi('WhichKeyGroup', s:colors.blue, '', '', '')
call s:hi('WhichKeyDesc', s:colors.fg, '', '', '')
call s:hi('WhichKeySeperator', s:colors.fg_dark, '', '', '')
call s:hi('WhichKeyFloat', '', s:colors.bg_dark, '', '')
call s:hi('WhichKeyBorder', s:colors.border, s:colors.bg_dark, '', '')
call s:hi('WhichKeyValue', s:colors.green, '', '', '')

" Language-specific highlights
" HTML
call s:hi('htmlTag', s:colors.red, '', '', '')
call s:hi('htmlEndTag', s:colors.red, '', '', '')
call s:hi('htmlTagName', s:colors.red, '', '', '')
call s:hi('htmlArg', s:colors.yellow, '', '', '')
call s:hi('htmlSpecialChar', s:colors.orange, '', '', '')

" CSS
call s:hi('cssBraces', s:colors.fg, '', '', '')
call s:hi('cssClassName', s:colors.yellow, '', '', '')
call s:hi('cssClassNameDot', s:colors.yellow, '', '', '')
call s:hi('cssDefinition', s:colors.fg, '', '', '')
call s:hi('cssMediaType', s:colors.purple, '', '', '')
call s:hi('cssProp', s:colors.blue, '', '', '')
call s:hi('cssPseudoClassId', s:colors.orange, '', '', '')
call s:hi('cssTagName', s:colors.red, '', '', '')

" JavaScript
call s:hi('javaScriptBraces', s:colors.fg, '', '', '')
call s:hi('javaScriptFunction', s:colors.red, '', '', '')
call s:hi('javaScriptIdentifier', s:colors.red, '', '', '')
call s:hi('javaScriptMember', s:colors.fg, '', '', '')
call s:hi('javaScriptNumber', s:colors.yellow, '', '', '')
call s:hi('javaScriptNull', s:colors.purple, '', '', '')
call s:hi('javaScriptParens', s:colors.fg, '', '', '')

" Python
call s:hi('pythonBuiltin', s:colors.orange, '', '', '')
call s:hi('pythonBuiltinObj', s:colors.orange, '', '', '')
call s:hi('pythonBuiltinFunc', s:colors.orange, '', '', '')
call s:hi('pythonFunction', s:colors.orange, '', '', '')
call s:hi('pythonDecorator', s:colors.purple, '', '', '')
call s:hi('pythonInclude', s:colors.red, '', '', '')
call s:hi('pythonImport', s:colors.red, '', '', '')
call s:hi('pythonRun', s:colors.red, '', '', '')
call s:hi('pythonCoding', s:colors.comment, '', 'italic', '')
call s:hi('pythonOperator', s:colors.red, '', '', '')
call s:hi('pythonException', s:colors.red, '', '', '')
call s:hi('pythonExceptions', s:colors.orange, '', '', '')
call s:hi('pythonBoolean', s:colors.purple, '', '', '')
call s:hi('pythonDot', s:colors.fg, '', '', '')
call s:hi('pythonConditional', s:colors.red, '', '', '')
call s:hi('pythonRepeat', s:colors.red, '', '', '')
call s:hi('pythonDoctestValue', s:colors.green, '', '', '')

" Ruby
call s:hi('rubyAttribute', s:colors.orange, '', '', '')
call s:hi('rubyConstant', s:colors.yellow, '', '', '')
call s:hi('rubyInterpolation', s:colors.orange, '', '', '')
call s:hi('rubyInterpolationDelimiter', s:colors.orange, '', '', '')
call s:hi('rubyRegexp', s:colors.cyan, '', '', '')
call s:hi('rubySymbol', s:colors.purple, '', '', '')
call s:hi('rubyStringDelimiter', s:colors.green, '', '', '')

" PHP
call s:hi('phpVarSelector', s:colors.fg, '', '', '')
call s:hi('phpKeyword', s:colors.red, '', '', '')
call s:hi('phpRepeat', s:colors.red, '', '', '')
call s:hi('phpConditional', s:colors.red, '', '', '')
call s:hi('phpStatement', s:colors.red, '', '', '')
call s:hi('phpMemberSelector', s:colors.fg, '', '', '')

" Markdown
call s:hi('markdownCode', s:colors.green, '', '', '')
call s:hi('markdownError', s:colors.fg, s:colors.bg, '', '')
call s:hi('markdownCodeBlock', s:colors.green, '', '', '')
call s:hi('markdownHeadingDelimiter', s:colors.orange, '', 'bold', '')
call s:hi('markdownH1', s:colors.orange, '', 'bold', '')
call s:hi('markdownH2', s:colors.orange, '', 'bold', '')
call s:hi('markdownH3', s:colors.orange, '', 'bold', '')
call s:hi('markdownH4', s:colors.orange, '', 'bold', '')
call s:hi('markdownH5', s:colors.orange, '', 'bold', '')
call s:hi('markdownH6', s:colors.orange, '', 'bold', '')
call s:hi('markdownListMarker', s:colors.red, '', '', '')
call s:hi('markdownOrderedListMarker', s:colors.red, '', '', '')
call s:hi('markdownRule', s:colors.fg_dark, '', '', '')
call s:hi('markdownBold', s:colors.fg, '', 'bold', '')
call s:hi('markdownItalic', s:colors.fg, '', 'italic', '')
call s:hi('markdownBoldItalic', s:colors.fg, '', 'bold,italic', '')
call s:hi('markdownUrl', s:colors.cyan, '', 'underline', '')
call s:hi('markdownLinkText', s:colors.blue, '', '', '')
call s:hi('markdownLinkDelimiter', s:colors.fg_dark, '', '', '')
call s:hi('markdownLinkTextDelimiter', s:colors.fg_dark, '', '', '')
call s:hi('markdownCodeDelimiter', s:colors.orange, '', '', '')
call s:hi('markdownBlockquote', s:colors.fg_dark, '', 'italic', '')

" Git
call s:hi('gitcommitComment', s:colors.comment, '', 'italic', '')
call s:hi('gitcommitUnmerged', s:colors.red, '', '', '')
call s:hi('gitcommitOnBranch', s:colors.fg, '', '', '')
call s:hi('gitcommitBranch', s:colors.purple, '', '', '')
call s:hi('gitcommitDiscardedType', s:colors.red, '', '', '')
call s:hi('gitcommitSelectedType', s:colors.green, '', '', '')
call s:hi('gitcommitHeader', s:colors.fg, '', '', '')
call s:hi('gitcommitUntrackedFile', s:colors.red, '', '', '')
call s:hi('gitcommitDiscardedFile', s:colors.red, '', '', '')
call s:hi('gitcommitSelectedFile', s:colors.green, '', '', '')
call s:hi('gitcommitUnmergedFile', s:colors.yellow, '', '', '')
call s:hi('gitcommitFile', s:colors.fg, '', '', '')
call s:hi('gitcommitSummary', s:colors.fg, '', '', '')
call s:hi('gitcommitOverflow', s:colors.error, '', '', '')

" Vim
call s:hi('vimCommentTitle', s:colors.comment, '', 'bold,italic', '')
call s:hi('vimNotation', s:colors.orange, '', '', '')
call s:hi('vimBracket', s:colors.orange, '', '', '')
call s:hi('vimMapModKey', s:colors.orange, '', '', '')
call s:hi('vimCommand', s:colors.red, '', '', '')
call s:hi('vimLet', s:colors.red, '', '', '')
call s:hi('vimNorm', s:colors.red, '', '', '')
call s:hi('vimFuncSID', s:colors.fg, '', '', '')
call s:hi('vimFunction', s:colors.orange, '', '', '')
call s:hi('vimGroup', s:colors.blue, '', '', '')
call s:hi('vimHiGroup', s:colors.blue, '', '', '')
call s:hi('vimSetSep', s:colors.fg_dark, '', '', '')
call s:hi('vimSep', s:colors.fg_dark, '', '', '')
call s:hi('vimContinue', s:colors.fg_dark, '', '', '')

" Terminal colors (if supported)
if exists('*term_setansicolors')
    let g:terminal_ansi_colors = [
        \ s:colors.bg_dark,
        \ s:colors.red,
        \ s:colors.green,
        \ s:colors.yellow,
        \ s:colors.blue,
        \ s:colors.purple,
        \ s:colors.cyan,
        \ s:colors.fg,
        \ s:colors.fg_dark,
        \ s:colors.error,
        \ s:colors.ok,
        \ s:colors.warn,
        \ s:colors.info,
        \ s:colors.purple,
        \ s:colors.hint,
        \ s:colors.fg_light
    \ ]
endif

" Cleanup
unlet s:colors