import re


with open('row.txt', 'r',encoding="utf8") as file:
    content = file.read().strip()

pattern_3 = r'[a-z]+_[a-z]+'
matches_3 = re.findall(pattern_3, content)
print( matches_3)
