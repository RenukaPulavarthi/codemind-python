n=input()
s1=int(n)**2
k=int(n[::-1])
s2=str(int(k)**2)
s2=int(s2[::-1])
if s1==s2:
    print("True")
else:
    print("False")