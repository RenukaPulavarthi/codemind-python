n=int(input())
lst=list(map(int,input().split()))
ls=[]
for i in lst:
    while i:
        re=i%10
        ls.append(re)
        i=i//10
print(sum(ls))