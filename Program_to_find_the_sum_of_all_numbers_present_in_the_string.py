def digi(s):
    f=0
    for i in s:
        if i.isdigit():
            f+=int(i)
    return f 


n=input()
print(digi(n))