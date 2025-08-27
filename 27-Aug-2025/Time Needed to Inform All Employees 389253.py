# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjlist= defaultdict(list)
        start = 0
        for i in range(n):
            adjlist[manager[i]].append(i)
            if manager[i] == -1:
                start = i
        def dfs(x):
            if x not in adjlist:
                return 0
            Max = 0
            for i in adjlist[x]:
                Max = max(dfs(i),Max)
            return Max + informTime[x]
        return dfs(start)
            