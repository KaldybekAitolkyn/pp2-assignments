def isUsual(num):
    for i in(2,3,5):
        while num%i==0:
            num=num//i
    if num==1:
        return True
    else:
        return False
    
num=int(input())
if(isUsual(num)):
    print("Yes")
else:
    print("No")