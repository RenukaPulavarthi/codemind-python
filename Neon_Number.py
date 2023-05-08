n=int(input())
s=n*n
su=0
while s:
    r=s%10;
    su+=r
    s//=10
if su==n:
    print("Neon Number")
else:
    print("Not Neon Number")