# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
import sys
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def solution():
    n=I()
    arr = IL()
    count = Counter(arr)
    
    options = set(count.values())
    min_deletions = float('inf')
    
    #c is always in range 1 to n
    for c in range(1, n + 1):
        if c not in options:
            continue

        deletions = 0
        for num in count:
            if count[num] < c:
                deletions += count[num]
            else:
                deletions += count[num] - c
        
        min_deletions = min(min_deletions, deletions)
    return min_deletions

# cases = 1
cases = I()
for i in range(cases):
    print(solution())