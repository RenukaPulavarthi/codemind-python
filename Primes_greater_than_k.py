def prime(n):
    if n<=1:
        return False
    s=0
    for i in range(2,n):
        if n%i==0:
            s=1
            break
    return s==0
n=int(input())
lst=list(map(int,input().split()))
m=int(input())
c=0
for i in lst:
    if i>=m:
        if prime(i):
            c+=1
print(c)