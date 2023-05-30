n=int(input())
lst=list(map(int,input().split()))
for i in range(n):
    c=0
    f=0
    for j in range(i+1,n):
        if lst[i]<lst[j]:
            f=1
            c+=1
            break;
        c+=1
    if f==1:
        print(c,end=" ")
    else:
        print("0",end=" ")