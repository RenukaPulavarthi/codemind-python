s=list(input().split())
k=list(input().split())
c=0
for i in k:
    for j in s:
        if i==" " or i=="":
            pass
        elif i.lower()==j.lower():
            print(i,end=" ")
            break