import re
s = input()
txt = re.findall("[A-Z]", s)
print(len(txt))