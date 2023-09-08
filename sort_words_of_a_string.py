def printing(s,l):
    j=0
    for i in range(len(s)):
        if s[i].isalnum():
            print(l[j],end="")
            j+=1
        else:
            print(s[i],end="")

lst=list(input().split())
l=[]
for i in range(len(lst)):
    for j in lst[i]:
        if j.isalnum():
            l.append(j)
    l.sort()
    printing(lst[i],l)
    print(" ",end="")
    l.clear()
