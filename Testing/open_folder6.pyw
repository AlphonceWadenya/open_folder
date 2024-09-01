#! python3
# open_folder.py - Opens folders based on aliases.

# Usage: pyw.exe open_folder.pyw save <alias> <folder_path> - Saves folder path to alias.
#        pyw.exe open_folder.pyw <alias> - Opens folder based on alias.
#        pyw.exe open_folder.pyw list - Lists all saved aliases and their corresponding folder paths.

# NOTE: This script is discrete, it runs from pressing "Win + R"

import shelve
import subprocess
import sys
import pyperclip

foldersShelf = shelve.open('folders')

# Save path from clipboard
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    alias = sys.argv[2]
    folder_path = pyperclip.paste()
    foldersShelf[alias] = folder_path

# List folder aliases
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        folder_aliases = pyperclip.copy(str(list(foldersShelf.keys())))
        if not folder_aliases:
            sys.exit(1)

# Open saved path            
    elif sys.argv[1] in foldersShelf:
        folder_path = foldersShelf[sys.argv[1]]
        subprocess.Popen(['explorer', folder_path])

foldersShelf.close()
