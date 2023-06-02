n=input()
k=input()
lst=[]
for i in n:
    if i==" ":
        pass
    elif (i.lower() not in k) and (i.upper() not in k):
        lst.append(i.lower())
for i in k:
    if i==" ":
        pass
    elif (i.lower() not in n) and (i.upper() not in n):
        lst.append(i.lower())
k=len(set(lst))
print(k-1)