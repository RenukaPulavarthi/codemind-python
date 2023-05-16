n=int(input())
lst=list(map(int,input().split()))
s=0
o=0
for i in range(len(lst)):
    if i%2==0:
        s+=lst[i];
    else:
        o+=lst[i]
if(s==o):
    print("YES")
else:
    print("NO")