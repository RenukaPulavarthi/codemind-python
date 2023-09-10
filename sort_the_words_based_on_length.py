lst=list(input().split())
lst.sort(key=len)
for i in range(len(lst)-1):
    if len(lst[i])==len(lst[i+1]) and lst[i]>lst[i+1]:
        t=lst[i]
        lst[i]=lst[i+1]
        lst[i+1]=t
print(*lst)