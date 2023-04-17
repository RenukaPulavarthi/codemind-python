r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
ev=sum([sum(mat[i]) for i in range(r) if i % 2==0])
od=sum([sum(mat[i]) for i in range(r) if i % 2!=0])
print(f"{ev} {od}")