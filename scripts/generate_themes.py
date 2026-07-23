#!/usr/bin/env python3
"""
Unified theme generator from palette.json.
Generates terminal themes (Kitty, Ghostty, Warp, Zellij, iTerm) and renders
editor templates (VS Code, Cursor, Kiro, Zed) for both dark and light variants.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTE_FILE = ROOT / "palette.json"
TEMPLATES_DIR = ROOT / "templates"

# plist templates for iTerm colors generation
ITERM_HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
"""

ITERM_FOOTER = """
</dict>
</plist>
"""

def hex_to_rgb_f(c: str):
    """Convert hex string (e.g. #ff0000) to float RGB tuple."""
    c = c.lstrip('#')
    r = int(c[0:2], 16) / 255.0
    g = int(c[2:4], 16) / 255.0
    b = int(c[4:6], 16) / 255.0
    return r, g, b

def iterm_color_block(key: str, hex_color: str) -> str:
    """Generate a single color entry for iTerm plist format."""
    r, g, b = hex_to_rgb_f(hex_color)
    return f"""\t<key>{key}</key>
\t<dict>
\t\t<key>Alpha Component</key>
\t\t<real>1</real>
\t\t<key>Blue Component</key>
\t\t<real>{b:.9f}</real>
\t\t<key>Color Space</key>
\t\t<string>srgb</string>
\t\t<key>Green Component</key>
\t\t<real>{g:.9f}</real>
\t\t<key>Red Component</key>
\t\t<real>{r:.9f}</real>
\t</dict>
"""

def generate_kitty(palette: dict, variant: str) -> str:
    """Generate theme contents for Kitty terminal configuration."""
    base = palette[variant]['base']
    ansi = palette[variant]['terminal']['ansi']
    ansi_bright = palette[variant]['terminal']['ansi_bright']
    ui = palette[variant]['ui']
    accents = palette[variant]['accents']
    
    inactive_tab_bg = ansi['black'] if variant == 'dark' else base['bg_dark']
    inactive_tab_fg = base['fg'] if variant == 'light' else base['fg_dim']
    active_tab_bg = base['fg']
    active_tab_fg = base['bg']
    
    return f"""# Guttenbergovitz theme for Kitty terminal ({variant} variant)
# Inspired by vintage printing and jazz aesthetics

# Base colors
foreground {base['fg']}
background {base['bg']}
selection_foreground {base['bg']}
selection_background {ui['selection']}
cursor {ui['cursor']}
cursor_text_color {base['bg']}

# Black
color0 {ansi['black']}
color8 {ansi_bright['black']}

# Red
color1 {ansi['red']}
color9 {ansi_bright['red']}

# Green
color2  {ansi['green']}
color10 {ansi_bright['green']}

# Yellow
color3  {ansi['yellow']}
color11 {ansi_bright['yellow']}

# Blue
color4  {ansi['blue']}
color12 {ansi_bright['blue']}

# Magenta
color5  {ansi['magenta']}
color13 {ansi_bright['magenta']}

# Cyan
color6  {ansi['cyan']}
color14 {ansi_bright['cyan']}

# White
color7  {ansi['white']}
color15 {ansi_bright['white']}

# URL underline color when hovering with mouse
url_color {accents['green']}

# Border colors
active_border_color {ui['cursor']}
inactive_border_color {ui['border']}

# Tab bar colors
active_tab_foreground {active_tab_fg}
active_tab_background {active_tab_bg}
inactive_tab_foreground {inactive_tab_fg}
inactive_tab_background {inactive_tab_bg}
"""

def generate_ghostty(palette: dict, variant: str) -> str:
    """Generate configuration content for Ghostty terminal."""
    base = palette[variant]['base']
    ansi = palette[variant]['terminal']['ansi']
    ansi_bright = palette[variant]['terminal']['ansi_bright']
    ui = palette[variant]['ui']
    
    return f"""# Guttenbergovitz theme for Ghostty terminal ({variant} variant)
background = {base['bg']}
foreground = {base['fg']}
cursor-color = {ui['cursor']}
selection-background = {ui['selection']}
selection-foreground = {base['bg']}

palette = 0={ansi['black']}
palette = 1={ansi['red']}
palette = 2={ansi['green']}
palette = 3={ansi['yellow']}
palette = 4={ansi['blue']}
palette = 5={ansi['magenta']}
palette = 6={ansi['cyan']}
palette = 7={ansi['white']}
palette = 8={ansi_bright['black']}
palette = 9={ansi_bright['red']}
palette = 10={ansi_bright['green']}
palette = 11={ansi_bright['yellow']}
palette = 12={ansi_bright['blue']}
palette = 13={ansi_bright['magenta']}
palette = 14={ansi_bright['cyan']}
palette = 15={ansi_bright['white']}
"""

def generate_warp(palette: dict, variant: str) -> str:
    """Generate configuration content for Warp terminal."""
    base = palette[variant]['base']
    ansi = palette[variant]['terminal']['ansi']
    ansi_bright = palette[variant]['terminal']['ansi_bright']
    accents = palette[variant]['accents']
    
    details = "darker" if variant == "dark" else "lighter"
    
    return f"""name: "Guttenbergovitz{' Light' if variant == 'light' else ''}"
accent: "{accents['orange']}"
background: "{base['bg']}"
cursor: "{base['fg']}"
details: {details}
foreground: "{base['fg']}"
terminal_colors:
  bright:
    black: "{ansi_bright['black']}"
    blue: "{ansi_bright['blue']}"
    cyan: "{ansi_bright['cyan']}"
    green: "{ansi_bright['green']}"
    magenta: "{ansi_bright['magenta']}"
    red: "{ansi_bright['red']}"
    white: "{ansi_bright['white']}"
    yellow: "{ansi_bright['yellow']}"
  normal:
    black: "{ansi['black']}"
    blue: "{ansi['blue']}"
    cyan: "{ansi['cyan']}"
    green: "{ansi['green']}"
    magenta: "{ansi['magenta']}"
    red: "{ansi['red']}"
    white: "{ansi['white']}"
    yellow: "{ansi['yellow']}"
"""

def generate_zellij(palette: dict, variant: str) -> str:
    """Generate KDL configuration content for Zellij multiplexer."""
    base = palette[variant]['base']
    ansi = palette[variant]['terminal']['ansi']
    ansi_bright = palette[variant]['terminal']['ansi_bright']
    accents = palette[variant]['accents']
    ui = palette[variant]['ui']
    
    theme_name = "guttenbergovitz-light" if variant == "light" else "guttenbergovitz"
    
    return f"""themes {{
    {theme_name} {{
        fg "{base['fg']}"
        bg "{ui['border']}"
        black "{ansi['black']}"
        red "{ansi['red']}"
        green "{ansi['green']}"
        yellow "{ansi['yellow']}"
        blue "{ansi['blue']}"
        magenta "{ansi['magenta']}"
        cyan "{ansi['cyan']}"
        white "{ansi['white']}"
        orange "{accents['orange']}"

        // Bright variants
        black_bright "{ansi_bright['black']}"
        red_bright "{ansi_bright['red']}"
        green_bright "{ansi_bright['green']}"
        yellow_bright "{ansi_bright['yellow']}"
        blue_bright "{ansi_bright['blue']}"
        magenta_bright "{ansi_bright['magenta']}"
        cyan_bright "{ansi_bright['cyan']}"
        white_bright "{ansi_bright['white']}"
        orange_bright "{accents['orange']}"
    }}
}}
"""

def generate_iterm(palette: dict, variant: str) -> str:
    """Generate PLIST content for iTerm colors."""
    base = palette[variant]['base']
    ansi = palette[variant]['terminal']['ansi']
    ansi_bright = palette[variant]['terminal']['ansi_bright']
    ui = palette[variant]['ui']
    
    out = [ITERM_HEADER]
    
    out.append(iterm_color_block('Background Color', base['bg']))
    out.append(iterm_color_block('Foreground Color', base['fg']))
    out.append(iterm_color_block('Cursor Color', ui['cursor']))
    out.append(iterm_color_block('Selection Color', ui['selection']))
    out.append(iterm_color_block('Selected Text Color', base['bg']))
    
    order = [
        ('Ansi 0 Color', ansi['black']),
        ('Ansi 1 Color', ansi['red']),
        ('Ansi 2 Color', ansi['green']),
        ('Ansi 3 Color', ansi['yellow']),
        ('Ansi 4 Color', ansi['blue']),
        ('Ansi 5 Color', ansi['magenta']),
        ('Ansi 6 Color', ansi['cyan']),
        ('Ansi 7 Color', ansi['white']),
        ('Ansi 8 Color', ansi_bright['black']),
        ('Ansi 9 Color', ansi_bright['red']),
        ('Ansi 10 Color', ansi_bright['green']),
        ('Ansi 11 Color', ansi_bright['yellow']),
        ('Ansi 12 Color', ansi_bright['blue']),
        ('Ansi 13 Color', ansi_bright['magenta']),
        ('Ansi 14 Color', ansi_bright['cyan']),
        ('Ansi 15 Color', ansi_bright['white']),
    ]
    
    for key, val in order:
        out.append(iterm_color_block(key, val))
        
    out.append(ITERM_FOOTER)
    return ''.join(out)

def generate_opencode(palette: dict) -> str:
    """Generate OpenCode theme JSON with both dark and light variants."""

    def c(variant: str, section: str, key: str) -> str:
        return palette[variant][section][key]

    def pair(section: str, key: str) -> dict:
        return {"dark": c("dark", section, key), "light": c("light", section, key)}

    theme = {
        "$schema": "https://opencode.ai/theme.json",
        "defs": {},
        "theme": {
            "primary": pair("accents", "blue"),
            "secondary": pair("accents", "purple"),
            "accent": pair("accents", "cyan"),
            "error": pair("status", "error"),
            "warning": pair("status", "warning"),
            "success": pair("status", "success"),
            "info": pair("status", "info"),
            "text": pair("base", "fg"),
            "textMuted": pair("base", "fg_dim"),
            "background": pair("base", "bg"),
            "backgroundPanel": pair("base", "bg_light"),
            "backgroundElement": pair("base", "bg_dark"),
            "border": pair("ui", "border"),
            "borderActive": {"dark": c("dark", "accents", "cyan"), "light": c("light", "accents", "cyan")},
            "borderSubtle": pair("ui", "border"),
            "diffAdded": {"dark": c("dark", "git", "added"), "light": c("light", "git", "added")},
            "diffRemoved": {"dark": c("dark", "git", "deleted"), "light": c("light", "git", "deleted")},
            "diffContext": pair("base", "fg_dim"),
            "diffHunkHeader": pair("ui", "border"),
            "diffHighlightAdded": {"dark": c("dark", "git", "added"), "light": c("light", "git", "added")},
            "diffHighlightRemoved": {"dark": c("dark", "git", "deleted"), "light": c("light", "git", "deleted")},
            "diffAddedBg": pair("diff", "add"),
            "diffRemovedBg": pair("diff", "delete"),
            "diffContextBg": pair("base", "bg"),
            "diffLineNumber": pair("ui", "line_number"),
            "diffAddedLineNumberBg": pair("diff", "add"),
            "diffRemovedLineNumberBg": pair("diff", "delete"),
            "markdownText": pair("base", "fg"),
            "markdownHeading": pair("accents", "yellow"),
            "markdownLink": pair("accents", "blue"),
            "markdownLinkText": pair("accents", "cyan"),
            "markdownCode": pair("accents", "green"),
            "markdownBlockQuote": pair("base", "fg_dim"),
            "markdownEmph": pair("accents", "orange"),
            "markdownStrong": pair("accents", "yellow"),
            "markdownHorizontalRule": pair("ui", "border"),
            "markdownListItem": pair("accents", "yellow"),
            "markdownListEnumeration": pair("accents", "orange"),
            "markdownImage": pair("accents", "blue"),
            "markdownImageText": pair("accents", "cyan"),
            "markdownCodeBlock": pair("base", "fg"),
            "syntaxComment": pair("semantic", "comment"),
            "syntaxKeyword": pair("semantic", "keyword"),
            "syntaxFunction": pair("semantic", "function"),
            "syntaxVariable": pair("semantic", "variable"),
            "syntaxString": pair("semantic", "string"),
            "syntaxNumber": pair("semantic", "number"),
            "syntaxType": pair("semantic", "type"),
            "syntaxOperator": pair("semantic", "operator"),
            "syntaxPunctuation": pair("semantic", "punctuation"),
        }
    }
    return json.dumps(theme, indent=4) + "\n"

def get_nested_val(data, path_str):
    """Retrieve nested dictionary value using a dot-separated path string."""
    parts = path_str.split('.')
    cur = data
    for part in parts:
        cur = cur[part]
    return cur

def render_template_obj(obj, palette, variant):
    """Recursively render template placeholders in dict or list structures."""
    if isinstance(obj, str):
        if obj.startswith('{{') and obj.endswith('}}'):
            path = obj[2:-2]
            return get_nested_val(palette[variant], path)
        elif '{{' in obj:
            m = re.match(r'\{\{([^}]+)\}\}(.*)', obj)
            if m:
                path = m.group(1)
                suffix = m.group(2)
                val = get_nested_val(palette[variant], path)
                return f"{val}{suffix}"
        return obj
    elif isinstance(obj, dict):
        return {k: render_template_obj(v, palette, variant) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [render_template_obj(x, palette, variant) for x in obj]
    return obj

def main():
    if not PALETTE_FILE.exists():
        print(f"Error: reference palette not found at {PALETTE_FILE}")
        return
        
    palette = json.loads(PALETTE_FILE.read_text())
    
    # 1. Generate Terminal Themes
    for variant in ['dark', 'light']:
        print(f"Generating terminal configs for '{variant}' variant...")
        
        # Kitty
        kitty_suffix = "-light" if variant == "light" else ""
        kitty_content = generate_kitty(palette, variant)
        kitty_path = ROOT / "kitty" / f"guttenbergovitz{kitty_suffix}.conf"
        kitty_path.write_text(kitty_content)
        print(f"  ✔ Kitty: {kitty_path.name}")
        
        # Ghostty
        ghostty_suffix = "-light" if variant == "light" else ""
        ghostty_content = generate_ghostty(palette, variant)
        ghostty_path = ROOT / "ghostty" / f"guttenbergovitz{ghostty_suffix}"
        ghostty_path.write_text(ghostty_content)
        print(f"  ✔ Ghostty: {ghostty_path.name}")
        
        # Warp
        warp_suffix = "-light" if variant == "light" else ""
        warp_content = generate_warp(palette, variant)
        warp_path = ROOT / "warp" / f"guttenbergovitz{warp_suffix}.yaml"
        warp_path.write_text(warp_content)
        print(f"  ✔ Warp: {warp_path.name}")
        
        # Zellij
        zellij_suffix = "-light" if variant == "light" else ""
        zellij_content = generate_zellij(palette, variant)
        zellij_path = ROOT / "zellij" / f"guttenbergovitz{zellij_suffix}.kdl"
        zellij_path.write_text(zellij_content)
        print(f"  ✔ Zellij: {zellij_path.name}")
        
        # iTerm
        iterm_name = "Guttenbergovitz-Light" if variant == "light" else "Guttenbergovitz"
        iterm_content = generate_iterm(palette, variant)
        iterm_path = ROOT / "iterm" / f"{iterm_name}.itermcolors"
        iterm_path.write_text(iterm_content)
        print(f"  ✔ iTerm: {iterm_path.name}")

    # 2. Render Editor Themes from Templates
    print("\nRendering editor themes from templates...")
    
    # VS Code (dark & light)
    for variant in ['dark', 'light']:
        suffix = "-light" if variant == "light" else ""
        tmpl_file = TEMPLATES_DIR / f"vscode-{variant}.json.tmpl"
        if tmpl_file.exists():
            tmpl_data = json.loads(tmpl_file.read_text())
            rendered = render_template_obj(tmpl_data, palette, variant)
            dest_file = ROOT / "vscode" / "themes" / f"guttenbergovitz{suffix}-color-theme.json"
            dest_file.write_text(json.dumps(rendered, indent=4))
            print(f"  ✔ VS Code ({variant}): {dest_file.name}")
            
    # 3. Generate OpenCode Theme
    print("\nGenerating OpenCode theme...")
    opencode_content = generate_opencode(palette)
    opencode_dir = ROOT / "opencode"
    opencode_dir.mkdir(exist_ok=True)
    opencode_path = opencode_dir / "guttenbergovitz.json"
    opencode_path.write_text(opencode_content)
    print(f"  ✔ OpenCode: {opencode_path.name}")

    # Zed
    zed_tmpl_file = TEMPLATES_DIR / "zed.json.tmpl"
    if zed_tmpl_file.exists():
        zed_tmpl = json.loads(zed_tmpl_file.read_text())
        for theme in zed_tmpl.get("themes", []):
            theme_variant = theme.get("appearance", "dark")
            theme["style"] = render_template_obj(theme["style"], palette, theme_variant)
        dest_file = ROOT / "zed" / "guttenbergovitz.json"
        dest_file.write_text(json.dumps(zed_tmpl, indent=4))
        print(f"  ✔ Zed (combined): {dest_file.name}")

if __name__ == '__main__':
    main()
