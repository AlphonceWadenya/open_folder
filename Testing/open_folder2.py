import subprocess
import sys

# Define your folder paths here
folders = {
    "work": r"C:\Path\to\Your\Work\Folder",
    "personalDocs": r"C:\Path\to\Your\Personal\Documents\Folder",
    # Add more folder paths as needed
}

def open_folder(folder_path):
    try:
        subprocess.Popen(['explorer', folder_path])
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python open_folder.py <folder_name>")
        sys.exit(1)
    
    folder_name = sys.argv[1]
    
    if folder_name in folders:
        folder_to_open = folders[folder_name]
        open_folder(folder_to_open)
    else:
        print("Folder not found.")
