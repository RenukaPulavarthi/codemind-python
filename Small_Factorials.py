def fac(a:int)->int:
    f=1
    for i in range(1,a+1):
        f=f*i
    return f
    
n=int(input())
for i in range(n):
    s=int(input())
    print(fac(s))