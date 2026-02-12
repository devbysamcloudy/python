from fileFolder import listFolder
from folder import get_useer_folder
import  os


IMAGES = [".jpg", ".jpeg", ".png"]
MUSIC = ["mp3", "wav"]
PDF = ["pdf"]
ZIP = ["tar", "zip", "rar"]
def main ():
    print ("welcome to the app")
    print("________________")
    working_folder = get_useer_folder()
    items = listFolder(working_folder)

    for items in items:
        print("single item is " , items)
        split_item = os.path.splitext(items)
        print("split item is", split_item)
        print("first element",split_item[0])
        print("second element", [1])
        extension = split_item[1]
        if extension in IMAGES:
            print(f"for file{items} its an Image")
        elif extension in MUSIC:
            print(f"for file {items} its a music")
        elif extension in PDF:
            print(f"for file {items} its a PDF")
        else:
            print(f"for a file{items} its an unknown")



main ()
