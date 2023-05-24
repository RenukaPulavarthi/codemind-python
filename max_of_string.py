n=input()
s=ord('z')
if chr(s) in n:
    print(chr(s))
else:
    while 1:
        s-=1
        if chr(s) in n:
            print(chr(s))
            break
        