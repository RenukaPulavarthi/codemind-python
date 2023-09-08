n=int(input())
se=set(map(int,input().split()))
c=0
for i in se:
    if i%2!=0:
        c+=1
print(c)