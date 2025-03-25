# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

import sys
from collections import Counter,defaultdict, deque
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
    que = deque()
    n = len(arr)
    que.append(arr[0])
    for i in range(1,n):
        if arr[i] <que[0]:
            que.appendleft(arr[i])
        else:
            que.append(arr[i])
        # print(que[0])
    return que

# cases = 1
cases = I()
for i in range(cases):
    print(*solution())