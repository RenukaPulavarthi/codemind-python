n,m=map(int,input().split())
lst=[]
for i in range(n):
    l=list(map(int,input().split()))
    lst.append(l)
    c=0
for i in range(m):
    f=0
    for j in range(n-1):
        if lst[j][i]>lst[j+1][i]:
            f=1
            break
    if f==0:
        c+=1
for i in range(m):
    f=0
    for j in range(n-1):
        if lst[j][i]<lst[j+1][i]:
            f=1
            break
    if f==0:
        c+=1
print(c)