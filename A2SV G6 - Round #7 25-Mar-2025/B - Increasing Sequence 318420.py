# Problem: B - Increasing Sequence - https://codeforces.com/gym/596141/problem/B

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
    n = I()
    arr = IL()
    b = 0 
    flag = 1
    for i in arr:
        if i != 1 and b < 1:
            b+=1
        elif b+1 == i:
            b+=2
        else:
            b+=1
        
    return b

# cases = 1
cases = I()
for i in range(cases):
    print(solution())