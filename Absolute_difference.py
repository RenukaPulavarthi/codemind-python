def prime(n):
    f=0
    if n==0 or n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            f=1
            break;
    return f==0
    
n=int(input())
m=1
k=1
lst=list(map(int,input().split()))
for i in lst:
    if prime(i):
        m*=i
    else:
        k*=i
print(abs(k-m))