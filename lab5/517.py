import re
s = input()
txt = re.findall(r"\d{2}/\d{2}/\d{4}", s)
print(len(txt))