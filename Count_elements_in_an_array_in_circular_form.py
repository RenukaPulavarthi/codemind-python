n=int(input())
lst=list(map(int,input().split()))
s=0
if lst[0]%2==0 and lst[-2]%2!=0:
    s+=1
elif lst[0]%2!=0 and lst[-2]%2==0:
    s+=1
if lst[1]%2==0 and lst[-1]%2!=0:
    s+=1
elif lst[1]%2!=0 and lst[-1]%2==0:
    s+=1
for i in range(1,n-1):
    if lst[i-1]%2==0 and lst[i+1]%2!=0:
        s+=1
    elif lst[i-1]%2!=0 and lst[i+1]%2==0:
        s+=1
print(s)