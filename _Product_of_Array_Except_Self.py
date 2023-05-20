n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    m=1
    for j in lst:
        if i!=j:
            m=m*j
    print(m,end=" ")