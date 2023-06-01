r,c=map(int,input().split())
lst=[]
for i in range(r):
    ls=list(map(int,input().split()))
    lst.append(sum(ls))
for i in lst:
    print(i,end=" ")