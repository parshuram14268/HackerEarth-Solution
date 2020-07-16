n,q=map(int,input().split())
s=list(map(int,input().split()))
for i in range(q):
    arr=list(map(int,input().split()))
    if arr[0] is 1:
        if s[arr[1]-1]==0:
            s[arr[1]-1]=1
        else:
            s[arr[1]-1]=0
    else:
        if s[arr[2]-1] == 0:
            print("EVEN")
        else:
            print("ODD")
