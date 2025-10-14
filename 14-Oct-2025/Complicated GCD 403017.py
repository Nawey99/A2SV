# Problem: Complicated GCD - https://codeforces.com/contest/664/problem/A

import random
import sys
from collections import Counter,defaultdict
from itertools import accumulate 
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def solution():
    a,b = II()
    if a==b:
        return a
    return 1

cases = 1
# cases = I()
for i in range(cases):
    print(solution())