n=input()
se=set()
for i in n:
    if i!=" " and i!="":
        se.add(i.lower())
k=list(se)
k.sort()
for i in k:
    print(i,end="")