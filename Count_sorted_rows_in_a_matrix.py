n,m=map(int,input().split())
lst=[]
for i in range(n):
    l=list(map(int,input().split()))
    lst.append(l)
    c=0
for i in range(n):
    f=0
    for j in range(m-1):
        if lst[i][j]>lst[i][j+1]:
            f=1
            break
    if f==0:
        c+=1
for i in range(n):
    f=0
    for j in range(m-1):
        if lst[i][j]<lst[i][j+1]:
            f=1
            break
    if f==0:
        c+=1
print(c)