def prime(n:int)->bool:
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
n=int(input())
lst=list(map(int,input().split()))
mini=min(lst.index(min(lst)),lst.index(max(lst)))
maxi=max(lst.index(min(lst)),lst.index(max(lst)))
c=0
for i in range(mini,maxi+1):
    if prime(lst[i]):
        c+=1
print(c)