# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0,1:1,2:1}
        def dp(x):
            if x not in memo:
                memo[x] = dp(x-1) + dp(x-2) + dp(x-3)
            return memo[x]
        return dp(n)