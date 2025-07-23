# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class DisjointSet:
    def __init__(self):
        self.parent = {ch: ch for ch in string.ascii_lowercase}
        self.size = {ch: 1 for ch in string.ascii_lowercase}
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
            return False
        else: 
            return True
    def is_connected(self,x,y):
        return self.get(x) == self.get(y)
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equations = sorted(equations, key=lambda x: '!=' in x)
        Union = DisjointSet()
        n = len(equations)
        for i in range(n):
            if equations[i][1] == '=':
                Union.union(equations[i][0],equations[i][-1])
            else:
                if Union.get(equations[i][0]) == Union.get(equations[i][-1]):
                    return False
        return True