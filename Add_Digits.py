def Add(n:int)->int:
    s=0
    while(n):
        s+=n%10
        n=n//10
    if s<10:
        return s;
    else:
        return Add(s)

n=int(input())
print(Add(n))