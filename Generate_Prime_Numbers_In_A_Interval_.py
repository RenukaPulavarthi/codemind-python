def prime(n):
    if n==0 or n==1:
        return False
    s=0
    for i in range(2,n):
        if n%i==0:
            s=1
            break
    return s==0
n=int(input())
m=int(input())
for i in range(n,m+1):
    if prime(i):
        print(i)