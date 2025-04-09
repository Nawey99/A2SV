# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

import random
import sys
from collections import Counter,defaultdict
from itertools import accumulate 
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def IS(): return sys.stdin.readline().strip().split()
def psum(a): return [0] + list(accumulate(a))
rand = random.randrange(2^62)
def wrapper(x): return x ^ rand
def solution():
    n,m = II()
    adj_list = defaultdict(int)
    visited = set()
    for _ in range(m):
        i,j =II()
        adj_list[i]+=1
        adj_list[j]+=1
    list_ = list(adj_list.values())
    count= Counter(list_)
    if count[2] == n :
        return 'ring topology'
    if count [2] == n-2 and count[1] ==2:
        return 'bus topology'
    if count [m] == 1:
        return 'star topology'   
    return 'unknown topology'

cases = 1
# cases = I()
for i in range(cases):
    print(solution())