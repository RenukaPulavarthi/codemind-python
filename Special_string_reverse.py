n=input()
lst=[]
ls=[]
k=0
for i in n:
    if i.isalpha():
        lst.append(i)
for i in range(len(lst)-1,-1,-1):
    ls.append(lst[i])
for i in range(len(n)):
    if n[i].isalpha():
        print(ls[k],end='')
        k+=1
    else:
        print(n[i],end="")