# Changelog

All notable changes to **Guttenbergovitz Theme** are documented in this file.
This project adheres to [Semantic Versioning](https://semver.org/).

## [1.3.0] - 2026-11-23

### Changed
- **Dark mode comments**: Tuned `semantic.comment` from `#7c7c7c` (`3.75:1`) to `#5e5e62` (`2.43:1`, matching Nord-style muted legibility) across VS Code, Neovim, Vim, Helix, Zed, and JetBrains, while keeping UI dim text and line numbers at `#7c7c7c`.
- **Light mode yellow**: Darkened `yellow` from `#b8995a` (`2.45:1`) to `#9c7d3e` (`3.50:1`) for legible types, classes, constants, and numbers without sacrificing the warm, low-contrast aesthetic.
- **Docstrings**: Mapped `@string.documentation` (Neovim), `string.quoted.docstring` / `string.quoted.docstring.multi` (VS Code), and `comment.doc` (Zed) to muted italic comment styling instead of green string highlighting.
- **Cross-IDE semantic parity**:
  - Unified `operator` to `red` (`@operator` in Neovim, `Operator` in Vim).
  - Unified `macro` to `cyan` (`@function.macro` / `@constant.macro` in Neovim, `Macro` in Vim).
  - Unified `boolean` and `constant.builtin` to `purple` across `palette.json`, VS Code, Neovim, Vim, Helix, and Zed.
  - Unified `attribute` / `decorator` to `purple` across `palette.json` and Zed.
  - Unified `@variable.builtin` (`self` / `this`) to `red` in Neovim to match VS Code and Helix.
- **README**: Rewritten with a clearer Philosophy section, updated palette swatches, 18-platform ports table, and quick-install instructions.

### Added
- **Zed syntax completeness**: Added `comment.doc`, `constant.builtin`, `variable.special`, `function.method`, `string.regex`, `string.escape`, `label`, `title`, `link_text`, `link_uri`, `emphasis`, and `emphasis.strong` to `templates/zed.json.tmpl` and `zed/guttenbergovitz.json`.
- **Validation coverage**: Extended `scripts/validate_consistency.py` to cover Kitty (light), Ghostty, Warp, JetBrains, tmux, Claude Code, and Pi (15 theme families total). Extended `scripts/check_palette.py` to inspect JetBrains `.icls` hex values.
- **CI workflows**: Expanded `.github/workflows/ci.yml` and `.github/workflows/validate-themes.yml` to validate all new ports and enforce `make check.palette`.

### Fixed
- **Installer (`scripts/install_theme.py`)**: Fixed `AttributeError` crash when selecting `iTerm` or `A` (Install for all), sorted interactive menu keys numerically, and replaced `(None)` with `(manual / config merge)`.
- **VS Code templates**: Synced `templates/vscode-dark.json.tmpl` and `templates/vscode-light.json.tmpl` with `semanticHighlighting` and `semanticTokenColors` so `generate_themes.py` no longer drifts from `vscode/themes/*.json`.
- **JetBrains**: Fixed dark `FileColor` values (`#3c3c2d`, `#3c2d2d`, `#2d2d3c`) in `Guttenbergovitz-Light.theme.json` and aligned `FILESTATUS_*_IGNORED` in `.icls` files with `palette.json` (`git.ignored`).

## [1.2.0] - 2026-10-07

### Added
- Language-specific highlighting and LSP semantic tokens across VS Code, JetBrains, Neovim, Vim, and Helix (Rust, Go, Python, Ruby, PHP, Java, C#, TypeScript, Lua, Shell, YAML, JSON, TOML, CSS, Regex).
- New ports: **tmux** and **Claude Code** (dark and light variants).
- Added tmux, Claude Code, and iTerm to `scripts/install_theme.py`.

## [1.1.2] - 2026-08-18

### Added
- Python and Go language-specific TextMate scopes in VS Code, Tree-sitter overrides in Neovim, and `GO_*` / `go.*` tokens in JetBrains.

### Fixed
- Aligned Python decorator color in Vim with other ports.

## [1.1.1] - 2026-07-30

### Fixed
- Python function calls in JetBrains (`PY.FUNCTION_CALL`, `PY.METHOD_CALL`, `PY.FUNC_DEFINITION`).
- Tree selection contrast in JetBrains Light theme and softer git-ignored file status colors.

## [1.1.0] - 2026-07-23

### Added
- JetBrains Islands UI support (2025.3+).
- New ports: **Pi**, **OpenCode**, and **Herdr**, plus updated Zellij KDL format.

## [1.0.0] - 2025-04-16

### Added
- Initial release with Dark and Light variants for VS Code, Neovim, Vim, Helix, Zed, JetBrains, Kitty, Ghostty, Warp, iTerm, and Zellij.
