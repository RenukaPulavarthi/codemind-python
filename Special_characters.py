n=input()
lst=[]
num=[]
for i in n:
    if i.isalpha() or i==" " or i=='':
        pass
    elif i.isdigit():
        num.append(int(i))
    else:
        lst.append(i)
if len(lst)%2==0:
    while num:
        for i in num:
            if i%2==0:
                print(i,end="")
                num.remove(i)
                break
        for i in num:
            if i%2!=0:
                print(i,end="")
                num.remove(i)
                break
else:
    while num:
        for i in num:
            if i%2!=0:
                print(i,end="")
                num.remove(i)
                break
        for i in num:
            if i%2==0:
                print(i,end="")
                num.remove(i)
                break
            