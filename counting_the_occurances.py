n=input()
s=input()
c=0
for i in n:
    if i==s:
        c+=1
if c==0:
    print("-1")
else:
    print(c)