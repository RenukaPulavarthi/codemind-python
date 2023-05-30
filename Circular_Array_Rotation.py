n,k,q=map(int,input().split())
lst=list(map(int,input().split()))
k=(n-k)%n
ls=[]
for i in range(k,n):
    ls.append(lst[i])
for i in range(0,k):
    ls.append(lst[i])
for i in range(q):
    o=int(input())
    print(ls[o])
