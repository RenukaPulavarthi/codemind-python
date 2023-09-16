n,m=map(int,input().split())
lst=[]
for i in range(n):
    l=list(map(int,input().split()))
    lst.append(l)
c=0
for i in range(1,n-1):
    for j in range(1,m-1):
        c+=lst[i][j]
print(c)