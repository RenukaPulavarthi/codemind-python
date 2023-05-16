def pali(n):
   s=n
   v=0
   while s:
       re=s%10
       v=v*10+re
       s=s//10
   return v==n

n=int(input())
s=n+1
while s:
    if pali(s):
        l=s
        break;
    s+=1
m=n-1
while m:
    if pali(m):
        r=m
        break;
    m-=1
if l-n < n-r:
    print(l)
elif l-n == n-r:
    print(r,l)
else:
    print(r)
    
    