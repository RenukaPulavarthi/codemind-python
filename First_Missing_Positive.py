n=int(input())
lst=list(map(int,input().split()))
i=1
while i:
    if i not in lst:
        print(i)
        break;
    i+=1