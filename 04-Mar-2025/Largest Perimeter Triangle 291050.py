# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        r = 2
        nums.sort(reverse=True)
        pr = [0]
        n = len(nums)
        for i in range(n):
            pr.append(pr[-1]+nums[i])
        while r<n:
            x = nums[l+1]+nums[r]
            if nums[l]<x:
                ans= pr[r+1]-pr[l]
                break
            l+=1
            r+=1
        return ans