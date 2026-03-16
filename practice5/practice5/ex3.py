import re

s = input()
if re.fullmatch(r"[a-z]+_[a-z]+", s):
    print("Match")
else:
    print("No match")
