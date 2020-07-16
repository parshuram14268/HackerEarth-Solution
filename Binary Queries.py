n,q=map(int,input().split())
s=list(map(int,input().split()))
for i in range(q):
    arr=list(map(int,input().split()))
    if arr[0] is 1:
        s[arr[1]-1]=(s[arr[1]-1])^1
    else:
        if s[arr[2]-1] == 0:
            print("EVEN")
        else:
            print("ODD")
