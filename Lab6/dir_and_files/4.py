import os

file_name = " "


if not os.path.exists(file_name):
    print(f"Error: File '{file_name}' not found.")
else:

    with open(file_name, 'r') as file:
        line_count = sum(1 for line in file)
    print(f"The file '{file_name}' contains {line_count} lines.")
