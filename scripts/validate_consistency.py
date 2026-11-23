#!/usr/bin/env python3
"""
Validate color consistency across all Guttenbergovitz theme implementations.
Reference: palette.json (which mirrors VSCode theme)
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple

ROOT = Path(__file__).parent.parent
PALETTE_FILE = ROOT / "palette.json"

class ColorValidator:
    def __init__(self):
        self.palette = self.load_palette()
        self.issues = []
        self.warnings = []
        
    def load_palette(self) -> dict:
        """Load the reference palette"""
        with open(PALETTE_FILE) as f:
            return json.load(f)
    
    def normalize_color(self, color: str) -> str:
        """Normalize color to lowercase hex format"""
        if not color:
            return ""
        color = color.strip().lower()
        if not color.startswith('#'):
            color = f'#{color}'
        return color
    
    def check_color(self, impl_name: str, color_name: str, expected: str, actual: str, context: str = ""):
        """Check if a color matches the expected value"""
        expected = self.normalize_color(expected)
        actual = self.normalize_color(actual)
        
        if not actual:
            self.issues.append({
                'severity': 'error',
                'implementation': impl_name,
                'color_name': color_name,
                'expected': expected,
                'actual': 'MISSING',
                'context': context
            })
            return False
        
        if expected != actual:
            self.issues.append({
                'severity': 'error',
                'implementation': impl_name,
                'color_name': color_name,
                'expected': expected,
                'actual': actual,
                'context': context
            })
            return False
        
        return True
    
    def validate_vscode_variant(self, variant: str) -> bool:
        """Validate VSCode theme variant against palette"""
        suffix = "-light" if variant == "light" else ""
        filename = f"guttenbergovitz{suffix}-color-theme.json"
        print(f"  🔍 Validating VSCode theme ({variant})...")
        vscode_file = ROOT / "vscode" / "themes" / filename
        
        if not vscode_file.exists():
            self.issues.append({
                'severity': 'error',
                'implementation': 'VSCode',
                'color_name': f'{variant} theme file',
                'expected': 'File exists',
                'actual': 'NOT FOUND',
                'context': str(vscode_file)
            })
            return False
            
        with open(vscode_file) as f:
            theme = json.load(f)
        
        colors = theme['colors']
        palette = self.palette[variant]
        
        checks = [
            ('editor.background', palette['base']['bg']),
            ('editor.foreground', palette['base']['fg']),
            ('sideBar.background', palette['base']['bg_dark']),
            ('editor.lineHighlightBackground', palette['ui']['line_highlight']),
            ('editor.selectionBackground', palette['ui']['selection']),
            ('editorLineNumber.foreground', palette['ui']['line_number']),
            ('focusBorder', palette['ui']['border']),
        ]
        
        all_ok = True
        for key, expected in checks:
            actual = colors.get(key, '')
            if not self.check_color(f'VSCode ({variant})', key, expected, actual):
                all_ok = False
        
        # Check token colors
        for token in theme['tokenColors']:
            name = token.get('name', '')
            if 'Comment' in name:
                fg = token['settings'].get('foreground', '')
                if not self.check_color(f'VSCode ({variant})', 'comment', palette['semantic']['comment'], fg, name):
                    all_ok = False
            elif 'Keyword' in name:
                fg = token['settings'].get('foreground', '')
                if not self.check_color(f'VSCode ({variant})', 'keyword', palette['semantic']['keyword'], fg, name):
                    all_ok = False
        
        return all_ok

    def validate_vscode(self) -> bool:
        """Validate VSCode themes against palette"""
        print("\n🔍 Validating VSCode themes...")
        dark_ok = self.validate_vscode_variant('dark')
        light_ok = self.validate_vscode_variant('light')
        
        all_ok = dark_ok and light_ok
        if all_ok:
            print("  ✅ VSCode themes are consistent")
        else:
            print("  ❌ VSCode themes have inconsistencies")
        return all_ok
    
    def validate_neovim_variant(self, variant: str, block_content: str) -> bool:
        """Validate Neovim theme variant colors"""
        palette = self.palette[variant]
        
        colors = {}
        for match in re.finditer(r'(\w+)\s*=\s*"(#[0-9a-fA-F]{6})"', block_content):
            colors[match.group(1)] = match.group(2)
            
        checks = [
            ('bg', palette['base']['bg']),
            ('bg_dark', palette['base']['bg_dark']),
            ('bg_light', palette['base']['bg_light']),
            ('fg', palette['base']['fg']),
            ('comment', palette['semantic']['comment']),
            ('red', palette['accents']['red']),
            ('green', palette['accents']['green']),
            ('yellow', palette['accents']['yellow']),
            ('orange', palette['accents']['orange']),
            ('selection', palette['ui']['selection']),
            ('border', palette['ui']['border']),
        ]
        
        all_ok = True
        for key, expected in checks:
            actual = colors.get(key, '')
            if not self.check_color(f'Neovim ({variant})', key, expected, actual):
                all_ok = False
        return all_ok

    def validate_neovim(self) -> bool:
        """Validate Neovim theme against palette"""
        print("\n🔍 Validating Neovim theme...")
        nvim_file = ROOT / "lua" / "guttenbergovitz" / "init.lua"
        
        with open(nvim_file) as f:
            content = f.read()
            
        parts = content.split("} or {")
        if len(parts) < 2:
            print("  ❌ Could not parse Neovim theme variants")
            return False
            
        light_ok = self.validate_neovim_variant('light', parts[0])
        dark_ok = self.validate_neovim_variant('dark', parts[1])
        
        all_ok = light_ok and dark_ok
        if all_ok:
            print("  ✅ Neovim theme is consistent")
        else:
            print("  ❌ Neovim theme has inconsistencies")
        return all_ok
    
    def validate_helix_variant(self, variant: str) -> bool:
        """Validate Helix theme variant against the reference palette.
        
        Args:
            variant: Either 'dark' or 'light'.
            
        Returns:
            True if all colors in Helix theme variant match the reference palette, False otherwise.
        """
        suffix = "-light" if variant == "light" else ""
        filename = f"guttenbergovitz{suffix}.toml"
        print(f"  🔍 Validating Helix theme ({variant})...")
        helix_file = ROOT / "helix" / filename
        
        if not helix_file.exists():
            self.issues.append({
                'severity': 'error',
                'implementation': 'Helix',
                'color_name': f'{variant} theme file',
                'expected': 'File exists',
                'actual': 'NOT FOUND',
                'context': str(helix_file)
            })
            return False
            
        with open(helix_file) as f:
            content = f.read()
        
        palette = self.palette[variant]
        
        # Extract the [palette] section from TOML file
        palette_match = re.search(r'\[palette\](.*)', content, re.DOTALL)
        if not palette_match:
            self.issues.append({
                'severity': 'error',
                'implementation': f'Helix ({variant})',
                'color_name': 'palette section',
                'expected': '[palette] section present',
                'actual': 'NOT FOUND',
                'context': str(helix_file)
            })
            return False
        
        colors = {}
        for match in re.finditer(r'(\w+)\s*=\s*"(#[0-9a-fA-F]{6})"', palette_match.group(1)):
            colors[match.group(1)] = match.group(2)
        
        checks = [
            ('bg0', palette['base']['bg']),
            ('bg1', palette['base']['bg_dark']),
            ('bg2', palette['base']['bg_light']),
            ('fg0', palette['base']['fg']),
            ('comment', palette['semantic']['comment']),
            ('red', palette['accents']['red']),
            ('green', palette['accents']['green']),
            ('yellow', palette['accents']['yellow']),
            ('orange', palette['accents']['orange']),
            ('bg3', palette['ui']['selection']),
        ]
        
        all_ok = True
        for key, expected in checks:
            actual = colors.get(key, '')
            if not self.check_color(f'Helix ({variant})', key, expected, actual):
                all_ok = False
        
        return all_ok

    def validate_helix(self) -> bool:
        """Validate both Helix dark and light themes against the palette.
        
        Returns:
            True if all Helix themes are consistent, False otherwise.
        """
        print("\n🔍 Validating Helix themes...")
        dark_ok = self.validate_helix_variant('dark')
        light_ok = self.validate_helix_variant('light')
        
        all_ok = dark_ok and light_ok
        if all_ok:
            print("  ✅ Helix themes are consistent")
        else:
            print("  ❌ Helix themes have inconsistencies")
        return all_ok

    def validate_kitty_variant(self, variant: str) -> bool:
        """Validate a single Kitty theme variant against the reference palette."""
        suffix = "-light" if variant == "light" else ""
        kitty_file = ROOT / "kitty" / f"guttenbergovitz{suffix}.conf"
        print(f"  🔍 Validating Kitty theme ({variant})...")

        if not kitty_file.exists():
            self.issues.append({
                'severity': 'error',
                'implementation': f'Kitty ({variant})',
                'color_name': 'theme file',
                'expected': 'File exists',
                'actual': 'NOT FOUND',
                'context': str(kitty_file)
            })
            return False

        content = kitty_file.read_text()
        palette = self.palette[variant]

        colors = {}
        for match in re.finditer(r'(\w+)\s+(#[0-9a-fA-F]{6})', content):
            colors[match.group(1)] = match.group(2)

        for match in re.finditer(r'color(\d+)\s+(#[0-9a-fA-F]{6})', content):
            colors[f'color{match.group(1)}'] = match.group(2)

        checks = [
            ('background', palette['base']['bg']),
            ('foreground', palette['base']['fg']),
            ('cursor', palette['ui']['cursor']),
            ('color0', palette['terminal']['ansi']['black']),
            ('color1', palette['terminal']['ansi']['red']),
            ('color2', palette['terminal']['ansi']['green']),
            ('color3', palette['terminal']['ansi']['yellow']),
            ('color8', palette['terminal']['ansi_bright']['black']),
        ]

        all_ok = True
        for key, expected in checks:
            actual = colors.get(key, '')
            if not self.check_color(f'Kitty ({variant})', key, expected, actual):
                all_ok = False
        return all_ok

    def validate_kitty(self) -> bool:
        """Validate both dark and light Kitty themes against the reference palette."""
        print("\n🔍 Validating Kitty themes...")
        dark_ok = self.validate_kitty_variant('dark')
        light_ok = self.validate_kitty_variant('light')
        all_ok = dark_ok and light_ok
        if all_ok:
            print("  ✅ Kitty themes are consistent")
        else:
            print("  ❌ Kitty themes have inconsistencies")
        return all_ok

    def validate_zed(self) -> bool:
        """Validate both dark and light Zed themes against the reference palette.
        
        Returns:
            True if both Zed themes are consistent with the palette, False otherwise.
        """
        print("\n🔍 Validating Zed themes...")
        zed_file = ROOT / "zed" / "guttenbergovitz.json"
        
        if not zed_file.exists():
            self.issues.append({
                'severity': 'error',
                'implementation': 'Zed',
                'color_name': 'theme file',
                'expected': 'File exists',
                'actual': 'NOT FOUND',
                'context': str(zed_file)
            })
            return False
            
        with open(zed_file) as f:
            data = json.load(f)
            
        all_ok = True
        found_variants = []
        for theme in data.get('themes', []):
            variant = theme.get('appearance', '')
            found_variants.append(variant)
            if variant not in ['dark', 'light']:
                continue
                
            print(f"  🔍 Validating Zed theme ({variant})...")
            style = theme.get('style', {})
            palette = self.palette[variant]
            
            checks = [
                ('editor.background', palette['base']['bg']),
                ('text', palette['base']['fg']),
                ('panel.background', palette['base']['bg_dark']),
                ('editor.active_line.background', palette['ui']['line_highlight']),
                ('editor.line_number', palette['ui']['line_number']),
                ('border', palette['ui']['border']),
            ]
            
            for key, expected in checks:
                actual = style.get(key, '')
                if not self.check_color(f'Zed ({variant})', key, expected, actual):
                    all_ok = False
                    
            # Check syntax highlighting colors
            syntax = style.get('syntax', {})
            syntax_checks = [
                ('comment', palette['semantic']['comment']),
                ('keyword', palette['semantic']['keyword']),
                ('string', palette['semantic']['string']),
                ('type', palette['semantic']['type']),
                ('function', palette['semantic']['function']),
            ]
            for key, expected in syntax_checks:
                actual = syntax.get(key, {}).get('color', '')
                if not self.check_color(f'Zed ({variant}) syntax', key, expected, actual):
                    all_ok = False
                    
        for req in ['dark', 'light']:
            if req not in found_variants:
                self.issues.append({
                    'severity': 'error',
                    'implementation': 'Zed',
                    'color_name': f'{req} variant',
                    'expected': 'Variant present',
                    'actual': 'MISSING',
                    'context': ''
                })
                all_ok = False
                
        if all_ok:
            print("  ✅ Zed themes are consistent")
        else:
            print("  ❌ Zed themes have inconsistencies")
        return all_ok

    def validate_vim(self) -> bool:
        """Validate both dark and light Vim colorscheme configurations.
        
        Returns:
            True if both Vim background configurations are consistent, False otherwise.
        """
        print("\n🔍 Validating Vim theme...")
        vim_file = ROOT / "vim" / "colors" / "guttenbergovitz.vim"
        
        if not vim_file.exists():
            self.issues.append({
                'severity': 'error',
                'implementation': 'Vim',
                'color_name': 'theme file',
                'expected': 'File exists',
                'actual': 'NOT FOUND',
                'context': str(vim_file)
            })
            return False
            
        with open(vim_file) as f:
            content = f.read()
            
        # Extract the two s:colors dictionary blocks (light and dark)
        blocks = re.findall(r'let s:colors = \{(.*?)\}', content, re.DOTALL)
        if len(blocks) < 2:
            self.issues.append({
                'severity': 'error',
                'implementation': 'Vim',
                'color_name': 's:colors blocks',
                'expected': 'At least 2 blocks found',
                'actual': f'{len(blocks)} blocks found',
                'context': ''
            })
            return False
            
        all_ok = True
        # ZIP expects light theme as the first block and dark theme as the second block
        for variant, block in zip(['light', 'dark'], blocks):
            print(f"  🔍 Validating Vim theme ({variant})...")
            colors = {}
            for match in re.finditer(r"\\\s*'(\w+)'\s*:\s*'([^']+)'", block):
                colors[match.group(1)] = match.group(2)
                
            palette = self.palette[variant]
            
            checks = [
                ('bg', palette['base']['bg']),
                ('bg_dark', palette['base']['bg_dark']),
                ('bg_light', palette['base']['bg_light']),
                ('fg', palette['base']['fg']),
                ('comment', palette['semantic']['comment']),
                ('red', palette['accents']['red']),
                ('green', palette['accents']['green']),
                ('yellow', palette['accents']['yellow']),
                ('orange', palette['accents']['orange']),
                ('selection', palette['ui']['selection']),
                ('border', palette['ui']['border']),
            ]
            
            for key, expected in checks:
                actual = colors.get(key, '')
                if not self.check_color(f'Vim ({variant})', key, expected, actual):
                    all_ok = False
                    
        if all_ok:
            print("  ✅ Vim theme is consistent")
        else:
            print("  ❌ Vim theme has inconsistencies")
        return all_ok

    def validate_zellij(self) -> bool:
        """Validate both dark and light Zellij themes against the reference palette.

        Zellij themes use the UI-component spec (base/background/emphasis_N
        attributes with 'r g b' values), so colors are compared as RGB triples.

        Returns:
            True if all Zellij themes are consistent, False otherwise.
        """
        print("\n🔍 Validating Zellij themes...")
        all_ok = True

        for variant in ['dark', 'light']:
            suffix = "-light" if variant == "light" else ""
            filename = f"guttenbergovitz{suffix}.kdl"
            zellij_file = ROOT / "zellij" / filename

            if not zellij_file.exists():
                self.issues.append({
                    'severity': 'error',
                    'implementation': 'Zellij',
                    'color_name': f'{variant} theme file',
                    'expected': 'File exists',
                    'actual': 'NOT FOUND',
                    'context': str(zellij_file)
                })
                all_ok = False
                continue

            print(f"  🔍 Validating Zellij theme ({variant})...")
            content = zellij_file.read_text()
            palette = self.palette[variant]
            base = palette['base']
            ui = palette['ui']
            accents = palette['accents']

            def rgb_to_hex(rgb: str) -> str:
                parts = rgb.split()
                if len(parts) != 3:
                    return ""
                try:
                    return "#{:02x}{:02x}{:02x}".format(*[int(p) for p in parts])
                except ValueError:
                    return ""

            fg = base['fg']
            bg = base['bg']
            bg_dark = base['bg_dark']
            bg_light = base['bg_light']
            selection = ui['selection']
            border = ui['border']
            red = accents['red']
            green = accents['green']
            yellow = accents['yellow']
            orange = accents['orange']
            blue = accents['blue']
            purple = accents['purple']
            cyan = accents['cyan']
            em0, em1, em2, em3 = orange, blue, green, purple

            expected = {
                'text_unselected': {'base': fg, 'background': bg},
                'text_selected': {'base': fg, 'background': selection},
                'ribbon_unselected': {'base': fg, 'background': bg_light},
                'ribbon_selected': {'base': bg_dark, 'background': fg},
                'table_title': {'base': yellow, 'background': bg},
                'table_cell_unselected': {'base': fg, 'background': bg},
                'table_cell_selected': {'base': fg, 'background': selection},
                'list_unselected': {'base': fg, 'background': bg},
                'list_selected': {'base': fg, 'background': selection},
                'frame_unselected': {'base': border, 'background': bg},
                'frame_selected': {'base': orange, 'background': bg},
                'frame_highlight': {'base': yellow, 'background': bg},
                'exit_code_success': {'base': green, 'background': bg},
                'exit_code_error': {'base': red, 'background': bg},
            }
            players = [orange, cyan, green, yellow, purple, blue, red, fg, bg_light, bg_dark]

            # Parse the KDL into {component: {attribute: 'r g b'}}
            actual = {}
            current = None
            for line in content.splitlines():
                stripped = line.strip()
                m = re.match(r'(\w+)\s*\{', stripped)
                if m:
                    current = m.group(1)
                    actual.setdefault(current, {})
                    continue
                m = re.match(
                    r'(base|background|emphasis_[0-3]|player_\d+)\s+(\d+)\s+(\d+)\s+(\d+)',
                    stripped
                )
                if m and current:
                    actual[current][m.group(1)] = f"{m.group(2)} {m.group(3)} {m.group(4)}"

            for comp_name, attrs in expected.items():
                for attr, hex_color in attrs.items():
                    actual_rgb = actual.get(comp_name, {}).get(attr, '')
                    if not self.check_color(
                        f'Zellij ({variant})', f'{comp_name}.{attr}',
                        hex_color, rgb_to_hex(actual_rgb)
                    ):
                        all_ok = False
                for attr, hex_color in zip(('emphasis_0', 'emphasis_1', 'emphasis_2', 'emphasis_3'),
                                           (em0, em1, em2, em3)):
                    actual_rgb = actual.get(comp_name, {}).get(attr, '')
                    if not self.check_color(
                        f'Zellij ({variant})', f'{comp_name}.{attr}',
                        hex_color, rgb_to_hex(actual_rgb)
                    ):
                        all_ok = False

            for i, hex_color in enumerate(players, start=1):
                attr = f'player_{i}'
                actual_rgb = actual.get('multiplayer_user_colors', {}).get(attr, '')
                if not self.check_color(
                    f'Zellij ({variant})', f'multiplayer_user_colors.{attr}',
                    hex_color, rgb_to_hex(actual_rgb)
                ):
                    all_ok = False

        if all_ok:
            print("  ✅ Zellij themes are consistent")
        else:
            print("  ❌ Zellij themes have inconsistencies")
        return all_ok

    def validate_opencode(self) -> bool:
        """Validate OpenCode theme against the reference palette."""
        print("\n🔍 Validating OpenCode theme...")
        opencode_file = ROOT / "opencode" / "guttenbergovitz.json"

        if not opencode_file.exists():
            self.issues.append({
                'severity': 'error',
                'implementation': 'OpenCode',
                'color_name': 'theme file',
                'expected': 'File exists',
                'actual': 'NOT FOUND',
                'context': str(opencode_file)
            })
            return False

        with open(opencode_file) as f:
            data = json.load(f)

        theme = data.get('theme', {})
        all_ok = True

        mapping = {
            'text': ('base', 'fg'),
            'textMuted': ('base', 'fg_dim'),
            'background': ('base', 'bg'),
            'backgroundPanel': ('base', 'bg_light'),
            'backgroundElement': ('base', 'bg_dark'),
            'border': ('ui', 'border'),
            'syntaxComment': ('semantic', 'comment'),
            'syntaxKeyword': ('semantic', 'keyword'),
            'syntaxFunction': ('semantic', 'function'),
            'syntaxVariable': ('semantic', 'variable'),
            'syntaxString': ('semantic', 'string'),
            'syntaxNumber': ('semantic', 'number'),
            'syntaxType': ('semantic', 'type'),
            'syntaxOperator': ('semantic', 'operator'),
            'syntaxPunctuation': ('semantic', 'punctuation'),
        }

        for variant in ['dark', 'light']:
            palette = self.palette[variant]
            for key, (section, color_key) in mapping.items():
                entry = theme.get(key, {})
                actual = entry.get(variant, '')
                expected = palette[section][color_key]
                if not self.check_color(f'OpenCode ({variant})', key, expected, actual):
                    all_ok = False

        if all_ok:
            print("  ✅ OpenCode theme is consistent")
        else:
            print("  ❌ OpenCode theme has inconsistencies")
        return all_ok

    def validate_herdr(self) -> bool:
        """Validate both dark and light Herdr [theme.custom] fragments against the palette.

        Returns:
            True if all Herdr themes are consistent, False otherwise.
        """
        print("\n🔍 Validating Herdr themes...")
        all_ok = True

        for variant in ['dark', 'light']:
            suffix = "-light" if variant == "light" else ""
            filename = f"guttenbergovitz{suffix}.toml"
            herdr_file = ROOT / "herdr" / filename

            if not herdr_file.exists():
                self.issues.append({
                    'severity': 'error',
                    'implementation': 'Herdr',
                    'color_name': f'{variant} theme file',
                    'expected': 'File exists',
                    'actual': 'NOT FOUND',
                    'context': str(herdr_file)
                })
                all_ok = False
                continue

            print(f"  🔍 Validating Herdr theme ({variant})...")
            content = herdr_file.read_text()
            palette = self.palette[variant]
            base = palette['base']
            accents = palette['accents']
            ui = palette['ui']
            status = palette['status']

            mapping = {
                'accent': accents['orange'],
                'panel_bg': base['bg'],
                'surface0': base['bg_light'],
                'surface1': ui['selection'],
                'surface_dim': base['bg_dark'],
                'overlay0': base['fg_dim'],
                'overlay1': base['fg_dark'],
                'text': base['fg'],
                'subtext0': base['fg_dim'],
                'mauve': accents['purple'],
                'green': accents['green'],
                'yellow': accents['yellow'],
                'red': status['error'],
                'blue': accents['blue'],
                'teal': accents['cyan'],
                'peach': accents['orange'],
            }

            colors = {}
            for match in re.finditer(r'(\w+)\s*=\s*"(#[0-9a-fA-F]{6})"', content):
                colors[match.group(1)] = match.group(2)

            for key, expected in mapping.items():
                actual = colors.get(key, '')
                if not self.check_color(f'Herdr ({variant})', key, expected, actual):
                    all_ok = False

        if all_ok:
            print("  ✅ Herdr themes are consistent")
        else:
            print("  ❌ Herdr themes have inconsistencies")
        return all_ok

    def validate_ghostty(self) -> bool:
        """Validate both dark and light Ghostty themes against the palette."""
        print("\n🔍 Validating Ghostty themes...")
        all_ok = True
        for variant in ['dark', 'light']:
            suffix = "-light" if variant == "light" else ""
            ghostty_file = ROOT / "ghostty" / f"guttenbergovitz{suffix}"
            if not ghostty_file.exists():
                self.issues.append({
                    'severity': 'error',
                    'implementation': f'Ghostty ({variant})',
                    'color_name': 'theme file',
                    'expected': 'File exists',
                    'actual': 'NOT FOUND',
                    'context': str(ghostty_file)
                })
                all_ok = False
                continue

            print(f"  🔍 Validating Ghostty theme ({variant})...")
            content = ghostty_file.read_text()
            palette = self.palette[variant]
            colors = {}
            for m in re.finditer(r'^([\w-]+)\s*=\s*(#[0-9a-fA-F]{6})', content, re.M):
                colors[m.group(1)] = m.group(2)
            for m in re.finditer(r'^palette\s*=\s*(\d+)=(#[0-9a-fA-F]{6})', content, re.M):
                colors[f'palette_{m.group(1)}'] = m.group(2)

            checks = [
                ('background', palette['base']['bg']),
                ('foreground', palette['base']['fg']),
                ('cursor-color', palette['ui']['cursor']),
                ('selection-background', palette['ui']['selection']),
                ('palette_0', palette['terminal']['ansi']['black']),
                ('palette_1', palette['terminal']['ansi']['red']),
                ('palette_2', palette['terminal']['ansi']['green']),
                ('palette_3', palette['terminal']['ansi']['yellow']),
                ('palette_8', palette['terminal']['ansi_bright']['black']),
            ]
            for key, expected in checks:
                if not self.check_color(f'Ghostty ({variant})', key, expected, colors.get(key, '')):
                    all_ok = False

        print("  ✅ Ghostty themes are consistent" if all_ok else "  ❌ Ghostty themes have inconsistencies")
        return all_ok

    def validate_warp(self) -> bool:
        """Validate both dark and light Warp themes against the palette."""
        print("\n🔍 Validating Warp themes...")
        all_ok = True
        for variant in ['dark', 'light']:
            suffix = "-light" if variant == "light" else ""
            warp_file = ROOT / "warp" / f"guttenbergovitz{suffix}.yaml"
            if not warp_file.exists():
                self.issues.append({
                    'severity': 'error',
                    'implementation': f'Warp ({variant})',
                    'color_name': 'theme file',
                    'expected': 'File exists',
                    'actual': 'NOT FOUND',
                    'context': str(warp_file)
                })
                all_ok = False
                continue

            print(f"  🔍 Validating Warp theme ({variant})...")
            content = warp_file.read_text()
            palette = self.palette[variant]
            top_colors = {}
            for m in re.finditer(r'^(accent|background|cursor|foreground):\s*"?(#[0-9a-fA-F]{6})"?', content, re.M):
                top_colors[m.group(1)] = m.group(2)

            checks = [
                ('accent', palette['accents']['orange']),
                ('background', palette['base']['bg']),
                ('cursor', palette['base']['fg']),
                ('foreground', palette['base']['fg']),
            ]
            for key, expected in checks:
                if not self.check_color(f'Warp ({variant})', key, expected, top_colors.get(key, '')):
                    all_ok = False

        print("  ✅ Warp themes are consistent" if all_ok else "  ❌ Warp themes have inconsistencies")
        return all_ok

    def validate_tmux(self) -> bool:
        """Validate both dark and light tmux themes against the palette."""
        print("\n🔍 Validating tmux themes...")
        all_ok = True
        for variant in ['dark', 'light']:
            suffix = "-light" if variant == "light" else ""
            tmux_file = ROOT / "tmux" / f"guttenbergovitz{suffix}.tmux.conf"
            if not tmux_file.exists():
                self.issues.append({
                    'severity': 'error',
                    'implementation': f'tmux ({variant})',
                    'color_name': 'theme file',
                    'expected': 'File exists',
                    'actual': 'NOT FOUND',
                    'context': str(tmux_file)
                })
                all_ok = False
                continue

            print(f"  🔍 Validating tmux theme ({variant})...")
            content = tmux_file.read_text()
            palette = self.palette[variant]
            colors = dict(re.findall(r'^(thm_\w+)="(#[0-9a-fA-F]{6})"', content, re.M))

            checks = [
                ('thm_bg', palette['base']['bg']),
                ('thm_bg_dark', palette['base']['bg_dark']),
                ('thm_bg_light', palette['base']['bg_light']),
                ('thm_fg', palette['base']['fg']),
                ('thm_fg_dim', palette['base']['fg_dim']),
                ('thm_red', palette['accents']['red']),
                ('thm_green', palette['accents']['green']),
                ('thm_yellow', palette['accents']['yellow']),
                ('thm_orange', palette['accents']['orange']),
                ('thm_purple', palette['accents']['purple']),
                ('thm_cyan', palette['accents']['cyan']),
                ('thm_selection', palette['ui']['selection']),
            ]
            for key, expected in checks:
                if not self.check_color(f'tmux ({variant})', key, expected, colors.get(key, '')):
                    all_ok = False

        print("  ✅ tmux themes are consistent" if all_ok else "  ❌ tmux themes have inconsistencies")
        return all_ok

    def validate_claude_code(self) -> bool:
        """Validate both dark and light Claude Code themes against the palette."""
        print("\n🔍 Validating Claude Code themes...")
        all_ok = True
        for variant in ['dark', 'light']:
            suffix = "-light" if variant == "light" else ""
            cc_file = ROOT / "claude-code" / f"guttenbergovitz{suffix}.json"
            if not cc_file.exists():
                self.issues.append({
                    'severity': 'error',
                    'implementation': f'Claude Code ({variant})',
                    'color_name': 'theme file',
                    'expected': 'File exists',
                    'actual': 'NOT FOUND',
                    'context': str(cc_file)
                })
                all_ok = False
                continue

            print(f"  🔍 Validating Claude Code theme ({variant})...")
            data = json.loads(cc_file.read_text())
            ov = data.get('overrides', {})
            palette = self.palette[variant]
            checks = [
                ('background', palette['base']['bg']),
                ('text', palette['base']['fg']),
                ('subtle', palette['base']['fg_dim']),
                ('promptBackground', palette['base']['bg_dark']),
                ('userMessageBackground', palette['base']['bg_light']),
                ('accentPrimary', palette['accents']['orange']),
                ('accentSecondary', palette['accents']['yellow']),
                ('success', palette['accents']['green']),
                ('error', palette['accents']['red']),
                ('info', palette['accents']['cyan']),
                ('border', palette['ui']['border']),
                ('selection', palette['ui']['selection']),
            ]
            for key, expected in checks:
                if not self.check_color(f'Claude Code ({variant})', key, expected, ov.get(key, '')):
                    all_ok = False

        print("  ✅ Claude Code themes are consistent" if all_ok else "  ❌ Claude Code themes have inconsistencies")
        return all_ok

    def validate_pi(self) -> bool:
        """Validate both dark and light Pi themes against the palette."""
        print("\n🔍 Validating Pi themes...")
        all_ok = True
        for variant in ['dark', 'light']:
            suffix = "-light" if variant == "light" else ""
            pi_file = ROOT / "pi" / f"guttenbergovitz{suffix}.json"
            if not pi_file.exists():
                self.issues.append({
                    'severity': 'error',
                    'implementation': f'Pi ({variant})',
                    'color_name': 'theme file',
                    'expected': 'File exists',
                    'actual': 'NOT FOUND',
                    'context': str(pi_file)
                })
                all_ok = False
                continue

            print(f"  🔍 Validating Pi theme ({variant})...")
            data = json.loads(pi_file.read_text())
            v = data.get('vars', {})
            palette = self.palette[variant]
            checks = [
                ('bg', palette['base']['bg']),
                ('bgDark', palette['base']['bg_dark']),
                ('bgLight', palette['base']['bg_light']),
                ('fg', palette['base']['fg']),
                ('fgDim', palette['base']['fg_dim']),
                ('red', palette['accents']['red']),
                ('green', palette['accents']['green']),
                ('yellow', palette['accents']['yellow']),
                ('orange', palette['accents']['orange']),
                ('purple', palette['accents']['purple']),
                ('cyan', palette['accents']['cyan']),
                ('blue', palette['accents']['blue']),
                ('border', palette['ui']['border']),
            ]
            for key, expected in checks:
                if not self.check_color(f'Pi ({variant})', key, expected, v.get(key, '')):
                    all_ok = False

        print("  ✅ Pi themes are consistent" if all_ok else "  ❌ Pi themes have inconsistencies")
        return all_ok

    def validate_jetbrains(self) -> bool:
        """Validate both dark and light JetBrains .icls schemes against the palette."""
        print("\n🔍 Validating JetBrains themes...")
        all_ok = True
        for variant in ['dark', 'light']:
            filename = "Guttenbergovitz-Light.icls" if variant == "light" else "Guttenbergovitz.icls"
            jb_file = ROOT / "jetbrains" / filename
            if not jb_file.exists():
                self.issues.append({
                    'severity': 'error',
                    'implementation': f'JetBrains ({variant})',
                    'color_name': 'theme file',
                    'expected': 'File exists',
                    'actual': 'NOT FOUND',
                    'context': str(jb_file)
                })
                all_ok = False
                continue

            print(f"  🔍 Validating JetBrains theme ({variant})...")
            content = jb_file.read_text()
            palette = self.palette[variant]
            colors = dict(re.findall(r'<option name="([^"]+)" value="([0-9a-fA-F]{6})" />', content))
            checks = [
                ('CONSOLE_BACKGROUND_KEY', palette['base']['bg']),
                ('TOOL_WINDOW_BACKGROUND', palette['base']['bg_dark']),
                ('CARET_COLOR', palette['ui']['cursor']),
                ('LINE_NUMBERS_COLOR', palette['ui']['line_number']),
                ('SELECTION_BACKGROUND', palette['ui']['selection']),
                ('ADDED_LINES_COLOR', palette['git']['added']),
                ('DELETED_LINES_COLOR', palette['git']['deleted']),
                ('FILESTATUS_IDEA_FILESTATUS_IGNORED', palette['git']['ignored']),
            ]
            for key, expected in checks:
                if not self.check_color(f'JetBrains ({variant})', key, expected, colors.get(key, '')):
                    all_ok = False

        print("  ✅ JetBrains themes are consistent" if all_ok else "  ❌ JetBrains themes have inconsistencies")
        return all_ok

    def validate_all(self) -> bool:
        """Run all theme validations.
        
        Returns:
            True if all implementations are consistent, False otherwise.
        """
        print("=" * 80)
        print("GUTTENBERGOVITZ THEME - CONSISTENCY VALIDATION")
        print("=" * 80)
        
        results = []
        results.append(self.validate_vscode())
        results.append(self.validate_neovim())
        results.append(self.validate_helix())
        results.append(self.validate_kitty())
        results.append(self.validate_ghostty())
        results.append(self.validate_warp())
        results.append(self.validate_zed())
        results.append(self.validate_vim())
        results.append(self.validate_jetbrains())
        results.append(self.validate_zellij())
        results.append(self.validate_tmux())
        results.append(self.validate_herdr())
        results.append(self.validate_opencode())
        results.append(self.validate_claude_code())
        results.append(self.validate_pi())
        
        # Print summary
        print("\n" + "=" * 80)
        print("SUMMARY")
        print("=" * 80)
        
        if not self.issues:
            print("✅ All themes are consistent!")
            return True
        
        print(f"\n❌ Found {len(self.issues)} inconsistencies:\n")
        
        # Group by implementation
        by_impl = defaultdict(list)
        for issue in self.issues:
            by_impl[issue['implementation']].append(issue)
        
        for impl, issues in sorted(by_impl.items()):
            print(f"\n{impl} ({len(issues)} issues):")
            for issue in issues:
                if issue['actual'] == 'MISSING':
                    print(f"  ❌ Missing: {issue['color_name']}")
                else:
                    print(f"  ❌ {issue['color_name']}: {issue['actual']} ≠ {issue['expected']}")
                if issue['context']:
                    print(f"     Context: {issue['context']}")
        
        return False

def main():
    validator = ColorValidator()
    success = validator.validate_all()
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
