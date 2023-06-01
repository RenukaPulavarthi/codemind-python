r,c=map(int,input().split())
lst=[]
for i in range(r):
    ls=list(map(int,input().split()))
    lst.append(ls)
for i in range(c):
    s=0
    for j in range(r):
        s+=lst[j][i]
    print(s,end=" ")
        