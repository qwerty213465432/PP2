import re


with open('row.txt', 'r',encoding="utf8") as file:
    content = file.read().strip()

modified_content_6 = re.sub(r'[ ,.]', ':', content)
print( modified_content_6)