#prime
n=int(input())
if n<=1:
    print("NO")
else:
    prime=True
    for i in range(2,n):
        if n%i==0:
            prime=False
            break
if prime:
            print("YES")
else:
            print("NO")