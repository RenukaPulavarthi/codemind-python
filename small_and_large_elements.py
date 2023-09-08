l=list(input().split())
k=[]
for i in l[0]:
    k.append(i)
k.sort()
print(k[0],end=" ")
k.clear()
for i in l[-1]:
    k.append(i)
k.sort()
print(k[-1])