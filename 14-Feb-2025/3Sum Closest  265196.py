# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        Min = float("inf")
        Sum = 0
        for i in range(n-2):
            target1 = target - nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                res = abs(target - (nums[i]+nums[l]+nums[r]))
                if res < Min:
                    Sum = nums[i]+nums[l]+nums[r]
                Min = min(Min,res)
                if nums[l] + nums[r] > target1:
                    r -=1
                else:
                    l+=1
        return Sum