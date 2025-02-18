# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_val = float("inf")
        total = 0
        res = 0
        max_val = float("-inf")
        for i in nums:
            min_val = min(min_val,total)
            total += i
            max_val = max(max_val,total-min_val)
        return max_val