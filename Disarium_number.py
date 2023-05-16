n=input()
l=len(n)
m=int(n)
t=m
s=0
while m:
    re=m%10
    s=s+(re**l)
    m=m//10
    l-=1
if s==t:
    print("True")
else:
    print("False")