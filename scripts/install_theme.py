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
        "files": [(ROOT / "helix" / "guttenbergovitz.toml", "guttenbergovitz.toml")],
        "instructions": "Add `theme = \"guttenbergovitz\"` to your ~/.config/helix/config.toml"
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
        "files": [(ROOT / "ghostty" / "guttenbergovitz", "guttenbergovitz")],
        "instructions": "Add `theme = guttenbergovitz` to your ~/.config/ghostty/config"
    },
    "4": {
        "name": "Kitty",
        "dest_dir": Path("~/.config/kitty/themes").expanduser(),
        "files": [(ROOT / "kitty" / "guttenbergovitz.conf", "guttenbergovitz.conf")],
        "instructions": "Add `include themes/guttenbergovitz.conf` to your ~/.config/kitty/kitty.conf"
    },
    "5": {
        "name": "Zellij",
        "dest_dir": Path("~/.config/zellij/themes").expanduser(),
        "files": [(ROOT / "zellij" / "guttenbergovitz.kdl", "guttenbergovitz.kdl")],
        "instructions": "Add `theme \"guttenbergovitz\"` to your ~/.config/zellij/config.kdl"
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

def install_platform(key):
    platform = PLATFORMS[key]
    name = platform["name"]
    dest_dir = platform["dest_dir"]
    files = platform["files"]
    
    print(f"\n{BOLD}{CYAN}Installing theme for: {name}...{RESET}")
    
    try:
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
