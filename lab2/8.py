n=int(input())
s=1
print(s, end=" ")
while s<=n:
    s=s*2
    if s<=n:
        print(s, end=" ")
    else:
        break