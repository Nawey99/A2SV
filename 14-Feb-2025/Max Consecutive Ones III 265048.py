# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        max_w=0
        zeronums=0
        n = len(nums)

        for r in range(n):
            if nums[r] == 0:
                zeronums +=1

            while zeronums>k:
                if nums[l] == 0:
                    zeronums -=1
                l +=1
            
            w = r-l+1
            max_w = max(max_w,w)
        return max_w