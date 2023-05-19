n=int(input())
lst=list(map(int,input().split()))
o=0
for i in range(len(lst)):
    if lst[i]%2!=0:
        o+=lst[i]
print(o)