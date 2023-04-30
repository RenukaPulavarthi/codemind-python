def add(a: int)->int:
    sum=0
    while a:
        r=a%10
        sum=sum+r
        a=a//10
    if sum<10:
        return sum
    else:
        return add(sum)

n=int(input())
s=add(n)
print(s)
        