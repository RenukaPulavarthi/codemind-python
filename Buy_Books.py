n=int(input())
ls=list(map(int,input().split()))
lst=list(map(int,input().split()))
k=sum(lst)-sum(ls)
if k>0:
    print(k)
else:
    print("0")