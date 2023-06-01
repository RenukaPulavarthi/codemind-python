r,c=map(int,input().split())
lst=[]
for i in range(r):
    ls=list(map(int,input().split()))
    lst.append(sum(ls))
print(max(lst))
        