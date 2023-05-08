a,b=map(int,input().split())
s=max(a,b)
while s:
    if s % a==0 and s % b==0:
        print(s)
        break;
    s+=1