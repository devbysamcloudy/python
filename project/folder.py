import os
from sys import exit


def get_useer_folder():
    folder_path = input("Enter folder path:")
    print(folder_path)
    isdir=os.path.isdir(folder_path)
    if not isdir:
        print("Enter a valid path")
        exit()
    return folder_path
