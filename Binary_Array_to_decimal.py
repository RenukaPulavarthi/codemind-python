n=int(input())
n=n-1
c=0
lst=list(map(int,input().split()))
for i in lst:
    if i==1:
        c+=2**n
    n-=1
print(c)