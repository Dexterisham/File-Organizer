import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organize_files(folder_path):
    # Define file type categories and their corresponding folders
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
        'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.sh', '.bat', '.ps1'],
        'Others': []
    }

    # Create folders for each category if they don't exist
    for folder in file_types.keys():
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

    # Organize files
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(folder_path, folder, file))
                    moved = True
                    break
            if not moved and file_ext:
                shutil.move(file_path, os.path.join(folder_path, 'Others', file))

def browse_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    folder_path = filedialog.askdirectory(title="Select Folder to Organize")
    return folder_path

if __name__ == "__main__":
    print("Select the folder you want to organize.")
    folder_path = browse_folder()
    if folder_path:  # Proceed only if a folder is selected
        organize_files(folder_path)
        print(f"Files in {folder_path} organized successfully!")
    else:
        print("No folder selected. Exiting.")
