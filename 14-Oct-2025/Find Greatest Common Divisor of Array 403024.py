# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        def gcf(a,b):
            if a%b == 0:
                return b
            return gcf(b,a%b)
        return gcf(nums[-1], nums[0])