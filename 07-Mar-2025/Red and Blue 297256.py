# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

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
    r = I()
    arr_r = IL()
    rs_r = 0
    max_r= 0
    max_b= 0
    rs_b=0
    b = I()
    arr_b=IL()
    for i in arr_r:
        rs_r += i
        max_r=max(max_r,rs_r)
    for i in arr_b:
        rs_b += i
        max_b=max(max_b,rs_b)
    return max_b+max_r

# cases = 1
cases = I()
for i in range(cases):
    print(solution())