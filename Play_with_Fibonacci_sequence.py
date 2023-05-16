n=int(input())
a=0
b=1
while n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    n-=1