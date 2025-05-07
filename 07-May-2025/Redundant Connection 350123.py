# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class DisjointSet:
        def __init__(self, n):
            self.root = [i for i in range(n+1)]
            self.size = [1] * (n+1)
        def get(self, a):
            if a == self.root[a]:
                return a
            self.root[a] = self.get(self.root[a])
            return self.root[a]
        def union(self, a, b):
            a = self.get(a)
            b = self.get(b)
            if a == b:  
                return False
            if self.size[a] < self.size[b]:
                a, b = b, a 
            self.root[b] = a
            self.size[a] += self.size[b]  
            return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DisjointSet(n)
        ans =[]
        for i,j in edges:
            if not dsu.union(i,j):
                ans = [i,j]
        return ans
