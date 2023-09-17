n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(0,n-2,2):
    if lst[i]<lst[i+1] and lst[i+1]>lst[i+2]:
        c+=1
    elif lst[i]>lst[i+1] and lst[i+1]<lst[i+2]:
        c+=1
    else:
        c=0
        break
print("yes" if c!=0 else "no")