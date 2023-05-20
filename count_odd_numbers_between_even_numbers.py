n=int(input())
c=0
lst=list(map(int,input().split()))
for i in range(1,len(lst)-1):
    if lst[i-1]%2==0 and lst[i+1]%2==0:
        if lst[i]%2!=0:
            c+=1
print(c)