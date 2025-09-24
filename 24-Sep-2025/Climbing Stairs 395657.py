# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(x):
            if x == 0 or x == 1:
                return 1
            if x not in memo:
                memo[x] =  dp(x-1) + dp(x-2)
            return memo[x]
        return dp(n)