n=int(input())
lst=list(map(int,input().split()))
s=sum(lst)
av=s//n
c=0
for i in lst:
    if i<=av:
        c+=1
print(c)