def fac(n):
    m=1
    for i in range(1,n+1):
        m*=i
    return m

n=int(input())
s=0
m=n
while n:
    re=n%10
    s+=fac(re)
    n=n//10
if s==m:
    print(f"The number {m} is a strong number")
else:
    print(f"The number {m} is not a strong number")