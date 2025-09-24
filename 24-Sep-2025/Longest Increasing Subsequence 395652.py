# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        num_of_min = [0]* n
        for idx in range(n):
            Max = 0
            for i in range(idx,-1,-1):
                if nums[i] < nums[idx]:
                    Max = max (Max , num_of_min[i])
            num_of_min[idx] = Max+1
        return max(num_of_min)