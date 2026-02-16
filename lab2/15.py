#attendance
n=int(input())
name=set()
for i in range(n):
    name.add(input().strip())
print(len(name))          