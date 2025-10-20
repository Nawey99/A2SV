# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A


import sys
from collections import Counter,defaultdict
from itertools import accumulate 
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def solution():
    l,r,d = II()
    if l > d:
        return d
    else:
        return r + (d-(r%d))
 
# cases = 1
cases = I()
for i in range(cases):
    print(solution())