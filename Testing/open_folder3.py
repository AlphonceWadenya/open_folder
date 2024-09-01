import subprocess
import shelve
import sys

def save_folder(alias, folder_path):
    with shelve.open('folders.db') as db:
        db[alias] = folder_path

def open_folder(alias):
    with shelve.open('folders.db') as db:
        if alias in db:
            folder_path = db[alias]
            subprocess.Popen(['explorer', folder_path])
        else:
            print(f"Alias '{alias}' not found.")

def list_folders():
    with shelve.open('folders.db') as db:
        print("Saved folders:")
        for alias in db:
            print(f"{alias}: {db[alias]}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python open_folder.py save <alias> <folder_path>")
        print("  python open_folder.py open <alias>")
        print("  python open_folder.py list")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "save":
        if len(sys.argv) != 4:
            print("Usage: python open_folder.py save <alias> <folder_path>")
            sys.exit(1)
        alias = sys.argv[2]
        folder_path = sys.argv[3]
        save_folder(alias, folder_path)
        print(f"Folder saved with alias '{alias}'.")
    elif command == "open":
        if len(sys.argv) != 3:
            print("Usage: python open_folder.py open <alias>")
            sys.exit(1)
        alias = sys.argv[2]
        open_folder(alias)
    elif command == "list":
        list_folders()
    else:
        print("Invalid command.")
