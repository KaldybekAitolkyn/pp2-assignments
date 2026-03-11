import re
s = input()
p = input()
sub = re.search(p, s)
if sub: print("Yes")
else: print("No")