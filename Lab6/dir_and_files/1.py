import os

def dirfile(Ppath):
    
    print("Directories:")
    for item in os.listdir(Ppath):
        if os.path.isdir(os.path.join(Ppath, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(Ppath):
        if os.path.isfile(os.path.join(Ppath, item)):
            print(item)

    print("\nAll items:")
    for item in os.listdir(Ppath):
        print(item)

path = input()
dirfile(path)
