# Change File Names CLI

A Python command-line tool that copies files from subfolders into a single folder and renames them based on folder name and disc rules.

---

## Features

- Handles multiple files per folder
- Conditional "Disc 1 / Disc 2" naming when a folder contains multiple files
- Single-file folders keep the original folder name
- Optional extension conversion
- Dry-run mode to preview actions without making changes
- Prevents overwriting existing files

---

## Requirements

- Python 3.7 or higher
- Works on Windows, macOS, and Linux

---

## Usage

### Basic command

```bash
py ChangeFileNames.py --source "C:\Test Folder" --dest "C:\Output Folder"