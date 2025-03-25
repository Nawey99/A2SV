# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(l,r):
            if l > r:
                return -1
            m = (l+r)//2
            if target ==  nums[m]:
                return m
            elif target > nums[m]:
                return helper(m+1,r)
            else:
                return helper(l,m-1)
        n = len(nums)-1
        return helper(0,n)