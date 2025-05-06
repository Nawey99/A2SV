# Problem: C - Arya Meets the Night King  - https://codeforces.com/gym/599383/problem/C

from bisect import bisect_right
import sys
from collections import Counter,defaultdict
from itertools import accumulate 
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def IS(): return sys.stdin.readline().strip().split()
def psum(a): return [0] + list(accumulate(a))
s,b = II()
attack =IL()
arr =[]
for _ in range(b):
    arr.append(IL())
arr.sort()
power = [arr[i][0] for i in range(b)]
defence = list(accumulate(arr[i][1] for i in range(b)))
ans = []
for atk in attack:
    idx = bisect_right(power, atk) - 1
    if idx >= 0:
        ans.append(defence[idx])
    else:
        ans.append(0)
print(*ans)