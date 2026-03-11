import re
s = input()
d = input()
spl = re.split(d, s)
print(",".join(spl))