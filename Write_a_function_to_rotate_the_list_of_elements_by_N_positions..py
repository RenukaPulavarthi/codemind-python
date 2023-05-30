n=int(input())
lst=list(map(int,input().split()))
k=int(input())
k=(n-k)%n
for i in range(k,n):
    print(lst[i],end=" ")
for i in range(0,k):
    print(lst[i],end=" ")