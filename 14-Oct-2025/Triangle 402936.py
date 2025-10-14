# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def dp(x,y):
            if x == len(triangle):
                return 0
            if (x,y) not in memo:
                memo[(x,y)] = triangle[x][y]+ min(dp(x+1,y),dp(x+1,y+1))
            return memo[(x,y)]
        return dp(0,0)