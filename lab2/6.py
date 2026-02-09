n=int(input())
num=input().split()
max=int(num[0])
for i in num:
    i=int(i)
    if max<i:
        max=i
print(max)