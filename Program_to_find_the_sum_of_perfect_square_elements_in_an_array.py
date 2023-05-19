def per(n):
    f=0
    for i in range(1,n+1):
        if i*i==n:
            f=1
            break
    return f==1

n=int(input())
lst=list(map(int,input().split()))
s=0
for i in lst:
    if per(i):
        s+=i
print(s)