s=input()
if s[0]=="-":
    c=s[1::]
    k=c[::-1]
    if k[0]=="0":
        print("-{}".format(c[1::-1]))
    else:
        print("-{}".format(k))
else:
    k=s[::-1]
    if k[0]=="0":
        print("{}".format(k[1::]))
    else:
        print(k)
    