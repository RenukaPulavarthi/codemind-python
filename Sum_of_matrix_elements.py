r=int(input())
c=int(input())
k=[]
for i in range(r):
    l=list(map(int,input().split()))
    k.append(sum(l))
print(sum(k))
    