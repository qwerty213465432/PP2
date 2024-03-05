import os

def pathis(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

    print(f"Checking access for path: {path}")

    if os.access(path, os.R_OK):
        print("Readable: Yes")
    else:
        print("Readable: No")

    if os.access(path, os.W_OK):
        print("Writable: Yes")
    else:
        print("Writable: No")

    if os.access(path, os.X_OK):
        print("Executable: Yes")
    else:
        print("Executable: No")


path = input()
pathis(path)
