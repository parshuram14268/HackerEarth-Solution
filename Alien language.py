tst=int(input())
while(tst>0):
    status=True
    s1=input()
    s2=input()
    for i in list(s1):
        if i in s2:
            print("YES")
            break
    else:
        print("NO")
    tst-=1
