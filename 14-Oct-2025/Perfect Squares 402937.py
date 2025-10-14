# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        def dp(Sum):
            if Sum > n:
                return float('inf')
            if Sum  == n:
                return 0
            if Sum not in memo:
                Min = float('inf')
                for i in range(1,int(sqrt(n))+1):
                    Min = min(Min,dp(Sum + (i*i))+1)
                memo[Sum] = Min
            return memo[Sum]
        return dp(0)