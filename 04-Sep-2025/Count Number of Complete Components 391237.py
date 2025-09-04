# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class DisjointSet:
    def __init__(self,n):
        self.parent  = {i:i for i in range(0,n)}
        self.size ={i:1 for i in range(0,n)}
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
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        Union = DisjointSet(n)
        parents = defaultdict(list)
        edge_number = defaultdict(int)
        ans = 0
        m = len(edges)
        parent = defaultdict(bool)
        for i in edges:
            edge_number[i[0]] +=1
            edge_number[i[1]] +=1
            Union.union(i[0],i[1])
        for i in range(n):
            parents[Union.get(i)].append(i)
        for key in parents.keys():
            parent[key] = True
        for i in range(n):
            if edge_number[i] != len(parents[Union.get(i)])-1:
                parent[Union.get(i)] = False
        for val in parent.values():
            if val:
                ans+=1
        return ans