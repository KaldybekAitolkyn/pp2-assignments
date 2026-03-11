import re
s = input()
txt = re.findall(r"\b[a-zA-Z]{3}\b", s)
print(len(txt))