n=input()
se=set()
for i in n:
    if i!=" " and i!="":
        se.add(i.lower())
k=len(se)
print(k)