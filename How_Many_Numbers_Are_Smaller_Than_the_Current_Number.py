n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    c=0
    for j in lst:
        if i!=j:
            if i>j:
                c+=1
    print(c,end=" ")