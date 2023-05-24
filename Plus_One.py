n=int(input())
lst=list(map(int,input().split()))
m=0
for i in lst:
    m=m*10+i
m=m+1
ls=[]
while m:
    re=m%10
    ls.append(re)
    m=m//10
for i in range(len(ls)-1,-1,-1):
    print(ls[i],end=" ")