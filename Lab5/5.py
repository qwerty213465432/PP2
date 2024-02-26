import re


with open('row.txt', 'r',encoding="utf8") as file:
    content = file.read().strip()

pattern_5 = 'a.*b$'
matches_5 = re.findall(pattern_5, content)
print(matches_5)