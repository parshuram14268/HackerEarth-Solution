import math
from collections import Counter
tst=int(input())
for i in range(tst):
    s=input()
    n=int(s)
    x=0
    if len(s)==1 or len(set(s))==1:
        x=1
    elif len(s) == len(set(s)):
        x=math.factorial(len(s))
    else:
        d=dict(Counter(list(s)))
        x=math.factorial(len(s))
        for (a,b) in d.items():
            x=x//math.factorial(int(b))
    print(x%(10**9 + 7))
