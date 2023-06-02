s=input()
k=input()
m=list(s+k)
m.sort()
for i in m:
    if i!=" " and i!="":
        print(i,end="")