def feb(n):
    a=0
    b=1
    for i in range(n):
        if a==n:
            return True
        c=a+b
        a=b
        b=c
    return False
n=int(input())
print(feb(n))