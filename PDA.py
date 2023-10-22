n=int(input())
s=sum([i for i in range(1,n) if n%i==0])
if n==s:
    print("PERFECT")
elif n>s:
    print("DEFICIENT")
else:
    print("ABUNDANT")