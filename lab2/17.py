n=int(input())
numbers=[]
for i in range(n):
    numbers.append(input().strip())
cnt=0
for num in set(numbers):
    if numbers.count(num)==3:
        cnt=cnt+1
print(cnt)