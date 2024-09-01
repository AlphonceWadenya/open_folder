import subprocess

def open_folder(folder_path):
    try:
        subprocess.Popen(['explorer', folder_path])
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    folder_to_open = r"C:\Users\Alphonce Wadenya\Documents\important_stuff\Work\2023\Q3\RFH"  # Replace with the actual folder path
    open_folder(folder_to_open)
