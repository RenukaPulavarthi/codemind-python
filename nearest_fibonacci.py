def fib(n):
    a=0
    b=1
    for i in range(n):
        if n==a:
            return True
        c=a+b
        a=b
        b=c
    return False

n=int(input())
m=n+1
for i in range(n-1,-1,-1):
    if fib(i):
        p=i
        break
while m:
    if fib(m):
        a=m
        break
    m+=1
if n-p<a-n:
    print(p)
elif n-p==a-n:
    print(p,a)
else:
    print(a)