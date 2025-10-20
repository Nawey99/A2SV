# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

import sys
from math import ceil
from collections import Counter,defaultdict
from itertools import accumulate 
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def solution():
    n,d = II()
    if n < d:return -1
    else:
        temp = ceil(n/2)  
        return temp if temp % d == 0 else temp + (d - temp%d)
 
cases = 1
for i in range(cases):
    print(solution())
