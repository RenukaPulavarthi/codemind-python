n=int(input())
lst=list(map(int,input().split()))
l=[]
while(len(lst)):
    for i in range(len(lst)):
        if lst[i]%2!=0:
            l.append(lst[i])
            lst.remove(lst[i])
            break
    for i in range(len(lst)):
        if lst[i]%2==0:
            l.append(lst[i])
            lst.remove(lst[i])
            break;
if n%2==0:
    print(*l)
else:
    l.append(0)
    print(*l)
    