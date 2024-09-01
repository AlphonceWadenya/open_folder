#! python3
# open_folder.py - Opens folders based on aliases.

# Usage: py.exe open_folder.py save <alias> <folder_path> - Saves folder path to alias.
#        py.exe open_folder.py <alias> - Opens folder based on alias.
#        py.exe open_folder.py list - Lists all saved aliases and their corresponding folder paths.

import shelve
import subprocess
import sys
# TODO: import pyperclip

foldersShelf = shelve.open('folders')

if len(sys.argv) >= 2 and sys.argv[1].lower() == 'save':
    if len(sys.argv) != 4:
        print("Usage: py.exe open_folder.py save <alias> <folder_path>")
        sys.exit(1)
    alias = sys.argv[2]
    folder_path = sys.argv[3]
    foldersShelf[alias] = folder_path
    print(f"Folder path saved with alias '{alias}'.")
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        folder_aliases = list(foldersShelf.keys())
        if folder_aliases:
            print("Saved folder aliases:")
            for alias in folder_aliases:
                print(alias)
        else:
            print("No saved folder aliases.")
    elif sys.argv[1] in foldersShelf:
        folder_path = foldersShelf[sys.argv[1]]
        try:
            subprocess.Popen(['explorer', folder_path])
        except Exception as e:
            print("An error occurred:", e)
    else:
        print("Alias not found.")

foldersShelf.close()
