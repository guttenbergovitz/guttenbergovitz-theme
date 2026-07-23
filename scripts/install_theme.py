#!/usr/bin/env python3
import os
import shutil
import sys
from pathlib import Path

# ANSI colors for beautiful terminal output
BOLD = "\033[1m"
GREEN = "\033[32m"
BLUE = "\033[34m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"
RESET = "\033[0m"

BANNER = f"""{BOLD}{YELLOW}
  ╔══════════════════════════════════════════════════════╗
  ║                GUTTENBERGOVITZ THEME                 ║
  ║                   CLI Installer                      ║
  ╚══════════════════════════════════════════════════════╝{RESET}"""

ROOT = Path(__file__).resolve().parents[1]

# Registry of supported platforms
PLATFORMS = {
    "1": {
        "name": "Helix",
        "dest_dir": Path("~/.config/helix/themes").expanduser(),
        "files": [
            (ROOT / "helix" / "guttenbergovitz.toml", "guttenbergovitz.toml"),
            (ROOT / "helix" / "guttenbergovitz-light.toml", "guttenbergovitz-light.toml")
        ],
        "instructions": "Add `theme = \"guttenbergovitz\"` (or `theme = \"guttenbergovitz-light\"`) to your ~/.config/helix/config.toml"
    },
    "2": {
        "name": "Zed",
        "dest_dir": Path("~/.config/zed/themes").expanduser(),
        "files": [(ROOT / "zed" / "guttenbergovitz.json", "guttenbergovitz.json")],
        "instructions": "Open Zed, switch themes (`cmd+k cmd+t`) and select \"Guttenbergovitz\""
    },
    "3": {
        "name": "Ghostty",
        "dest_dir": Path("~/.config/ghostty/themes").expanduser(),
        "files": [
            (ROOT / "ghostty" / "guttenbergovitz", "guttenbergovitz"),
            (ROOT / "ghostty" / "guttenbergovitz-light", "guttenbergovitz-light")
        ],
        "instructions": "Add `theme = guttenbergovitz` (or `theme = guttenbergovitz-light`) to your ~/.config/ghostty/config"
    },
    "4": {
        "name": "Kitty",
        "dest_dir": Path("~/.config/kitty/themes").expanduser(),
        "files": [
            (ROOT / "kitty" / "guttenbergovitz.conf", "guttenbergovitz.conf"),
            (ROOT / "kitty" / "guttenbergovitz-light.conf", "guttenbergovitz-light.conf")
        ],
        "instructions": "Add `include themes/guttenbergovitz.conf` (or `themes/guttenbergovitz-light.conf`) to your ~/.config/kitty/kitty.conf"
    },
    "5": {
        "name": "Zellij",
        "dest_dir": Path("~/.config/zellij/themes").expanduser(),
        "files": [
            (ROOT / "zellij" / "guttenbergovitz.kdl", "guttenbergovitz.kdl"),
            (ROOT / "zellij" / "guttenbergovitz-light.kdl", "guttenbergovitz-light.kdl")
        ],
        "instructions": "Add `theme \"guttenbergovitz\"` (or `theme \"guttenbergovitz-light\"`) to your ~/.config/zellij/config.kdl"
    },
    "6": {
        "name": "Vim",
        "dest_dir": Path("~/.vim/colors").expanduser(),
        "files": [(ROOT / "vim" / "colors" / "guttenbergovitz.vim", "guttenbergovitz.vim")],
        "instructions": "Open Vim and run `:colorscheme guttenbergovitz` (or add to your ~/.vimrc)"
    },
    "7": {
        "name": "Neovim",
        "dest_dir": Path("~/.config/nvim").expanduser(),
        "files": [
            (ROOT / "colors" / "guttenbergovitz.lua", "colors/guttenbergovitz.lua"),
            (ROOT / "colors" / "guttenbergovitz-light.lua", "colors/guttenbergovitz-light.lua"),
            (ROOT / "lua" / "guttenbergovitz" / "init.lua", "lua/guttenbergovitz/init.lua")
        ],
        "instructions": "Open Neovim and run `:colorscheme guttenbergovitz` (or `:colorscheme guttenbergovitz-light`)\nTo enable italicized comments: `vim.g.guttenbergovitz_italics = true`"
    },
    "8": {
        "name": "VS Code",
        "dest_dir": Path("~/.vscode/extensions/guttenbergovitz").expanduser(),
        "files": [
            (ROOT / "vscode" / "package.json", "package.json"),
            (ROOT / "vscode" / "README.md", "README.md"),
            (ROOT / "vscode" / "assets" / "icon.png", "assets/icon.png"),
            (ROOT / "vscode" / "themes" / "guttenbergovitz-color-theme.json", "themes/guttenbergovitz-color-theme.json"),
            (ROOT / "vscode" / "themes" / "guttenbergovitz-light-color-theme.json", "themes/guttenbergovitz-light-color-theme.json")
        ],
        "instructions": "Restart VS Code, then switch themes (`cmd+k cmd+t`) and select \"Guttenbergovitz\" or \"Guttenbergovitz Light\""
    },
    "9": {
        "name": "Kiro",
        "dest_dir": Path("~/.kiro/extensions/guttenbergovitz").expanduser(),
        "files": [
            (ROOT / "vscode" / "package.json", "package.json"),
            (ROOT / "vscode" / "README.md", "README.md"),
            (ROOT / "vscode" / "assets" / "icon.png", "assets/icon.png"),
            (ROOT / "vscode" / "themes" / "guttenbergovitz-color-theme.json", "themes/guttenbergovitz-color-theme.json"),
            (ROOT / "vscode" / "themes" / "guttenbergovitz-light-color-theme.json", "themes/guttenbergovitz-light-color-theme.json")
        ],
        "instructions": "Restart Kiro, then switch themes (`cmd+k cmd+t`) and select \"Guttenbergovitz\" or \"Guttenbergovitz Light\""
    },
    "10": {
        "name": "Cursor",
        "dest_dir": Path("~/.cursor/extensions/guttenbergovitz").expanduser(),
        "files": [
            (ROOT / "vscode" / "package.json", "package.json"),
            (ROOT / "vscode" / "README.md", "README.md"),
            (ROOT / "vscode" / "assets" / "icon.png", "assets/icon.png"),
            (ROOT / "vscode" / "themes" / "guttenbergovitz-color-theme.json", "themes/guttenbergovitz-color-theme.json"),
            (ROOT / "vscode" / "themes" / "guttenbergovitz-light-color-theme.json", "themes/guttenbergovitz-light-color-theme.json")
        ],
        "instructions": "Restart Cursor, then switch themes (`cmd+k cmd+t`) and select \"Guttenbergovitz\" or \"Guttenbergovitz Light\""
    },
    "11": {
        "name": "Warp",
        "dest_dir": Path("~/.warp/themes").expanduser(),
        "files": [
            (ROOT / "warp" / "guttenbergovitz.yaml", "guttenbergovitz.yaml"),
            (ROOT / "warp" / "guttenbergovitz-light.yaml", "guttenbergovitz-light.yaml")
        ],
        "instructions": "Open Warp, navigate to Settings → Appearance → Theme, and select \"Guttenbergovitz\" or \"Guttenbergovitz Light\""
    },
    "12": {
        "name": "JetBrains",
        "dest_dir": None,
        "files": [
            (ROOT / "jetbrains" / "Guttenbergovitz.icls", "Guttenbergovitz.icls"),
            (ROOT / "jetbrains" / "Guttenbergovitz-Light.icls", "Guttenbergovitz-Light.icls")
        ],
        "instructions": "Restart your IDE, navigate to Settings → Editor → Color Scheme, and select \"Guttenbergovitz\" or \"Guttenbergovitz Light\"\nTo build/install the UI Theme plugin, run: make zip.jetbrains-ui"
    },
    "13": {
        "name": "OpenCode",
        "dest_dir": Path("~/.config/opencode/themes").expanduser(),
        "files": [
            (ROOT / "opencode" / "guttenbergovitz.json", "guttenbergovitz.json")
        ],
        "instructions": "Open OpenCode, then switch themes and select \"Guttenbergovitz\""
    }
}

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_success(message):
    print(f"{GREEN}✔ {message}{RESET}")

def print_info(message):
    print(f"{BLUE}ℹ {message}{RESET}")

def print_warning(message):
    print(f"{YELLOW}⚠ {message}{RESET}")

def print_error(message):
    print(f"{RED}✘ {message}{RESET}")

def find_jetbrains_dirs():
    """Scan standard locations for installed JetBrains IDE configuration folders."""
    jb_base = Path("~/Library/Application Support/JetBrains").expanduser()
    if not jb_base.exists():
        return []
    
    dirs = []
    for p in jb_base.iterdir():
        if p.is_dir() and not p.name.startswith('.'):
            dirs.append(p)
    return dirs

def install_platform(key):
    platform = PLATFORMS[key]
    name = platform["name"]
    dest_dir = platform["dest_dir"]
    files = platform["files"]
    
    print(f"\n{BOLD}{CYAN}Installing theme for: {name}...{RESET}")
    
    try:
        if name == "JetBrains":
            jb_dirs = find_jetbrains_dirs()
            if not jb_dirs:
                print_warning("No active JetBrains IDE configuration directories found under ~/Library/Application Support/JetBrains/")
                print_info("Please import the scheme manually inside your IDE using File -> Settings -> Editor -> Color Scheme -> Import Scheme.")
                return
                
            for jb_dir in jb_dirs:
                colors_dir = jb_dir / "colors"
                colors_dir.mkdir(parents=True, exist_ok=True)
                for src, rel_dest in files:
                    dest = colors_dir / rel_dest
                    shutil.copy2(src, dest)
                    print_success(f"Copied to {jb_dir.name}: {src.name} -> {dest}")
                    
            print_success(f"{name}: Installed successfully on {len(jb_dirs)} IDE directories!")
            print(f"{BOLD}Activation:{RESET} {platform['instructions']}")
            return

        # Check and create directory if needed
        if not dest_dir.exists():
            dest_dir.mkdir(parents=True, exist_ok=True)
            print_info(f"Created directory: {dest_dir}")
            
        for src, rel_dest in files:
            dest = dest_dir / rel_dest
            
            # Ensure nested subdirectories are created (for Neovim colors/ and lua/)
            dest.parent.mkdir(parents=True, exist_ok=True)
            
            shutil.copy2(src, dest)
            print_success(f"Copied: {src.name} -> {dest}")
            
        print_success(f"{name}: Installed successfully!")
        print(f"{BOLD}Activation:{RESET} {platform['instructions']}")
    except Exception as e:
        print_error(f"Error during installation of {name}: {e}")

def main():
    clear_screen()
    print(BANNER)
    
    # If platform arguments are passed via command line
    if len(sys.argv) > 1:
        targets = sys.argv[1:]
        # Map target names to registry keys
        name_to_key = {p["name"].lower(): k for k, p in PLATFORMS.items()}
        
        for target in targets:
            key = name_to_key.get(target.lower())
            if key:
                install_platform(key)
            else:
                print_error(f"Unknown platform: {target}")
                print(f"Available platforms: {', '.join(p['name'] for p in PLATFORMS.values())}")
        return

    # Interactive mode
    while True:
        print(f"\nSelect editors/terminals to install the theme for:")
        for key, p in PLATFORMS.items():
            print(f"  {BOLD}{key}{RESET}. {p['name']} ({p['dest_dir']})")
        print(f"  {BOLD}A{RESET}. Install for all")
        print(f"  {BOLD}Q{RESET}. Quit")
        
        choice = input(f"\nEnter numbers (e.g. 1 3 4), 'A' or 'Q': ").strip().upper()
        
        if choice == 'Q':
            print("Installation aborted.")
            break
        elif choice == 'A':
            for key in sorted(PLATFORMS.keys()):
                install_platform(key)
            break
        elif choice:
            keys = choice.split()
            valid_keys = [k for k in keys if k in PLATFORMS]
            if not valid_keys:
                print_error("Invalid choice. Please try again.")
                continue
            for key in valid_keys:
                install_platform(key)
            break

if __name__ == "__main__":
    main()
