# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class DisjointSet:
    def __init__(self,n):
        self.parent  = {i:i for i in range(1,n+1)}
        self.size ={i:1 for i in range(1,n+1)}
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
            else:
                self.parent[ypar] = xpar
                self.size[xpar] += self.size[ypar]
    def is_connected(self,x,y):
        return self.get(x) == self.get(y)
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        Union = DisjointSet(n)
        ans = set()
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    Union.union(i+1,j+1)
        for i in range(n):
            ans.add(Union.get(i+1))
        return len(ans)
