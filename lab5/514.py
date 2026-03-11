import re
s = input()
txt = re.compile(r"^\d+$")
if txt.match(s):
    print("Match")
else:
    print("No match")