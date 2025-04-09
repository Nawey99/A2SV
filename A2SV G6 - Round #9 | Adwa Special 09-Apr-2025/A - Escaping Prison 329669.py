# Problem: A - Escaping Prison - https://codeforces.com/gym/601269/problem/A

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
    n,k = II()
    Max = 0
    for i in range(n):
        Max += max(II())
    return "YES" if Max >= k else "NO"

# cases = 1
cases = I()
for i in range(cases):
    print(solution())