# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        def dp(idx):
            if idx == n:
                return 0
            if idx > n:
                return float('inf')
            if idx not in memo:
                memo[idx] = min(cost[idx] + dp(idx+1),cost[idx] + dp(idx+2))
            return memo[idx]
        return min(dp(0),dp(1))