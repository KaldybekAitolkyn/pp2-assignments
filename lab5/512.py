import re
s = input()
txt = re.findall("[0-9][0-9]+", s)
for i in txt:
    print(i, end=" ")