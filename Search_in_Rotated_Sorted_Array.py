n=int(input())
lst=list(map(int,input().split()))
m=int(input())
f=0
for i in range(n):
    if lst[i]==m:
        f=1
        break
print(i if f==1 else "-1")