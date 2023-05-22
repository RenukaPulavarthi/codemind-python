n=input()
s=0
for i in n:
    if i.isdigit():
        s+=1
if s!=0:
    print(f'Contains {s} digit')
else:
    print("Doesn't contain digit")