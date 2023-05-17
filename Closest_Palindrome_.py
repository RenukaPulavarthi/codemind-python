def pali(n):
    s=n
    m=0
    while s:
        re=s%10
        m=m*10+re
        s=s//10
    return n==m
    
n=int(input())
np=n+1
pp=n-1
while np:
    if pali(np):
        break
    np+=1
while pp:
    if pali(pp):
        break
    pp-=1
if np-n < n-pp:
    print(np)
elif np-n == n-pp:
    print(pp,np)
else:
    print(pp)