# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        ans = n-1
        Max = 0
        if n == 1:
            return True
        for i in range(n):
            Max = max(Max,nums[i])
            if Max == 0 and i < n-1:
                return False
            Max -=1
        return True