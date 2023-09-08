s=input()
l=[]
for i in s:
    if i!=" ":
        l.append(i)
    else:
        l.sort()
        print(l[0],l[-1],end=" ")
        l.clear()
l.sort()
print(l[0],l[-1])