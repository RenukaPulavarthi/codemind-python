s=input()
f=0
for i in s:
    if s.count(i)>1:
        f=1
        break
print("True" if f==0 else "False")