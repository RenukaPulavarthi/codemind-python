def self_div(n: int)->bool:
    a=n
    while n:
        r=n%10
        if r==0:
            return False
        if a%r>0:
            return False;
        n=n//10
    return True;
   
n=int(input())
s=int(input())
for i in range(n,s+1):
    if self_div(i):
        print(i,end=" ")