n=int(input())
for i in range(n):
    k=int(input())
    s=input()
    f=0
    for i in s:
        if s.count(i)==1 and i!=" " and i!='':
            f=1
            print(i)
            break;
    if f==0:
        print("-1")