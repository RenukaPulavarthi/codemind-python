n,m=map(int,input().split())
lst1=list(map(int,input().split()))
lst2=set(map(int,input().split()))
l=[]
for i in lst1:
    if i not in l:
        l.append(i)
for i in l:
    if i in lst2:
        print(i,end=" ")