import re


with open('row.txt', 'r',encoding="utf8") as file:
    content = file.read().strip()


pattern_4 = r'[A-Z][a-z]+'
matches_4 = re.findall(pattern_4, content)
print( matches_4)