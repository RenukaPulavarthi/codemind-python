def add(a):
    s=0;
    while a:
        re=a%10
        s+=re
        a=a//10
    return s
    
n=int(input())
k=add(n)
while k>9:
    k=add(k)
print(k)