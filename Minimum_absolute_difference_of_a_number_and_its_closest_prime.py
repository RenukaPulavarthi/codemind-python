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
if prime(n):
    print("0")
else:
    np=n+1
    pp=n-1
    while np:
        if prime(np):
            break
        np+=1
    while pp:
        if prime(pp):
            break;
        pp-=1
    print(min(np-n,n-pp))