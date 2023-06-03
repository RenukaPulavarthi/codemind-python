lst=list(input().split())
for i in range(len(lst)):
    if i%2==0:
        print(lst[i][::-1],end=" ")
    else:
        print(lst[i],end=" ")