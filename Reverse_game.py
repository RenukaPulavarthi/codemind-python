n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    s=0
    while(i):
        s=(s*10)+(i%10)
        i=i//10
    print(s,end=" ")