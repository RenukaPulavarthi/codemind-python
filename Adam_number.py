n=input()
r=n[::-1]
k=int(n)
m=int(r)
sq=k*k
sq1=m*m
so=0
while sq1:
    re=sq1%10
    so=so*10+re
    sq1=sq1//10
if sq==so:
    print("True")
else:
    print("False")