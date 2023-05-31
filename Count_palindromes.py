def pali(n):
    s=n
    m=0
    while s:
        re=s%10
        m=m*10+re
        s=s//10
    return n==m
    
n=int(input())
c=0
lst=list(map(int,input().split()))
for i in lst:
    if pali(i):
        c+=1
print(c)