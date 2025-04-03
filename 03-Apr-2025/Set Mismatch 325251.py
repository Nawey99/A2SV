# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mis,dub = 0,0
        for num in nums:
            if nums[abs(num)-1] <0:
                dub = abs(num)
                nums[abs(num)-1] = -(nums[abs(num)-1])
            nums[abs(num)-1] = -(nums[abs(num)-1])
        for i in range(n):
            if nums[i] > 0:
                mis = i+1
        return [dub,mis]