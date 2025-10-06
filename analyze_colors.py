#!/usr/bin/env python3
"""
Analyze color consistency across Guttenbergovitz theme implementations.
Base reference: VSCode theme
"""

import json
import re
from pathlib import Path
from collections import defaultdict

# VSCode theme as reference
VSC_COLORS = {
    'bg': '#232326',
    'bg_dark': '#1d1d20',
    'bg_light': '#2a2a2d',
    'fg': '#d4be98',
    'fg_dim': '#7c7c7c',
    'selection': '#3a3a3d',
    'border': '#3a3a3d',
    
    # Accents
    'red': '#a96b69',
    'green': '#89a87d',
    'yellow': '#d6b986',
    'orange': '#d79969',
    
    # Terminal ANSI
    'terminal_black': '#1d1d20',
    'terminal_bright_black': '#7c7c7c',
    'terminal_red': '#a96b69',
    'terminal_bright_red': '#a96b69',
    'terminal_green': '#89a87d',
    'terminal_bright_green': '#89a87d',
    'terminal_yellow': '#d6b986',
    'terminal_bright_yellow': '#d6b986',
    'terminal_blue': '#d79969',
    'terminal_bright_blue': '#d79969',
    'terminal_magenta': '#a96b69',
    'terminal_bright_magenta': '#a96b69',
    'terminal_cyan': '#89a87d',
    'terminal_bright_cyan': '#89a87d',
    'terminal_white': '#d4be98',
    'terminal_bright_white': '#d4be98',
}

def extract_neovim_colors():
    """Extract colors from Neovim theme"""
    colors = {}
    with open('lua/guttenbergovitz/init.lua', 'r') as f:
        content = f.read()
        # Find dark theme colors
        dark_section = re.search(r'} or \{(.*?)-- Terminal', content, re.DOTALL)
        if dark_section:
            matches = re.findall(r'(\w+)\s*=\s*"(#[0-9a-fA-F]{6})"', dark_section.group(1))
            for name, color in matches:
                colors[name] = color.lower()
    return colors

def extract_helix_colors():
    """Extract colors from Helix theme"""
    colors = {}
    with open('helix/guttenbergovitz.toml', 'r') as f:
        content = f.read()
        # Find palette section
        palette_section = re.search(r'\[palette\](.*)', content, re.DOTALL)
        if palette_section:
            matches = re.findall(r'(\w+)\s*=\s*"(#[0-9a-fA-F]{6})"', palette_section.group(1))
            for name, color in matches:
                colors[name] = color.lower()
    return colors

def extract_kitty_colors():
    """Extract colors from Kitty theme"""
    colors = {}
    with open('kitty/guttenbergovitz.conf', 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                match = re.match(r'(\w+)\s+(#[0-9a-fA-F]{6})', line)
                if match:
                    colors[match.group(1)] = match.group(2).lower()
                # Handle palette colors
                match = re.match(r'color(\d+)\s+(#[0-9a-fA-F]{6})', line)
                if match:
                    colors[f'color{match.group(1)}'] = match.group(2).lower()
    return colors

def extract_warp_colors():
    """Extract colors from Warp theme"""
    colors = {}
    with open('warp/guttenbergovitz.yaml', 'r') as f:
        content = f.read()
        # Extract basic colors
        for key in ['background', 'foreground', 'cursor', 'accent']:
            match = re.search(rf'{key}:\s*"(#[0-9a-fA-F]{{6}})"', content)
            if match:
                colors[key] = match.group(1).lower()
        # Extract terminal colors
        terminal_section = re.search(r'terminal_colors:(.*)', content, re.DOTALL)
        if terminal_section:
            matches = re.findall(r'(\w+):\s*"(#[0-9a-fA-F]{6})"', terminal_section.group(1))
            for name, color in matches:
                colors[f'terminal_{name}'] = color.lower()
    return colors

def extract_ghostty_colors():
    """Extract colors from Ghostty theme"""
    colors = {}
    with open('ghostty/guttenbergovitz', 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                # Handle basic colors
                match = re.match(r'(\w+)\s*=\s*([0-9a-fA-F]{6})', line)
                if match:
                    colors[match.group(1)] = f'#{match.group(2).lower()}'
                # Handle palette colors
                match = re.match(r'palette\s*=\s*(\d+)=#([0-9a-fA-F]{6})', line)
                if match:
                    colors[f'palette_{match.group(1)}'] = f'#{match.group(2).lower()}'
    return colors

def extract_zed_colors():
    """Extract colors from Zed theme"""
    with open('zed/guttenbergovitz.json', 'r') as f:
        data = json.load(f)
        theme = data['themes'][0]['style']
        colors = {}
        # Flatten the structure
        for key, value in theme.items():
            if isinstance(value, str) and value.startswith('#'):
                colors[key] = value.lower()
            elif key == 'syntax':
                for syntax_key, syntax_val in value.items():
                    if isinstance(syntax_val, dict) and 'color' in syntax_val:
                        colors[f'syntax_{syntax_key}'] = syntax_val['color'].lower()
        return colors

def extract_vim_colors():
    """Extract colors from Vim theme"""
    colors = {}
    with open('vim/colors/guttenbergovitz.vim', 'r') as f:
        content = f.read()
        # Find color palette
        palette_section = re.search(r"let s:colors = \{(.*?)\}", content, re.DOTALL)
        if palette_section:
            matches = re.findall(r"'(\w+)':\s*'(#[0-9a-fA-F]{6})'", palette_section.group(1))
            for name, color in matches:
                colors[name] = color.lower()
    return colors

def compare_colors(implementations):
    """Compare colors across implementations"""
    print("\n" + "="*80)
    print("GUTTENBERGOVITZ THEME - COLOR CONSISTENCY ANALYSIS")
    print("Reference: VSCode theme")
    print("="*80)
    
    # Map common color names
    color_mappings = {
        'bg': ['bg', 'bg0', 'background', 'editor.background'],
        'bg_dark': ['bg_dark', 'bg1'],
        'bg_light': ['bg_light', 'bg2'],
        'fg': ['fg', 'fg0', 'foreground'],
        'fg_dim': ['fg_dim', 'fg4', 'gray', 'comment'],
        'selection': ['selection', 'bg3'],
        'red': ['red'],
        'green': ['green'],
        'yellow': ['yellow'],
        'orange': ['orange', 'blue'],  # Note: Helix uses 'blue' for orange
    }
    
    issues = []
    
    for vsc_name, expected_color in VSC_COLORS.items():
        if vsc_name.startswith('terminal_'):
            continue  # Skip terminal colors for now
            
        print(f"\n{vsc_name.upper()}: {expected_color}")
        print("-" * 80)
        
        # Find mapped names
        mapped_names = color_mappings.get(vsc_name, [vsc_name])
        
        for impl_name, impl_colors in implementations.items():
            found = False
            for mapped in mapped_names:
                if mapped in impl_colors:
                    color = impl_colors[mapped]
                    status = "✓" if color == expected_color else "✗"
                    print(f"  {impl_name:15} {mapped:20} {color:10} {status}")
                    if color != expected_color:
                        issues.append({
                            'implementation': impl_name,
                            'color_name': vsc_name,
                            'mapped_name': mapped,
                            'expected': expected_color,
                            'actual': color
                        })
                    found = True
                    break
            if not found:
                print(f"  {impl_name:15} {'MISSING':20} {'-':10} ✗")
                issues.append({
                    'implementation': impl_name,
                    'color_name': vsc_name,
                    'mapped_name': 'MISSING',
                    'expected': expected_color,
                    'actual': None
                })
    
    return issues

def main():
    implementations = {
        'Neovim': extract_neovim_colors(),
        'Helix': extract_helix_colors(),
        'Kitty': extract_kitty_colors(),
        'Warp': extract_warp_colors(),
        'Ghostty': extract_ghostty_colors(),
        'Zed': extract_zed_colors(),
        'Vim': extract_vim_colors(),
    }
    
    issues = compare_colors(implementations)
    
    print("\n" + "="*80)
    print(f"SUMMARY: Found {len(issues)} inconsistencies")
    print("="*80)
    
    # Group issues by implementation
    by_impl = defaultdict(list)
    for issue in issues:
        by_impl[issue['implementation']].append(issue)
    
    for impl, impl_issues in sorted(by_impl.items()):
        print(f"\n{impl}: {len(impl_issues)} issues")
        for issue in impl_issues:
            if issue['actual'] is None:
                print(f"  - Missing: {issue['color_name']}")
            else:
                print(f"  - {issue['color_name']}: {issue['actual']} → {issue['expected']}")

if __name__ == '__main__':
    main()
