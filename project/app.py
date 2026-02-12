import os

from fileFolder import listFolder
from file_sys import move_files
from folder import get_useer_folder

IMAGES = [".jpg", ".jpeg", ".png"]
MUSIC = [".mp3", ".wav"]
PDF = [".pdf"]
ZIP = [".tar", ".zip", ".rar"]

def main():
    print("welcome to the app")
    print("________________")

    working_folder = get_useer_folder()
    items = listFolder(working_folder)

    for item in items:
        print("single item is", item)

        split_item = os.path.splitext(item)
        print("split item is", split_item)
        print("first element", split_item[0])
        print("second element", split_item[1])

        extension = split_item[1].lower()

        if extension in IMAGES:
            print(f"for file {item} its an Image")
            folder_name = "Images"

        elif extension in MUSIC:
            print(f"for file {item} its a music")
            folder_name = "Music"

        elif extension in PDF:
            print(f"for file {item} its a PDF")
            folder_name = "PDFs"

        elif extension in ZIP:
            print(f"for file {item} its a Zip")
            folder_name = "Zips"

        else:
            print(f"for file {item} its unknown")
            folder_name = "Others"

        print("The folder is", folder_name)

        move_files(
            filename=item,
            working_dir=working_folder,
            folder_name=folder_name
        )

main()
