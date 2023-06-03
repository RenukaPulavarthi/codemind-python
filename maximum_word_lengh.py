lst=list(input().split())
l=[]
for i in lst:
    l.append(len(i))
print(max(l))