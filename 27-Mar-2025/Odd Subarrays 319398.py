# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

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
    count = 0
    r = 1
    l = 0
    while r <n:
        if arr[r] < arr[l]:
            count +=1
            l = r
            r +=1
        l +=1
        r +=1
    return count

# cases = 1
cases = I()
for i in range(cases):
    print(solution())