from folder import get_useer_folder
from file_sys import list_folder_files, move_files
import os

#Android->Kotlin,Java,Js(react native)
#Android 16
#from android 8>above
#use all caps to create a constant
#some delete folder files. chmod→#
#windows
IMAGE = ["jpg", "jpeg", "png"]
MUSIC = ["mp3", "wav"]
PDF = ["pdf"]
ZIP = ["tar", "zip", "rar"]

#have settings prompted for each delete or not

def main():
    print("Welcome to folder organisation app")
    print(" ")
    working_folder = get_useer_folder()
    items = list_folder_files(working_folder)
    prompt_input = input("For each file prompt before move. y or n: ").lower()

    if prompt_input == 'y':
        prompt = True
    else:
        prompt = False

    for item in items:
        if os.path.isdir(os.path.join(working_folder, item)):
            print(f"Skipping directory: {item}")
            continue

        split_item = os.path.splitext(item)
        extension = split_item[1].lower()

        folder_name = "Other"

        if extension in IMAGE:
            folder_name = "Image"
        elif extension in MUSIC:
            folder_name = "Music"
        elif extension in PDF:
            folder_name = "Pdf"
        elif extension in ZIP:
            folder_name = "Zip"
        else:
            folder_name = "Other"

        move_files(
            filename=item,
            working_dir=working_folder,
            folder_name=folder_name,
            prompt=prompt
        )

main()