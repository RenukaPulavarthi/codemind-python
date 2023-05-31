def prime(n):
    if n==0 and n==1:
        return False
    s=0
    for i in range(2,n):
        if n%i==0:
            s=1
            break
    return s==0
n=int(input())
lst=[]
f=0
for i in range(2,n):
    if n%i==0:
        if prime(i):
            lst.append(i)
for i in range(len(lst)):
    for j in range(len(lst)):
        if i!=j:
            if lst[i]*lst[j]==n:
                f=1
                break
if f==1:
    if lst[i]<lst[j]:
        print(lst[i],lst[j])
    else:
        print(lst[j],lst[i])
else:
    print("-1")