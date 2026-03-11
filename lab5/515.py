import re
s = input()
def convert(match):
    return match.group(1) + match.group(1)
txt = re.sub("([0-9])", convert, s)
print(txt)