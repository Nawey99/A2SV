# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def checker(x):
            p_sum = calcu(x)
            for i in range(len(nums)):
                if nums[i]-p_sum[i] >0:
                    return False
            return True

        def calcu(x):
            temp = [0] * (len(nums)+1)
            for i in range(x):
                l,r,v = queries[i]
                temp[l] += v
                temp [r+1] -=v
            for i in range(1,len(temp)):
                temp[i] += temp[i-1]
            temp.pop()
            return temp
        
        low,high = 0, len(queries)-1
        while low <= high:
            mid = (low+high)//2
            if checker(mid):
                high =mid-1
            else:
                low = mid+1
        return low if checker(low) else -1