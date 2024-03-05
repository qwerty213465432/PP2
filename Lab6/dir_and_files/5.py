def listtofile(filename, input_list):
    with open(filename, 'w') as file:
        for item in input_list:
            file.write(str(item) + '\n')


filename = input("Enter the filename to write the list: ")
my_list = input("Enter the list (separate elements with spaces): ").split()
listtofile(filename, my_list)
