# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

import sys
import math
import bisect
from collections import Counter, defaultdict

read_int = lambda: int(sys.stdin.readline().strip())
read_str = lambda: sys.stdin.readline().strip()
read_tup = lambda: map(int, sys.stdin.readline().split())
read_list = lambda: list(map(int, sys.stdin.readline().split()))
mod = 10 ** 9 + 7

def check(s, first, second, one, two, j = 0):
    dis = j
    for i in range(j, 10):
        if one - two > second or two - one > first:
            return dis

        dis += 1
        if i & 1:
            second -= 1
            if s[i] == '1':
                two += 1
            if s[i] == '?':
                return  min(check(s, first, second, one, two + 1, i + 1), check(s, first, second, one, two, i + 1))
        else:
            first -= 1
            if s[i] == '1':
                one += 1
            if s[i] == '?':
                return min(check(s, first, second, one + 1, two, i + 1), check(s, first, second, one, two, i + 1))
    return dis

def solve():
    s = read_str()
    res = check(s, 5, 5, 0, 0)
    print(res)


def main():
    t = read_int()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()