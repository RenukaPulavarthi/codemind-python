n=input()
l=len(n)
s=int(n)
se=set()
while s:
    re=s%10
    se.add(re)
    s=s//10
if len(se)==l:
    print("Unique Number")
else:
    print("Not Unique Number")
