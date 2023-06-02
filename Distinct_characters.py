n=input()
lst=[]
for i in n:
    if i==" " or i=="":
        pass
    elif n.count(i.lower())==1:
        lst.append(i.lower())
lst.sort()
for i in lst:
    print(i,end="")