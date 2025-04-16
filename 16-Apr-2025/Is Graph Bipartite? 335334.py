# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        for j in range(n):
            color = [-1] * n
            que = deque()
            color[j] = 1
            que.append((graph[j],color[j]))
            while que:
                _n =len(que)
                curr,flag = que.popleft()
                for _ in range(_n):
                    for i in curr:
                        if color[i] == flag:
                            return False
                        elif color[i] == -1:
                            color[i] = flag^1
                            que.append((graph[i],color[i]))
        return True
