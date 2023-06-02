s=list(input().split())
k=list(input().split())
c=0
for i in s:
    for j in k:
        if i.lower()==j.lower():
            c+=1
            break
print(c)