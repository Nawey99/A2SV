# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        Min,Max,Sum=0,0,0
        for i in nums:
            Sum += i
            if Sum > Max:
                Max = Sum
            if Sum<Min:
                Min = Sum
        return abs(Max-Min)