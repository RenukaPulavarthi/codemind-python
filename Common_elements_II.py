n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=[]
for i in l1:
    if i not in l:
        l.append(i)
for i in l:
    if i not in l2:
        print(i,end=" ")
for i in l2:
    if i not in l:
        print(i,end=" ")