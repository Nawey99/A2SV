# Problem: A - The Ticket Booth - https://codeforces.com/gym/594077/problem/A

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
    n,s = II()
    x  = s//n
    if s %n == 0:
        return x
    return x + 1

cases = 1
# cases = I()
for i in range(cases):
    print(solution())