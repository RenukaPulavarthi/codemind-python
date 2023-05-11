n=int(input())
s=64+n
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(s),end=" ")
    print()
    s-=1