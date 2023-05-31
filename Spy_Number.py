n=int(input())
s=0
m=1
while n:
    re=n%10
    s+=re
    m*=re
    n=n//10
print("Spy Number" if s==m else "Not Spy Number")