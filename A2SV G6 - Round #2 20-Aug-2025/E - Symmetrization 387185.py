# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

import sys

def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip()))

def solution():
    n = I()
    if n == 1:
        arr = IL()
        return 0  # Single cell, no flips needed
    
    arr = []
    res = 0
    visited = set()
    
    for _ in range(n):
        arr.append(IL())
    
    for i in range(n):
        for j in range(n):
            if (i, j) not in visited:
                num0 = 0
                num1 = 0
                coords = [
                    (i, j),
                    (j, n - 1 - i),           # 90° rotation
                    (n - 1 - i, n - 1 - j),   # 180° rotation
                    (n - 1 - j, i)            # 270° rotation
                ]
                
                for x, y in coords:
                    if (x, y) not in visited:
                        if arr[x][y] == 0:
                            num0 += 1
                        else:
                            num1 += 1
                        visited.add((x, y))
                
                res += min(num0, num1)
    
    return res

cases = I()
for _ in range(cases):
    print(solution())