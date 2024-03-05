def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        print(f"Number of lines in '{filename}': {line_count}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.")


filename = input("Enter the path to the text file: ")
count_lines(filename)
