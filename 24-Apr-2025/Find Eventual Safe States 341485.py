# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        arr = [0] * n
        dic = defaultdict(list)
        que = deque()
        arr = [0] * n
        ans = []
        for i in range(n):
            arr[i] = len(graph[i])
            for j in graph[i]:
                dic[j].append(i)
        for i in range(n):
            if arr[i] == 0:
                que.append(i)
        while que:
            n= len(que)
            for _ in range(n):
                curr = que.popleft()
                ans.append(curr)
                for i in dic[curr]:
                    arr[i] -= 1
                    if arr[i] == 0:
                        que.append(i)
        return sorted(ans)
