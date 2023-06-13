def reverse(n):
    s=str(n)
    k=int(s[::-1])
    return n+k
def pali(n):
    s=str(n)
    k=int(s[::-1])
    return n==k

n=int(input())
while n:
    k=reverse(n)
    if pali(k):
        print(k)
        break
    n=k