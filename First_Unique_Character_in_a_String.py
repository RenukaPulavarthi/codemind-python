s=input()
f=0
for i in range(len(s)):
    if s.count(s[i])==1:
        f=1
        print(i)
        break;
if f==0:
    print("-1")