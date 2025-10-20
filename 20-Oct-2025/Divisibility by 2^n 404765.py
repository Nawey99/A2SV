# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

import sys
from collections import Counter,defaultdict
from itertools import accumulate 
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def solution():
    n=I()
    arr = IL()
    def fun(x):
        temp = 0
        while x %2 ==0:
            x //=2
            temp+=1
        return temp
    ans =0 
    for i in arr:
        ans += fun(i)
    ans = n-ans
    if ans <= 0:
        return 0
    count = 0
    x = n//2
    temp = []
    for i in range(x,0,-1):
        temp.append(fun(i*2))
    temp.sort()
    for i in range(len(temp)-1,-1,-1):
        ans -= temp[i]
        count+=1
        if ans <=0:
            return count
    return -1
            
        

# cases = 1
cases = I()
for i in range(cases):
    print(solution())