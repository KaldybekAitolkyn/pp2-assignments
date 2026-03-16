import re

s = input()
if re.fullmatch(r"[A-Z][a-z]+", s):
    print("Match")
else:
    print("No match")

