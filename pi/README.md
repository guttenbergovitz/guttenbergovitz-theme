# Pi (LLM TUI) Theme

Guttenbergovitz themes for [Pi](https://pi.dev) — the LLM-powered coding agent TUI.

## Installation

### Via the installer script

Run the interactive installer and select **Pi**:

```bash
make install
```

Or install directly:

```bash
python3 scripts/install_theme.py pi
```

### Manual installation

```bash
mkdir -p ~/.pi/agent/themes
cp pi/guttenbergovitz.json ~/.pi/agent/themes/
cp pi/guttenbergovitz-light.json ~/.pi/agent/themes/
```

### Activation

1. Open Pi
2. Run `/settings`
3. Select `guttenbergovitz` (dark) or `guttenbergovitz-light` as your theme

Or set it in `~/.pi/agent/settings.json`:

```json
{
  "theme": "guttenbergovitz"
}
```

## Preview

### Guttenbergovitz (dark)
Warm, vintage-inspired dark theme with reduced blue light. Background `#232326`, foreground `#d4be98`.

### Guttenbergovitz Light
Daylight variant with the same warm character. Background `#f5f3f0`, foreground `#5a4a3a`.
