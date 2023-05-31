def selfd(n):
    m=n
    f=0
    while(m):
        re=m%10
        if re==0 or n%re>0:
            f=1
            break
        m=m//10
    if f==0:
        print(n,end=" ")


n=int(input())
m=int(input())
for i in range(n,m+1):
    selfd(i)
    