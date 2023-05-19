n=int(input())
lst=list(map(int,input().split()))
s=sum(lst)
f=0
k=s/n
print('{:.2f}'.format(k))
