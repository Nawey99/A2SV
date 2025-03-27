# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

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
    n,k= II()
    arr = IL()
    diff = []
    res = 0
    for i in range(1,n):
        diff.append(arr[i]-arr[i-1])
    diff.sort()
    k = n-k
    for i in range(k):
        res += diff[i]
    return res

cases = 1
# cases = I()
for i in range(cases):
    print(solution())