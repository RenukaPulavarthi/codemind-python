def prime(n:int)->bool:
    if n==1 or n==0:
        return True
    f=0
    for i in range(2,n):
        if n%i==0:
            f=1
            break;
    return f==1

n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if prime(i):
            c+=1;
print(c)