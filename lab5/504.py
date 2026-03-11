import re
s = input()
digits = re.findall("\\d", s)
for i in digits:
    print(i, end=" ")