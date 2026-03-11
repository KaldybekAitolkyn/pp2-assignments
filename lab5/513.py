import re
s = input()
txt = re.findall(r"\b\w+\b", s)
print(len(txt))