import re
s = input()
start = re.match("Hello", s)
if start: print("Yes")
else: print("No")