# Guttenbergovitz for Kimi Code

## Install

Copy themes to the Kimi Code themes directory:

```bash
mkdir -p ~/.kimi-code/themes
cp guttenbergovitz.json ~/.kimi-code/themes/
cp guttenbergovitz-light.json ~/.kimi-code/themes/
```

Or use the repo installer:

```bash
python3 scripts/install_theme.py "kimi code"
```

Then in Kimi Code:

```
/theme
```

Select `Custom: guttenbergovitz` or `Custom: guttenbergovitz-light`.

## Alternative: tui.toml

Set the theme in `~/.kimi-code/tui.toml`:

```toml
theme = "guttenbergovitz"
```

## Notes

- Both themes override all built-in color tokens (`primary`, `accent`, text, borders, diffs, `roleUser`, `shellMode`) with colors from [`palette.json`](../palette.json).
- Editing the active theme file requires `/reload-tui` (or switching themes back and forth) to apply changes.
