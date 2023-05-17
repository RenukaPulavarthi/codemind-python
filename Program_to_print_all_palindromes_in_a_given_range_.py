def pali(n):
    m=n
    s=0
    while m:
        re=m%10
        s=s*10+re
        m=m//10
    return s==n
    
a=int(input())
b=int(input())
for i in range(a,b):
    if pali(i):
        print(i,end=" ")