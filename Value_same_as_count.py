n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    if i==lst.count(i) and i not in l:
        l.append(i)
print(len(l))