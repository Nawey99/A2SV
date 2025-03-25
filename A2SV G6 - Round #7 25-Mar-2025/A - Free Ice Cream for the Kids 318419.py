# Problem: A - Free Ice Cream for the Kids - https://codeforces.com/gym/596141/problem/A

import sys
from collections import Counter,defaultdict
from itertools import accumulate 
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def IS(): return sys.stdin.readline().strip().split()
def psum(a): return [0] + list(accumulate(a))
def solution():
    deserted= 0
    n,x = II()
    for _ in range(n):
        p,d = input().split()
        d = int(d)
        if p == '-':
            if x<d:
                deserted +=1
            else:
                x-=d
        else:
            x+=d
    return x,deserted

cases = 1
# cases = I()
for i in range(cases):
    print(*solution())