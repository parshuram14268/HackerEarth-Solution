tst=int(input())
while(tst>0):
    a,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    lis=[]
    for i in range(0,a,2):
        lis.append(arr[i]+arr[a-i-1])
    ans=max(lis)-min(lis)
    if k==ans:
        print(ans,'\nLucky chap!')
    elif k<ans:
        print(ans,'\nNo more girlfriends!')
    else:
        print(ans,'\nChick magnet Jhool!')
    tst-=1
