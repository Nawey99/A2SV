# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(grid)
        ans = 0 
        m_row = []
        heapify(m_row)
        for i in range(n):
            _n = len(grid[i])
            for j in range(_n):
                grid[i][j] = -grid[i][j]
            heapify(grid[i])
            for _ in range(limits[i]):
                heappush(m_row,heappop(grid[i]))
        for _ in range(k):
            ans += heappop(m_row)
        return -ans

