# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        b_max = 0
        Max_l =1
        l = 0
        r = 0
        while r< n:
            if b_max & nums[r] == 0:
                b_max ^= nums[r]
                r+=1
                Max_l = max(Max_l,r-l)
            else:
                b_max ^= nums[l]
                l+=1
        return Max_l
                
