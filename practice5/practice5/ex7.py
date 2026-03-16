import re

s = input()
result = re.sub(r"_([a-z])", lambda m: m.group(1).upper(), s)
print(result)

#_ алып тастап, одан кейінгі әріпті бас әріпке айналдырады.
