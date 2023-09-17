n=int(input())
lst= list(map(int,input().split()))
for i in range(0,n,2):
    for j in range(lst[i+1]):
        print(lst[i],end=" ")