n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
f=0
for i in range(n):
    if lst[i]>=a and lst[i]<=b:
        print(lst[i],end=" ")
        f=1
if f==0:
    print("-1")