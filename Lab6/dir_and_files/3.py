import os

def pathis(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"The path '{path}' does not exist.")


path = input("Enter the path to analyze: ")
pathis(path)
