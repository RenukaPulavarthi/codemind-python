r,c=map(int,input().split())
lst=[]
for i in range(r):
    l=list(map(int,input().split()))
    lst.append(l)
l=[]
for i in range(r):
    s=0
    for j in range(c):
        s+=lst[i][j]
    l.append(s)
for i in range(c):
    s=0
    for j in range(r):
        s+=lst[j][i]
    l.append(s)
print(max(l))