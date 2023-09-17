n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
m=0
for i in lst:
    if i<a or i>b:
        if i>m:
            m=i
print(m if m!=0 else "-1")