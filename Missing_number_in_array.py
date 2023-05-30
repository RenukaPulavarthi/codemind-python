for i in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    for j in range(1,n+1):
        if j not in lst:
            print(j)