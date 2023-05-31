a,b=map(int,input().split())
lst=list(map(int,input().split()))
c=0
for i in lst:
    if i%b!=0:
        c+=1
print(c)