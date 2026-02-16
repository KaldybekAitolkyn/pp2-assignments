#moda
n=int(input())
num=list(map(int, input().split()))
elem=num[0]
maxcnt=0
for i in range(n):
    cnt=0
    for j in range(n):
        if num[i]==num[j]:
            cnt=cnt+1
    if cnt>maxcnt or (cnt==maxcnt and num[i]<elem):
        maxcnt=cnt
        elem=num[i]
print(elem)        
    
