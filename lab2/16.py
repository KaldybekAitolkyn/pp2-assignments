#new or old
n=int(input())
num=list(map(int, input().split()))
s=set()
for i in num:
    if i not in s:
        print("YES")
        s.add(i)
    else:
        print("NO")