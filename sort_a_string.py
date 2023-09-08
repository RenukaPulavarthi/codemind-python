s=input()
l=[]
for i in s:
    if i.isalnum():
        l.append(i)
l.sort()
j=0
for i in range(len(s)):
    if s[i].isalnum():
        print(l[j],end="")
        j+=1
    else:
        print(s[i],end="")