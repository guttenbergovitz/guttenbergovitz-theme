#!/usr/bin/env python3
import json
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

FILES = [
    ROOT / "vscode/themes/guttenbergovitz-color-theme.json",
    ROOT / "vscode/themes/guttenbergovitz-light-color-theme.json",
    ROOT / "ghostty/guttenbergovitz",
    ROOT / "warp/guttenbergovitz.yaml",
    ROOT / "zellij/guttenbergovitz.kdl",
    ROOT / "helix/guttenbergovitz.toml",
    ROOT / "kitty/guttenbergovitz.conf",
    ROOT / "lua/guttenbergovitz/init.lua",
    ROOT / "zed/guttenbergovitz.json",
]

HEX_RE = re.compile(r"#[0-9a-fA-F]{6}")

def load_palette():
    text = (ROOT / "palette.json").read_text()
    allowed = set()
    for m in HEX_RE.finditer(text):
        allowed.add(m.group(0).lower())
    return allowed

def scan_file(path: Path, allowed: set[str]):
    text = path.read_text(errors="ignore")
    bad = []
    for m in HEX_RE.finditer(text):
        color = m.group(0).lower()
        if color not in allowed:
            bad.append(color)
    return sorted(set(bad))

def main():
    allowed = load_palette()
    any_errors = False
    for f in FILES:
        if not f.exists():
            continue
        bad = scan_file(f, allowed)
        if bad:
            any_errors = True
            rel = f.relative_to(ROOT)
            print(f"[palette-check] {rel}: unknown colors: {', '.join(bad)}")
    if any_errors:
        print("[palette-check] FAILED: found colors outside the allowed palette")
        sys.exit(1)
    else:
        print("[palette-check] OK: all files use allowed colors")

if __name__ == "__main__":
    main()
