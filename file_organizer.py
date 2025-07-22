import os
import shutil

def organize_files_by_extension(folder_path):
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            ext = file_name.split('.')[-1]
            target_folder = os.path.join(folder_path, ext)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(os.path.join(folder_path, file_name), os.path.join(target_folder, file_name))

if __name__ == "__main__":
    organize_files_by_extension(".")