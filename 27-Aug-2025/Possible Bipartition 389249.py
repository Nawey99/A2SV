# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node,col):
            for i in adj_list[node]:
                if i not in color:
                    color[i] = 3- col
                    if not dfs(i,3-col):
                        return False
                else:
                    if color[i] != 3-col:
                        return False
            return True
        adj_list = defaultdict(list)
        for x,y in dislikes:
            adj_list[x].append(y)
            adj_list[y].append(x)
        color = defaultdict(int)
        for i in range(1,n+1):
            if i not in color:
                color[i] = 1
                if not dfs(i,color[i]):
                    return False
        return True
