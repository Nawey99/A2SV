# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x):
            if x<0: return 0

            re = 0
            l, cur = 0,0
            for r in range(len(nums)):
                cur += nums[r]

                while cur>x:
                    cur -= nums[l]
                    l+=1
                re+=(r-l+1)
            return re


        x= helper(goal) - helper(goal-1) 
        return x