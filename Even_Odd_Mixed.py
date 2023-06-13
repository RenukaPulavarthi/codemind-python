n=int(input())
s=n
lst=[]
c=0
while n:
    lst.append(n%10)
    n=n//10
for i in lst:
    if i%2==0:
        c+=1
if c==len(lst):
    print("Even")
elif c<len(lst) and c!=0:
    print("Mixed")
else:
    print("Odd")