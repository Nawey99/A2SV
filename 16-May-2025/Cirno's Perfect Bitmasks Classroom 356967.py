# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

class DisjointSet:
    def __init__(self,n):
        self.parent  = {i:i for i in range(1,n+1)}
        self.size ={i:1 for i in range(1,n+1)}
        self.result = {i:[i] for i in range(1,n+1)}
    def get(self, x):
        if self.parent[x]!=x:
            self.parent[x] = self.get(self.parent[x])
        return self.parent[x]
    def union(self, x,y):
        xpar = self.get(x)
        ypar = self.get(y)
        if xpar != ypar:
            if self.size[xpar] < self.size[ypar]:
                self.parent[xpar] = ypar
                self.size[ypar] += self.size[xpar]
                self.result[ypar].extend(self.result[xpar])
            else:
                self.parent[ypar] = xpar
                self.size[xpar] += self.size[ypar]
                self.result[xpar].extend(self.result[ypar])
    def is_connected(self,x,y):
        return self.get(x) == self.get(y)
import random
import sys
from collections import Counter,defaultdict
from itertools import accumulate 
def I(): return int(sys.stdin.readline().strip())
def II(): return map(int, sys.stdin.readline().strip().split())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def IS(): return sys.stdin.readline().strip().split()
def psum(a): return [0] + list(accumulate(a))
rand = random.randrange(2^62)
def wrapper(x): return x ^ rand
def solution():
    n = I()
    if n == 1:
        return 3
    bits = bin(n)
    bits = bits[2::]
    bits = bits[::-1]
    m = len(bits)
    for i in range(m):
        if bits[i] == '1':
            if i == m-1:
                ans = 1<<i 
                return ans+1
            else:
                return 1<<i
# cases = 1
cases = I()
for i in range(cases):
    print(solution())