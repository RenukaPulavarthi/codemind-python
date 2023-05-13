n=int(input())
lst=list(map(int,input().split()))
m=max(lst)
s=0
while s!=len(lst):
    s=0
    for i in lst:
        if m%i==0:
           s+=1
    m+=1
print(m-1)