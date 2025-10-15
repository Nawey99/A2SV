# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

import sys
from math import prod
from collections import Counter,defaultdict
from itertools import accumulate 
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def solution():
    n = I()
    arr =IL()
    ans = defaultdict(int)
    for i in range(n):
        temp = arr[i]
        d = 2
        while d * d <= temp:
            while temp % d == 0:
                ans[d] +=1
                temp //= d
            d += 1
        if temp >1 :
            ans[temp] +=1
    if len(ans.values()) ==0 and len(set(arr)) != 1:
        return 'NO'
    for val in ans.values():
        if val % n != 0:
            return 'NO'
    return 'YES'
# cases = 1
cases = I()
for i in range(cases):
    print(solution())