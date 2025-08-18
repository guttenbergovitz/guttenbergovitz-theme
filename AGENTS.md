# Repository Guidelines

This repository hosts the Guttenbergovitz theme across multiple editors and terminals. Keep changes minimal, consistent across platforms, and documented in the corresponding platform folder.

## Project Structure & Module Organization

- `vscode/`: VS Code theme (`package.json`, `themes/*.json`, `.vsix`, assets).
- `nvim/`, `vim/`: Neovim/Vim themes and docs; shared color references under `colors/`.
- `kitty/`, `iterm/`, `zellij/`, `warp/`, `ghostty/`: Terminal themes.
- `helix/`, `zed/`, `jetbrains/`: Editor themes and installation notes.
- `README.md`: Philosophy and palette; each platform has its own `README.md`.

## Build, Test, and Development Commands

- VS Code package: `cd vscode && npm install && npm run package`
  - Produces `guttenbergovitz-<version>.vsix` via `@vscode/vsce`.
- Install VS Code build locally: `code --install-extension vscode/guttenbergovitz-0.0.3.vsix`
- Other platforms: no build step; copy/import files per platform `README.md` (e.g., Kitty: `~/.config/kitty/themes/guttenbergovitz.conf` and `include` it).

## Coding Style & Naming Conventions

- File naming: use `guttenbergovitz.*`; light variant uses `guttenbergovitz-light.*`.
- Indentation: JSON/TOML/YAML = 2 spaces; Lua = 2 spaces; no tabs.
- Colors: hex lowercase (e.g., `#d4be98`); keep palette aligned with root `README.md`.
- JSON: valid JSON only (no comments), stable key ordering in theme files.
- Keep changes platform-scoped and update only affected directories plus shared docs if palette changes.

## Testing Guidelines

- No automated tests; verify manually across editors:
  - VS Code: switch via “Preferences: Color Theme → Guttenbergovitz”.
  - Neovim/Vim: follow `nvim/` or `vim/` README; quick check `:colorscheme guttenbergovitz`.
  - Terminals: import/symlink config and confirm ANSI colors match the palette.
- Validate both dark and light variants: comments legibility, diagnostics, selection, inlay hints.

## Commit & Pull Request Guidelines

- Commit style: Conventional Commits (`feat:`, `fix:`, `docs:` …) as in git history.
- PRs should include: concise description, linked issue, screenshots/gifs of affected UIs, and notes on cross-platform parity.
- If VS Code theme changes, bump `version` in `vscode/package.json` and regenerate the `.vsix`.
- Update platform `README.md` if installation or screenshots change.

