t=int(input())
if t<=100 and t>=3:
    for i in range(1,t+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
    for i in range(t,0,-1):
        for j in range(1,i):
            print("*",end="")
        if i-1>0:
            print()
else:
    print("The pattern is not possible")