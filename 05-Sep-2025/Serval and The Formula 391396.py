# Problem: Serval and The Formula - https://codeforces.com/problemset/problem/2085/C

import sys
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def solution():
    n,m =II()
    if  n == m:
        return -1
    if n & m == 0:
        return 0
    length_of_bit = max(n,m).bit_length()
    next_power = 2 ** length_of_bit
    k = next_power - max(n,m)
    return k

# cases = 1
cases = I()
for i in range(cases):
    print(solution())