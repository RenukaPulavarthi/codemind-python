n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    if i!=0 and i!=1:
        print("False")
        break;
else:
    print("True")