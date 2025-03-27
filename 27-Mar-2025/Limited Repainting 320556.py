# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

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
    def checker(x):
        count_ans = 0
        red = float('inf')
        for color,cost in zip(s,arr):
            
            if color == 'B' and cost>x:
                if red>x:
                    count_ans +=1
                    red = 0
            if color == 'R':
                
                red = max(red,cost)
                
                
        return count >= count_ans
    n,count=II()
    s = S()
    arr = IL()
    low = 0
    high = max(arr)
    while low<=high:
        mid = (low+high)//2
        if checker(mid):
            res = mid
            high = mid-1
        else:
            low = mid +1
    return res

# cases = 1
cases = I()
for i in range(cases):
    print(solution())