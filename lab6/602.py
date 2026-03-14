n=int(input())
numbers=list(map(int, input().split()))
print(len(list(filter(lambda x: x%2==0, numbers))))