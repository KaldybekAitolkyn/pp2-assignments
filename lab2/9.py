#max to min
n=int(input())
num=list(map(int,input().split()))
max=int(num[0])
min=int(num[0])
for i in num:
    i=int(i)
    if max<i:
        max=i
    if min>i:
        min=i
for i in range(n):
    if num[i]==max:
        num[i]=min
print(*num)
