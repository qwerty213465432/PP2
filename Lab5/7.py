import re


with open('row.txt', 'r',encoding="utf8") as file:
    content = file.read().strip()

camel_case_string = ''.join(word.capitalize() for word in content.split('_'))
print( camel_case_string)