# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def bs(x):
            sub = 0
            curr = 0
            for n in nums:
                curr += n 
                if curr > x :
                    sub +=1
                    curr = n
            return sub+1 <= k
        low,high = max(nums),sum(nums)
        res = high
        while low <= high:
            mid = (low + high )//2
            if bs(mid):
                high = mid - 1
                res = mid
            else:
                low = mid +1
        return res
