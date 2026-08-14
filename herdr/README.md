# Guttenbergovitz for Herdr

> "It's not the notes you play, it's the notes you don't play." - Miles Davis

A warm, vintage-inspired theme for [Herdr](https://herdr.dev/), the terminal multiplexer for AI coding agents, matching the Guttenbergovitz color scheme.

## About

Guttenbergovitz was conceived during a deep dive into jazz history, evolving from a discussion about the parallels between music evolution and code aesthetics. Just as Miles Davis stripped jazz to its essence in "Kind of Blue", this theme aims to reduce visual noise while maintaining depth and character.

## Philosophy

Drawing inspiration from both old European printing traditions and modern color science, Guttenbergovitz combines the warmth of vintage manuscripts with contemporary minimalist design principles. It's like a well-aged whiskey - complex but not overwhelming.

## Design Principles

- Less blue light, more warmth
- Minimal but meaningful syntax highlighting
- Focus on readability and reduced eye strain
- Inspired by vintage book printing
- Professional without being corporate
- Like Count Basie's orchestra: elegant, precise, and purposeful

## Installation

Herdr has no external theme files. Colors are configured inline in `~/.config/herdr/config.toml` via the `[theme.custom]` section.

### Using the CLI installer

```bash
make install
```

Choose **Herdr** from the list (you'll be asked for the dark or light variant), or pass it directly:

```bash
python3 scripts/install_theme.py herdr          # dark (default)
python3 scripts/install_theme.py herdr light    # light
python3 scripts/install_theme.py herdr dark     # back to dark
```

The installer merges the `[theme.custom]` block into your existing `config.toml`, replacing any previous custom colors while leaving the rest of the config untouched, and reloads the running Herdr server so the theme applies immediately.

### Manual Installation

Append the contents of `herdr/guttenbergovitz.toml` (dark) or `herdr/guttenbergovitz-light.toml` (light) to `~/.config/herdr/config.toml`. If you already have a `[theme.custom]` table, replace its contents instead.

## Activation

The theme applies after reloading the config:

```bash
herdr server reload-config
```

## Dark and light variants

Both `herdr/guttenbergovitz.toml` (dark) and `herdr/guttenbergovitz-light.toml` (light) are shipped. Herdr 0.8.0 keeps exactly one active `[theme.custom]` table, and its `auto_switch` (`dark_name`/`light_name`) only selects built-in themes — so the two variants cannot auto-follow your terminal's light/dark appearance. Switch between them with:

```bash
python3 scripts/install_theme.py herdr light
python3 scripts/install_theme.py herdr dark
```

## Color Tokens

The theme overrides every Herdr color token (`accent`, `panel_bg`, `surface0/1/dim`, `overlay0/1`, `text`, `subtext0`, `mauve`, `green`, `yellow`, `red`, `blue`, `teal`, `peach`) using the Guttenbergovitz palette.

## Contributing

Feel free to open an issue or submit a pull request on our [GitHub repository](https://github.com/guttenbergovitz/guttenbergovitz-theme).

## License

This theme is released under the MIT License. See the [LICENSE](../LICENSE) file for more details.

## Design Notes

- `theme.custom` tokens follow Herdr's catppuccin-style naming; `red` maps to the palette's error color (`#cc6666`) for UI visibility.
- Keep theme parity with other ports when adjusting colors.
