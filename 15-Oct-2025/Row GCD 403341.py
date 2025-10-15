# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

import sys
from math import gcd
from collections import Counter,defaultdict
from itertools import accumulate 
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def solution():
    n,m = II()
    arr = IL()
    arr1 = IL()
    store = []
    arr.sort()
    for i in range(1,n):
        store.append(arr[i]-arr[i-1])

    ans=[]
    gcf = gcd(*store)
    for i in arr1:
        ans.append(gcd(gcf,i+arr[0]))
    return ans
        

cases = 1
for i in range(cases):
    print(*solution())