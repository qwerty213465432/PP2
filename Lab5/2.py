
import re


with open('row.txt', 'r',encoding="utf8") as file:
    content = file.read().strip()

pattern_2 = 'ab{2,3}'
matches_2 = re.findall(pattern_2, content)
print( matches_2)