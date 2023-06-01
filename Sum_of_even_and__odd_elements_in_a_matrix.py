n,m=map(int,input().split())
s=0
c=0
for i in range(n):
    lst=list(map(int,input().split()))
    for i in lst:
        if i%2==0:
            s+=i
        else:
            c+=i
print(s,c)