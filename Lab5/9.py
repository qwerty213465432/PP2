import re


with open('row.txt', 'r',encoding="utf8") as file:
    content = file.read().strip()

modified_content_9 = re.sub(r'(?<!^)(?=[A-Z])', ' ', content)
print( modified_content_9)