l=input()
n=l.lower()
c=0
for i in n:
    if n.count(i)==1 and i!=''and i!=' ':
        c+=1
print(c)