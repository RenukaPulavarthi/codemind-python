n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
f=0
for i in lst:
    if i<a or i>b:
        f=1
        print(i,end=" ")
if f==0:
    print("-1")