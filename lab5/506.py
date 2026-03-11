import re
s = input()
adress = re.search(r"[a-zA-Z0-9._-]+@\w+\.\w+", s)
if adress: print(adress.group())
else: print("No email")