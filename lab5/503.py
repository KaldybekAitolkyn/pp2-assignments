import re
s = input()
p = input()
lst = re.findall(p, s)
print(len(lst))