# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcf(a,b):
            if a%b == 0:
                return b
            return gcf(b,a%b)
        n = len(nums)
        count=0
        l,r =0,0
        while r<n:
            l=r
            temp = nums[r]
            while l<n:
                temp = gcf(temp,nums[l])
                if gcf(temp,nums[l]) == k:
                    count+=1
                l+=1
            r+=1
        return count