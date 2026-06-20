#!/usr/bin/env python3
"""
Generate terminal and multiplexer themes from palette.json.
Supports Kitty, Ghostty, Warp, Zellij, and iTerm (both light and dark variants).
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTE_FILE = ROOT / "palette.json"

# plist header and footer templates for iTerm colors generation
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
    return f"""
\t<key>{key}</key>
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
\t\t<key>/key>
\t\t<string>srgb</string>
\t\t<key>Green Component</key>
\t\t<real>{g:.9f}</real>
\t\t<key>Red Component</key>
\t\t<real>{r:.9f}</real>
\t</dict>
"""

# Wait, let's fix the duplicated tags in iterm_color_block
# The original script had:
#     return f"""
# 	<key>{key}</key>
# 	<dict>
# 		<key>Alpha Component</key>
# 		<real>1</real>
# 		<key>Blue Component</key>
# 		<real>{b:.9f}</real>
# 		<key>Color Space</key>
# 		<string>srgb</string>
# 		<key>Green Component</key>
# 		<real>{g:.9f}</real>
# 		<key>Red Component</key>
# 		<real>{r:.9f}</real>
# 	</dict>
# """

def iterm_color_block_correct(key: str, hex_color: str) -> str:
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
    
    out.append(iterm_color_block_correct('Background Color', base['bg']))
    out.append(iterm_color_block_correct('Foreground Color', base['fg']))
    out.append(iterm_color_block_correct('Cursor Color', ui['cursor']))
    out.append(iterm_color_block_correct('Selection Color', ui['selection']))
    out.append(iterm_color_block_correct('Selected Text Color', base['bg']))
    
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
        out.append(iterm_color_block_correct(key, val))
        
    out.append(ITERM_FOOTER)
    return ''.join(out)

def main():
    if not PALETTE_FILE.exists():
        print(f"Error: reference palette not found at {PALETTE_FILE}")
        return
        
    palette = json.loads(PALETTE_FILE.read_text())
    
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

if __name__ == '__main__':
    main()
