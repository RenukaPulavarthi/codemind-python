def vowel(s):
    l=0
    for i in s:
        if i.isalpha() and i in "aeiouAEIOU":
            l+=1
    return l

lst=list(input().split())
l=[]
for i in lst:
    l.append(vowel(i))
print(l.count(max(l)))