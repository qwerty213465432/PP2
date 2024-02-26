import re


with open('row.txt', 'r',encoding="utf8") as file:
    content = file.read().strip()


pattern_1 = 'ab*'
matches_1 = re.findall(pattern_1, content)
print(matches_1)