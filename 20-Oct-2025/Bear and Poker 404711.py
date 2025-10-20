# Problem: Bear and Poker - https://codeforces.com/problemset/problem/574/C

import sys
from collections import Counter,defaultdict
from itertools import accumulate 
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def solution():
    n =I()
    arr = IL()
    def fun(n):
        for d in range(2,4):
            while n % d == 0:
                n //= d
        return n
    ans = set()
    for i in range(n):
        ans.add(fun(arr[i]))
    return 'Yes' if len(ans) == 1 else 'No'
cases = 1
for i in range(cases):
    print(solution())