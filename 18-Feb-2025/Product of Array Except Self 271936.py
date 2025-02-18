# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        total = 1
        total0 = 1
        res = []
        count = 0
        for i in nums:
            if i == 0 and count == 0:
                count +=1
                continue
            total0 *=i
        for i in nums:
            total *=i
        for i in nums:
            if i == 0:
                res.append(total0)
            else:
                res.append(total//i)
        return res