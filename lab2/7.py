n=int(input())
num=input().split()
max=int(num[0])
pos=1
for i in range(1,n):
    if max<int(num[i]):
        max=int(num[i])
        pos=i+1
print(pos)