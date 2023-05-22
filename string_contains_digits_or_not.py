def digi(s):
    f=0
    for i in s:
        if i.isdigit():
            f+=1
    if f!=0:
        print("Yes")
    else:
        print("No")


n=int(input())
for i in range(n):
    s=input()
    digi(s)