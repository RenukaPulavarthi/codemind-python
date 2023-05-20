n=int(input())
lst=list(map(int,input().split()))
s=0
for i in lst:
    s+=i*(2**(n-1))
    n-=1
print(s)