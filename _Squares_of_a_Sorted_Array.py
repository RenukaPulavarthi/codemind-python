n=int(input())
lst=list(map(int,input().split()))
ls=[]
for i in lst:
    ls.append(i**2)
ls.sort()
for i in ls:
    print(i,end=" ")