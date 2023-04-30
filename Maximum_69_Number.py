n=int(input())
l=n%10;
k=(n//10)%10
m=(n//100)%10
o=n//1000
if o==6:
    o=9
elif m==6:
    m=9
elif k==6:
    k=9
elif l==6:
    l=9
print(o,end="")
print(m,end="")
print(k,end="")
print(l,end="")