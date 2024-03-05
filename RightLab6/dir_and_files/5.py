def listtofile(filename, input_list):
    with open(filename, 'w') as file:
        for item in input_list:
            file.write(str(item) + '\n')


filename = " "
my_list = " ".split()
listtofile(filename, my_list)
