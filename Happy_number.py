def happy(n:int)->int:
    s=0
    while(n):
        s+=(n%10)**2
        n=n//10
    if s<10:
        return s;
    else:
        return happy(s)

n=int(input())
k=happy(n)
if k==1 or k==7:
    print("True")
else:
    print("False")