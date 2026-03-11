import re
s = input()
txt = re.search("cat|dog", s)
if txt: print("Yes")
else: print("No")