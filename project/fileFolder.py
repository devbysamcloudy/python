import os

def listFolder(folder_path):
    files = os.listdir(folder_path)
    print(files)
    return files
