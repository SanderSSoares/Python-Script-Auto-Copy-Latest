#!/usr/bin/env python3
"""
auto_copy_latest.py
-----------------------------------
This script finds the most recently modified file in a source folder
and copies it to a target folder (such as a USB pen-drive).

Usage:
    python auto_copy_latest.py "C:/path/to/source" "E:/"

Example:
    python auto_copy_latest.py "C:/Users/Sander/Documents/Reports" "E:/Backup"
"""

import os
import sys
import shutil
from pathlib import Path

def copy_latest_file(source_folder: str, target_folder: str):
    # Convert to Path objects for easier handling
    src = Path(source_folder)
    dst = Path(target_folder)

    # Check if source exists
    if not src.exists() or not src.is_dir():
        print(f"Source folder does not exist: {src}")
        return

    # Check if target exists
    if not dst.exists() or not dst.is_dir():
        print(f"Target folder does not exist: {dst}")
        return

    # Find all files in the source folder
    files = [f for f in src.iterdir() if f.is_file()]
    if not files:
        print(f"No files found in source folder: {src}")
        return

    # Pick the most recently modified file
    latest_file = max(files, key=lambda f: f.stat().st_mtime)

    # Copy it to the target folder (keeping the same filename)
    destination_file = dst / latest_file.name
    shutil.copy2(latest_file, destination_file)  # copy2 keeps metadata

    print(f"Copied latest file: {latest_file.name}")
    print(f"From: {latest_file}")
    print(f"To:   {destination_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python auto_copy_latest.py <source_folder> <target_folder>")
        sys.exit(1)

    source = sys.argv[1]
    target = sys.argv[2]
    copy_latest_file(source, target)
