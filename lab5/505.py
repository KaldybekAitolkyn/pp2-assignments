import re
s = input()
check = re.search("^[a-zA-Z].*\d$", s)
if check: print("Yes")
else: print("No")