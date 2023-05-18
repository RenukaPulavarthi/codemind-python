def prime(n):
    if n==0 and n==1:
        return False
    s=0
    for i in range(2,n):
        if n%i==0:
            s=1
            break
    return s==0
n=int(input())
m=int(input())
s=n+m+1
while s:
    if prime(s):
        break
    s+=1
print(s-(n+m))