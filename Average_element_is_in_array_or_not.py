n=int(input())
lst=list(map(int,input().split()))
s=sum(lst)
f=0
k=s//n
for i in lst:
    if i==k:
        f=1
        break
if f==1:
    print("True")
else:
    print("False")