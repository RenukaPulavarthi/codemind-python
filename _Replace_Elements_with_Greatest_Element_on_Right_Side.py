n=int(input())
lst=list(map(int,input().split()))
for i in range(n):
    ma=-1
    for j in range(i+1,n):
        if ma<lst[j]:
            ma=lst[j]
    print(ma,end=" ")
        