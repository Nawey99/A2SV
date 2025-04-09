# Problem: B - Empress Taytu and The Water Source - https://codeforces.com/gym/601269/problem/B

from math import ceil
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
    n, k = II()
    demand = IL()
    hours = IL()

    def checker(x):
        total = 0
        for d, h in zip(demand, hours):
            total += ceil(d / x) * h
        return total <= k

    low, high = 1, 10 ** 18
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if checker(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

# cases = 1
cases = I()
for i in range(cases):
    print(solution())