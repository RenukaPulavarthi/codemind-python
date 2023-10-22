n=int(input())
l=len(str(n))
s=(n*n)%(10**l)
if s==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
