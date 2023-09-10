def vowel(s):
    l=0
    for i in s:
        if i.isalpha() and i in "aeiouAEIOU":
            l+=1
    print(l,end=" ")
lst=list(input().split())
for i in lst:
    vowel(i)