# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total= (len(nums)* (len(nums) +1))//2
        t = 0
        for i in nums:
            t +=i
        return total-t
