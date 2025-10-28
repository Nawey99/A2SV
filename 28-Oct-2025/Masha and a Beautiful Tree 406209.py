# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

import sys
from collections import Counter,defaultdict
from itertools import accumulate 
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def solution():
    n = I()
    arr = IL()
    swap = 0
    def merge(left,right):
            l = 0
            while l < len(left) and l < len(right) and left[l] == right[l]:
                l += 1
            if l < len(left) and l < len(right) and left[l] > right[l]:
                nonlocal swap
                swap +=1
                return right + left
            return left + right
    def mergeSort(arr):
        if len(arr) == 1:
            return arr
        mid = len(arr)//2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        mix = merge(left,right)
        return mix
    temp =  mergeSort(arr)
    temp1 = sorted(arr)
    return swap if temp1 == temp else -1

# cases = 1
cases = I()
for i in range(cases):
    print(solution())