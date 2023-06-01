s=list(input().split())
c=0
for i in s:
    m=i.lower()
    k=m[::-1]
    if m==k:
        c+=1
print(c)