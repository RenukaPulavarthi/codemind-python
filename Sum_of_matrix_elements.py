n=int(input())
r=int(input())
lst=[]
for i in range(n):
    l=list(map(int,input().split()))
    lst.append(sum(l))
print(sum(lst))