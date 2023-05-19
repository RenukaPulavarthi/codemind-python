n=int(input())
lst=list(map(int,input().split()))
l=len(lst)
for i in range(l-1,0,-1):
    if lst[i]%2!=0:
        print(lst[i])
        break