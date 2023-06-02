n=int(input())
peo=[]
hou=[]
for i in range(n):
    s=int(input())
    peo.append(s)
for i in range(n):
    s=int(input())
    hou.append(s)
for i in range(n):
    for j in range(len(hou)):
        if peo[i]<=hou[j]:
            hou.remove(hou[j])
            break
print(len(hou))