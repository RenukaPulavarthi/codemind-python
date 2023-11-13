n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    if i==lst.count(i) and i not in l:
        l.append(i)
print(f"{sum(l)/len(l):.2f}" if len(l)!=0 else "-1")