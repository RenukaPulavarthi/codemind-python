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
k=len(set(lst))
print(k)