n=int(input())
lst=list(map(int,input().split()))
h=min(lst)
while(h):
    for i in lst:
        if i%h!=0:
            h-=1
            break
    else:
        break;
print(h)