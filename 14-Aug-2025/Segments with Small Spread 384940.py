# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

import sys
from collections import Counter,defaultdict, deque
from itertools import accumulate 
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def solution():
    n,k =II()
    arr = IL()
    l=0
    ans = 0
    inc = deque()
    dec = deque()
    for i in range(n):
        while inc and arr[inc[-1]] >= arr[i]:
            inc.pop()
        inc.append(i)
        while dec and arr[dec[-1]] < arr[i]:
            dec.pop()
        dec.append(i)
        while abs(arr[dec[0]]-arr[inc[0]]) > k:
            l+=1
            if dec[0] < l:
                dec.popleft()
            if inc[0] < l:
                inc.popleft()
        ans += i-l+1 
    return ans

cases = 1
# cases = I()
for i in range(cases):
    print(solution())