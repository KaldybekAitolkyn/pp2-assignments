s=input()
if any(ch in "aeoiuAEIOU" for ch in s):
    print("Yes")
else:
    print("No")