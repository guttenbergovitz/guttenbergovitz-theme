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
    
    def validate_helix(self) -> bool:
        """Validate Helix theme against palette"""
        print("\n🔍 Validating Helix theme...")
        helix_file = ROOT / "helix" / "guttenbergovitz.toml"
        
        with open(helix_file) as f:
            content = f.read()
        
        palette = self.palette['dark']
        
        # Extract palette section
        palette_match = re.search(r'\[palette\](.*)', content, re.DOTALL)
        if not palette_match:
            print("  ❌ Could not parse Helix theme")
            return False
        
        colors = {}
        for match in re.finditer(r'(\w+)\s*=\s*"(#[0-9a-fA-F]{6})"', palette_match.group(1)):
            colors[match.group(1)] = match.group(2)
        
        checks = [
            ('bg0', palette['base']['bg']),
            ('bg1', palette['base']['bg_dark']),
            ('bg2', palette['base']['bg_light']),
            ('fg0', palette['base']['fg']),
            ('gray', palette['semantic']['comment']),
            ('red', palette['accents']['red']),
            ('green', palette['accents']['green']),
            ('yellow', palette['accents']['yellow']),
            ('orange', palette['accents']['orange']),
            ('bg3', palette['ui']['selection']),
        ]
        
        all_ok = True
        for key, expected in checks:
            actual = colors.get(key, '')
            if not self.check_color('Helix', key, expected, actual):
                all_ok = False
        
        if all_ok:
            print("  ✅ Helix theme is consistent")
        else:
            print("  ❌ Helix theme has inconsistencies")
        
        return all_ok
    
    def validate_kitty(self) -> bool:
        """Validate Kitty theme against palette"""
        print("\n🔍 Validating Kitty theme...")
        kitty_file = ROOT / "kitty" / "guttenbergovitz.conf"
        
        with open(kitty_file) as f:
            content = f.read()
        
        palette = self.palette['dark']
        
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
            if not self.check_color('Kitty', key, expected, actual):
                all_ok = False
        
        if all_ok:
            print("  ✅ Kitty theme is consistent")
        else:
            print("  ❌ Kitty theme has inconsistencies")
        
        return all_ok
    
    def validate_all(self) -> bool:
        """Run all validations"""
        print("=" * 80)
        print("GUTTENBERGOVITZ THEME - CONSISTENCY VALIDATION")
        print("=" * 80)
        
        results = []
        results.append(self.validate_vscode())
        results.append(self.validate_neovim())
        results.append(self.validate_helix())
        results.append(self.validate_kitty())
        
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
