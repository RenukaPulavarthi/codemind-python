n=input()
k=input()
lst=[]
for i in n:
    if i==' ':
        pass
    elif i.lower() in k:
        lst.append(i.lower())
    elif i.upper() in k:
        lst.append(i.lower())
k=list(set(lst))
k.sort()
if len(k)<1:
    print("-1")
else:
    for i in k:
        print(i,end="")