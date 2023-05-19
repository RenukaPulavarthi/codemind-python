n=int(input())
lst=list(map(int,input().split()))
k=lst[0]
for i in lst:
    if i<k:
        k=i
print(k)