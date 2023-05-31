m=int(input())
s=0
n=m**2
while n:
    re=n%10
    s+=re
    n=n//10
print("Neon Number" if s==m else "Not Neon Number")