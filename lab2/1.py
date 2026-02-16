#leap if it is divisible by 4, but not by 100, or if it is divisible by 400.
a=int(input())
if (a%4==0 and a%100!=0) or a%400==0:
    print("YES")
else:
    print("NO")
