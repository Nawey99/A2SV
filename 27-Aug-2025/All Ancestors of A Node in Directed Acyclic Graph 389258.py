# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            if node in memo:
                return memo[node]
            
            ancestors = set()
            for parent in in_list[node]:
                ancestors.add(parent)
                ancestors |= dfs(parent) 
            
            memo[node] = ancestors
            return ancestors

        in_list = defaultdict(list)
        for u, v in edges:
            in_list[v].append(u)
        
        memo = {}
        ans = []
        for i in range(n):
            ans.append(sorted(dfs(i)))
        
        return ans