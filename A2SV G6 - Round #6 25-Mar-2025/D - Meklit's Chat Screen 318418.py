# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

import sys
from collections import Counter,defaultdict,deque
from itertools import accumulate 
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def IS(): return sys.stdin.readline().strip().split()
def psum(a): return [0] + list(accumulate(a))
def solution():
    n,k = II()
    arr = IL()
    que = deque()
    dic = defaultdict(int)
    for i in range(n):
        # print(que)
        if arr[i] in dic:
            # print("hi")
            continue
        dic[arr[i]] +=1
        que.appendleft(arr[i])
        if len(que) > k:
            x =  que.pop()
            dic[x] -=1
            if dic[x] == 0:
                del dic[x]
        # print(que,"\n")
        
    print(len(que))
    print(*que)

cases = 1
# cases = I()
for i in range(cases):
    solution()