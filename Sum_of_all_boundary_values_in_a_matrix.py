n,m=map(int,input().split())
lst=[]
c=0
for i in range(n):
    l=list(map(int,input().split()))
    lst.append(l)
for i in range(n):
    for j in range(m):
        if i==0 or j==n-1 or i==n-1 or j==0:
            c+=lst[i][j]
print(c)