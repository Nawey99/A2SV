# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
from typing import Counter


n,k = map(int,input().split())
arr = list(map(int,input().split()))
max_size=0
count = defaultdict(int)
res = []
l = 0
for r in range(n):
    count[arr[r]] += 1
    while len(count) >k:
        count[arr[l]] -=1
        if count[arr[l]] == 0:
            del count[arr[l]]
        l +=1
        
    max_size = max(max_size,r-l)
    if max_size == r-l:
        res= [l+1,r+1]
        
print(*res)