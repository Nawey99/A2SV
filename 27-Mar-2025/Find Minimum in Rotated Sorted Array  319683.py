# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low<high:
            mid = (high+low)//2
            if nums[high]>nums[mid]:
                high = mid
            elif nums[high]<nums[mid]:
                low = mid+1
        return nums[low]
            