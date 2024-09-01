#! python3
# open_folder.py - Opens folders based on aliases.

# Usage: py.exe open_folder.py save <alias> <folder_path> - Saves folder path to alias.
#        py.exe open_folder.py <alias> - Opens folder based on alias.
#        py.exe open_folder.py list - Lists all saved aliases and their corresponding folder paths.

# NOTE: This script is not as discrete as running it from the "Win + R"

import shelve
import subprocess
import sys
import pyperclip

foldersShelf = shelve.open('folders')

# Save path from clipboard
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    if len(sys.argv) != 3:
        print("Usage: py.exe open_folder.py save <alias> <clip board content>")
        sys.exit(1)
    alias = sys.argv[2]
    folder_path = pyperclip.paste()
    foldersShelf[alias] = folder_path
    print(f"Folder path saved with alias '{alias}'.")

# List folder aliases or open saved path
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        folder_aliases = list(foldersShelf.keys())
        if folder_aliases:
            print("Saved folder aliases:")
            for alias in folder_aliases:
                print(alias)
        else:
            print("No saved folder aliases.")

# Open saved path            
    elif sys.argv[1] in foldersShelf:
        folder_path = foldersShelf[sys.argv[1]]
        try:
            subprocess.Popen(['explorer', folder_path])
        except Exception as e:
            print("An error occurred:", e)
    else:
        print("Alias not found.")

foldersShelf.close()
