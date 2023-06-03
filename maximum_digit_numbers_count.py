n=int(input())
l=[]
c=0
lst=list(input().split())
for i in lst:
    l.append(len(i))
k=max(l)
for i in lst:
    if len(i)==k:
        print(i,end=" ")
