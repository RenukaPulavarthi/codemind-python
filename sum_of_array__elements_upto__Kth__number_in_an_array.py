n=int(input())
lst=list(map(int,input().split()))
m=int(input())
s=0
for i in lst:
    s+=i
    if i==m:
        break
print(s)