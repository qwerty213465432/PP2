import re


with open('row.txt', 'r',encoding="utf8") as file:
    content = file.read().strip()

parts = re.findall('[A-Z][^A-Z]*', content)
print( parts)
