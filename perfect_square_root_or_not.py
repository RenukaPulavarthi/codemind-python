n=int(input())
f=0
for i in range(n):
    if i*i==n:
        f=1
        break;
if f==1:
    print("True")
else:
    print("False")
        