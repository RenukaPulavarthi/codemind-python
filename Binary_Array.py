n=int(input())
lst=list(input().split())
f=0
for i in lst:
    if i in '01':
        pass
    else:
        f=1
        break
print(f==0)