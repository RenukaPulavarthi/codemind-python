for _ in range(int(input())):
    a=int(input())
    lst=[]
    f=0
    while a:
        re=a%10
        lst.append(re)
        a=a//10
    lst.sort()
    for i in range(len(lst)-1):
        if lst[i]+1!=lst[i+1]:
            f=1
    if f==1:
        print("NO")
    else:
        print("YES")