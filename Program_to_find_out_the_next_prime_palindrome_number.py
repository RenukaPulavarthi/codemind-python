def prime(n):
    f=0
    for i in range(2,n):
        if n%i==0:
            f=1
            break
    if f==1 or n==0 or n==1:
        return 0
    else:
        return 1

def pali(n):
    m=n
    s=0
    while m:
        re=m%10
        s=s*10+re
        m=m//10
    return s==n
    
n=int(input())
n+=1
while n:
    if prime(n):
        if pali(n):
            print(n)
            break;
    n+=1