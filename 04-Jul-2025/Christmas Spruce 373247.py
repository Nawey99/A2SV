# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B


import sys
from collections import defaultdict
def I(): return int(sys.stdin.readline().strip())
def solution():
    children = defaultdict(list)
    n = I()
    for child in range(2,n+1):
        parent = I()
        children[parent].append(child)
        
    for node in range(1, n + 1):
        if len(children[node]) > 0:  # internal node
            leaf_count = 0
            for child in children[node]:
                if len(children[child]) == 0:
                    leaf_count += 1
            if leaf_count < 3:
                return "No"
    
    return "Yes"

cases = 1
for i in range(cases):
    print(solution())