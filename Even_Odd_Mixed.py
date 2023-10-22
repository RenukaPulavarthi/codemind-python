n=int(input())
o=0
e=0
while(n):
    re=n%10
    if re%2==0:
        e+=1
    else:
        o+=1
    n=n//10
if e>0 and o>0:
    print("Mixed")
elif e>0:
    print("Even")
else:
    print("Odd")