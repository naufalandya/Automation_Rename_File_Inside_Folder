import os
import re

def rename_files(folder_path, search_str, replace_str):
    if not os.path.isdir(folder_path):
        print(f"{folder_path} bukan direktori.")
        return

    files = os.listdir(folder_path)

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            new_file_name = re.sub(search_str, replace_str, file_name)
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(file_path, new_file_path)
            print(f"{file_name} lu ubah jadi {new_file_name}")

folder_path = "Python"
search_str = "repaired"
replace_str = ""

rename_files(folder_path, search_str, replace_str)
