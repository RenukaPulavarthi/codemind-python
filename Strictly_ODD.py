n=int(input())
lst=list(map(int,input().split()))
s=0
c=0
for i in range(n):
    if lst[i]%2==0:
        s+=1
        if i%2==0:
            c+=1
print(s==c)