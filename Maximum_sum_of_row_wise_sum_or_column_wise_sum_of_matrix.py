r,c=map(int,input().split())
lst=[]
l=[]
for i in range(r):
    ls=list(map(int,input().split()))
    lst.append(ls)
    l.append(sum(ls))
for i in range(c):
    s=0
    for j in range(r):
        s+=lst[j][i]
    l.append(s)
print(max(l))
        