import os
import shutil
from os.path import isdir


def list_folder_files(folder_path):
    files= os.listdir(folder_path)
    return files

def move_files(working_dir, filename, folder_name):
    move_path= os.path.join(working_dir,folder_name)
    source = os.path.join(working_dir,folder_name)
    print("Moving the file to",move_path)

    isdir=os.path.isdir(move_path)

    if not isdir:
        os.makedirs(move_path)

    shutil.move(src=source,dst=move_path)

