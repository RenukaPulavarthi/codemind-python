n=input()
lst=[]
for i in n:
    lst.append(int(i))
for i in range(len(lst)):
    if lst[i]==6:
        lst[i]=9
        break;
for i in lst:
    print(i,end="")