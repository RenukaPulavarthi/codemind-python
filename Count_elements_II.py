n,m=map(int,input().split())
s=set(map(int,input().split()))
se=set(map(int,input().split()))
print(len(s.union(se))-len(s.intersection(se)))