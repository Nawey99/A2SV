# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

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
    n = I()
    s = S()
    def rec(l=0,r=0,good=97):
        if l == r:
            return int(ord(s[r]) != good)
        m = (l+r)//2
        count_l,count_r = 0,0
        for i in range(l,m+1):
            if ord(s[i])!=good:
                count_l+=1
        for i in range(m+1,r+1):
            if ord(s[i])!=good:
                count_r+=1
        return min(count_l+rec(m+1,r,good+1),count_r+rec(l,m,good+1))
    return rec(0,n-1,97)

# cases = 1
cases = I()
for i in range(cases):
    print(solution())