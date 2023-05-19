n=int(input())
lst=list(map(int,input().split()))
k=int(input())
f=0
for i in lst:
    if i==k:
        f=1
        break
if f==1:
    print("True")
else:
    print("False")