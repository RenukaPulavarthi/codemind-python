n=int(input())
lst=[]
while n:
    re=n%10
    lst.append(re)
    n=n//10
print(max(lst))
    