import zipfile
import os
from datetime import datetime

def backup_folder(folder_path):
    zip_filename = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    with zipfile.ZipFile(zip_filename, 'w') as backup_zip:
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                backup_zip.write(file_path, os.path.relpath(file_path, folder_path))
    print(f"Backup created: {zip_filename}")

if __name__ == "__main__":
    backup_folder(".")