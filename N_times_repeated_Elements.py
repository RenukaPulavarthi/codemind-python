n=int(input())
lst=list(map(int,input().split()))
k=int(input())
l=[]
for i in lst:
    if k==lst.count(i) and i not in l:
        l.append(i)
if len(l)==0:
    print("-1")
else:
    print(*l)