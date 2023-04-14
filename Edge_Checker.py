a,b=map(int,input().split())
if a+1==b:
    print("Yes")
elif b+1==a:
    print("Yes")
elif a==1 and b==10:
    print("Yes")
elif a==10 and b==1:
    print("Yes")
else:
    print("No")