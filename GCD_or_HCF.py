a,b=map(int,input().split())
m=min(a,b)
while m<=a*b:
    if a%m==0 and b%m==0:
        print(m)
        break;
    m=m-1
