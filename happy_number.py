def happy(n):
    s=0
    while n:
        re=n%10
        s+=re*re
        n=n//10
    return s

n=int(input())
s=happy(n)
while s>9:
    s=happy(s)
if s==1 or s==7:
    print("True")
else:
    print("False")