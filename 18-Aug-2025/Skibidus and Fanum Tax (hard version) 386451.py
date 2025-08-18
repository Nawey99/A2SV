# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

from bisect import bisect_left
import sys
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def solution():
    n,m = II()
    arr = IL()
    b = sorted(IL())
    if n == 1:
        return 'YES'
    prev = min(arr[0],b[0]-arr[0])
    for i in range(1,n):
        x = bisect_left(b,prev+arr[i])
        if x ==m:
            if arr[i] < prev:
                return 'NO'
            prev = arr[i]
        else:
            val = b[x]-arr[i]
            if arr[i] >= prev and val >= prev:
                prev = min(arr[i], val)
            elif arr[i] >= prev:
                prev = arr[i]
            elif val >= prev:
                prev = val
            else:
                return "NO"
    return 'YES'

# cases = 1
cases = I()
for i in range(cases):
    print(solution())