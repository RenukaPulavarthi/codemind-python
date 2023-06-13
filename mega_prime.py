def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
n=int(input())
s=n
lst=[]
c=0
while(n):
    lst.append(n%10)
    n=n//10
if prime(s):
    for i in lst:
        if prime(i):
            c+=1
    if c==len(lst):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
    