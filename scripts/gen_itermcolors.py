#!/usr/bin/env python3
import json
from pathlib import Path

TPL_HEADER = """<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">
<plist version=\"1.0\">
<dict>
"""

TPL_FOOTER = """
</dict>
</plist>
"""

def hex_to_rgb_f(c: str):
    c = c.lstrip('#')
    r = int(c[0:2], 16) / 255.0
    g = int(c[2:4], 16) / 255.0
    b = int(c[4:6], 16) / 255.0
    return r, g, b

def color_block(key: str, hex_color: str) -> str:
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
\t</dict>
"""

def main():
    root = Path(__file__).resolve().parents[1]
    palette = json.loads((root / 'palette.json').read_text())
    dark = palette['dark']
    ansi = dark['ansi_remap']

    out = []
    out.append(TPL_HEADER)

    # Core UI colors
    out.append(color_block('Background Color', dark['base']['bg']))
    out.append(color_block('Foreground Color', dark['base']['fg']))
    out.append(color_block('Cursor Color', dark['base']['fg']))
    out.append(color_block('Selection Color', dark['ui']['selection']))
    out.append(color_block('Selected Text Color', dark['base']['bg']))

    # ANSI 0..15
    order = [
        ('Ansi 0 Color', 'black'),
        ('Ansi 1 Color', 'red'),
        ('Ansi 2 Color', 'green'),
        ('Ansi 3 Color', 'yellow'),
        ('Ansi 4 Color', 'blue'),
        ('Ansi 5 Color', 'magenta'),
        ('Ansi 6 Color', 'cyan'),
        ('Ansi 7 Color', 'white'),
        ('Ansi 8 Color', 'bright_black'),
        ('Ansi 9 Color', 'bright_red'),
        ('Ansi 10 Color', 'bright_green'),
        ('Ansi 11 Color', 'bright_yellow'),
        ('Ansi 12 Color', 'bright_blue'),
        ('Ansi 13 Color', 'bright_magenta'),
        ('Ansi 14 Color', 'bright_cyan'),
        ('Ansi 15 Color', 'bright_white'),
    ]
    for key, name in order:
        out.append(color_block(key, ansi[name]))

    out.append(TPL_FOOTER)

    out_path = root / 'iterm' / 'Guttenbergovitz.itermcolors'
    out_path.write_text(''.join(out))
    print(f"Wrote {out_path}")

if __name__ == '__main__':
    main()

