# Problem: B - Nafargi's Binary Reduction Game - https://codeforces.com/gym/594077/problem/B

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
    s = S()
    count = 0
    for i in s:
        if i == '0':
            count-=1
        else:
            count+=1
    return abs(count)

cases = 1
# cases = I()
for i in range(cases):
    print(solution())