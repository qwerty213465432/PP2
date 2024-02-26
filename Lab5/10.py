import re


with open('row.txt', 'r',encoding="utf8") as file:
    content = file.read().strip()


snake_case_string = ''.join('_' + char.lower() if char.isupper() else char for char in content).lstrip('_')
print( snake_case_string)