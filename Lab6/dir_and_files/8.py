import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.F_OK):
            os.remove(path)
            print(f"The file at '{path}' has been successfully deleted.")
        else:
            print(f"Permission denied for file '{path}'.")
    else:
        print(f"The file '{path}' does not exist.")


path = " "
delete_file(path)
