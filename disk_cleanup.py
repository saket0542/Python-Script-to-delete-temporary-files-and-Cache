import os, shutil

# More local Temp Files
More_Local_Temp = r"C:\Users\YourUserName\AppData\Local\Temp"

# Temp files
Temp_files = r"C:\Windows\Temp"

#Deleting files using prefetch
prefetch_folder=r"C:\Windows\Prefetch"
def clear_folder(folderpath):
    # get all the files and subdirectories within the folderpath
    Trash = os.listdir(folderpath)
    for item in Trash:
        item_path=os.path.join(folderpath,item)
        try:
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                print(f"{item_path} is not a file or directory")
        except Exception as e:
            print(f"Error deleting{item_path}:{e}")


if __name__ == "__main__":
    print(f'Cleaning {More_Local_Temp }')
    clear_folder(More_Local_Temp )

    print(f'Cleaning {Temp_files }')
    clear_folder(Temp_files )

    print(f'Cleaning {prefetch_folder}')
    clear_folder(prefetch_folder)
