for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if lst[i]+lst[j] in lst:
                c+=1
    print(c if c!=0 else "-1")