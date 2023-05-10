n=input()
nu=int(n)
s=nu*nu
l=len(n)
k=s%(10**l)
if k==nu:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")