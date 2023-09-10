def cons(s):
    l=[]
    for i in s:
        if i.isalpha() and i not in "aeiouAEIOU":
            l.append(i)
    l.sort()
    j=0
    for i in s:
        if i.isalpha() and i not in "aeiouAEIOU":
            print(l[j],end="")
            j+=1
        else:
            print(i,end="")

lst=list(input().split())
for i in lst:
    cons(i)
    print(" ",end="")