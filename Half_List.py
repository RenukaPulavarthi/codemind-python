n=int(input())
lst=list(map(int,input().split()))
lst1=[lst[i] for i in range(n//2)]
lst2=[lst[i] for i in range(n-1,(n//2)-1,-1)]
for i in lst2:
    print(i,end=" ")
for i in lst1:
    print(i,end=" ")